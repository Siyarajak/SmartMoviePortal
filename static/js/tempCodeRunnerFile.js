// voice.js

function speakMessage(message) {
    if ('speechSynthesis' in window) {
        const utterance = new SpeechSynthesisUtterance(message);
        window.speechSynthesis.speak(utterance);
    } else {
        console.warn("TTS not supported in this browser.");
    }
}

// For booking confirmation
function speakBooking(seats, seat_number, movie_name) {
    const msg = `Booking Successful! You have booked ${seats} seat(s) for ${movie_name}. Your seat number(s) is/are ${seat_number}.`;
    speakMessage(msg);
}

// For movie recommendations
function speakRecommendations(original_movie, recommendations) {
    const recList = recommendations.join(", ");
    const msg = `Top recommended movies similar to ${original_movie} are: ${recList}.`;
    speakMessage(msg);
}
