import os
import pandas as pd
import difflib
from flask import Flask, request, render_template
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import mysql.connector

app = Flask(__name__)
app.debug = True  # Enable debug mode to see errors in logs

# ------------------ Database ------------------
db_config = {
    "host": os.environ.get("MYSQL_HOST"),
    "user": os.environ.get("MYSQL_USER"),
    "password": os.environ.get("MYSQL_PASSWORD"),
    "database": os.environ.get("MYSQL_DB")
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

# ------------------ Movie Recommendation ------------------
required_cols = ['title', 'genres', 'keywords', 'tagline', 'cast', 'director']

# Load CSV safely
movies_data = pd.read_csv("movies.csv", dtype=str, low_memory=False)

# Add missing columns if not present
for col in required_cols:
    if col not in movies_data.columns:
        movies_data[col] = ""

# Replace NaN with empty strings
movies_data = movies_data.fillna('').reset_index(drop=True)

# Combine features
combined_features = (
    movies_data['genres'] + ' ' +
    movies_data['keywords'] + ' ' +
    movies_data['tagline'] + ' ' +
    movies_data['cast'] + ' ' +
    movies_data['director']
)

vectorizer = TfidfVectorizer()
feature_vector = vectorizer.fit_transform(combined_features)
similarity = cosine_similarity(feature_vector)
list_of_all_titles = movies_data['title'].fillna('').astype(str).tolist()

# ------------------ Routes ------------------
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/book", methods=["GET", "POST"])
def book():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title FROM movies")
    movies = cursor.fetchall()
    cursor.close()
    conn.close()

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        movie_id = request.form["movie"]
        seat_number = request.form["seat"]
        seats = int(request.form["seats"])
        price = seats * 200  # Rs.200 per seat

        conn = get_db_connection()
        cursor = conn.cursor()

        # Check if user already exists
        cursor.execute("SELECT id FROM users WHERE email=%s", (email,))
        user = cursor.fetchone()
        if user:
            user_id = user[0]
        else:
            cursor.execute(
                "INSERT INTO users (name, email, password) VALUES (%s,%s,%s)",
                (name, email, "1234")
            )
            user_id = cursor.lastrowid

        # Insert booking
        cursor.execute(
            "INSERT INTO bookings (user_id, movie_id, seat_number, price) VALUES (%s,%s,%s,%s)",
            (user_id, movie_id, seat_number, price)
        )
        conn.commit()
        cursor.close()
        conn.close()

        return render_template(
            "book.html",
            movies=movies,
            success=f"Booking Successful! Total Price: {price}",
            seats=seats,
            seat_number=seat_number,
            movie_name=[m[1] for m in movies if str(m[0]) == movie_id][0],
            total_price=price
        )

    return render_template("book.html", movies=movies)

@app.route("/display")
def display():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT b.id, u.name, u.email, m.title, b.seat_number, b.price, b.booking_time
        FROM bookings b
        JOIN users u ON b.user_id = u.id
        JOIN movies m ON b.movie_id = m.id
    """)
    bookings = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("display.html", bookings=bookings)

# ------------------ Recommendations ------------------
@app.route("/recommend", methods=["GET", "POST"])
def recommend():
    if request.method == "POST":
        movie_name = request.form["movie_name"]
        find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles, n=1, cutoff=0.6)

        if not find_close_match:
            return render_template("recommend.html", message=f"Sorry, no match found for {movie_name}")

        close_match = find_close_match[0]
        index_of_movie = movies_data[movies_data.title == close_match].index[0]
        similarity_score = list(enumerate(similarity[index_of_movie]))
        sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)
        recommendations = [movies_data.loc[m[0], 'title'] for m in sorted_similar_movies[1:6]]

        return render_template("recommend.html", recommendations=recommendations, original_movie=close_match)

    return render_template("recommend.html")

# ------------------ Run App ------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
