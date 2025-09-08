# 🎬 SmartMoviePortal

SmartMoviePortal is a Flask-based web application that allows users to book movie tickets, view all bookings, and get movie recommendations. It combines a simple yet modern frontend with a functional backend for seamless movie ticket management.

## 🚀 Features

Book a Ticket : 1.Enter your name, email, select a movie, and book seats. 

   2.Supports multiple seat bookings with automatic price calculation.

View All Bookings : Displays all ticket bookings with details (Name, Email, Movie, Seat, Price, and Time).

Movie Recommendation System : Enter a movie name to get smart recommendations based on your choice.

Interactive Frontend : Clean and modern UI using HTML, CSS, and JavaScript.


## 🛠️ Tech Stack

Backend: Python (Flask)

Frontend: HTML, CSS, JavaScript

Database: CSV (movies.csv for storing bookings & movie data)

Deployment Ready: Includes Procfile for Heroku deployment

## 📂 Project Structure
 
    SmartMoviePortal/
    │── static/              # Static files (CSS, JS, Images)
    │── templates/           # HTML templates (Jinja2)
    │── app.py               # Main Flask application
    │── movies.csv           # Movie dataset and bookings
    │── requirements.txt     # Python dependencies
    │── Procfile.txt         # Deployment file (Heroku)
    │── .gitignore           # Git ignore file

## ⚙️ Installation & Setup

1.Clone the repository

     git clone https://github.com/Siyarajak/SmartMoviePortal.git
     cd SmartMoviePortal


2.Create a virtual environment

    python -m venv venv
    source venv/bin/activate   # On Linux/Mac
    venv\Scripts\activate      # On Windows


3.Install dependencies

    pip install -r requirements.txt


4.Run the application

    python app.py


5.Open in Browser

    http://127.0.0.1:5000


 ## 🌐 Deployment

Since the repository already contains a Procfile.txt, you can deploy it easily on Heroku:

    heroku login
    heroku create smart-movie-portal
    git push heroku main
    heroku open   
    
## 📸 Screenshots
### logo 
<img width="107" height="83" alt="image" src="https://github.com/user-attachments/assets/92d0ce8e-9c36-4863-af98-6d6af3229e88" />

### 🏠 Homepage
<img width="1899" height="1073" alt="Screenshot 2025-09-08 204143" src="https://github.com/user-attachments/assets/ddbfaa46-99e8-4fd4-8fb8-b62f574a6c16" />
### 🎟️ Book Ticket
<img width="1898" height="1011" alt="Screenshot 2025-09-08 204154" src="https://github.com/user-attachments/assets/a3179368-e2b3-4e89-ae88-20e93df36757" />
### 🎥 Movie Recommendation
<img width="1889" height="1006" alt="Screenshot 2025-09-08 204220" src="https://github.com/user-attachments/assets/341a384f-ac71-4b76-98a1-1e6011158ed2" />

## 📌 Future Enhancements

Integrate a real database (SQLite / PostgreSQL)

Add authentication (user login & signup)

Implement seat availability system

Improve movie recommendation using more ML models

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo, make changes, and submit a PR.

## 📜 License

This project is licensed under the MIT License – feel free to use and modify.

    

