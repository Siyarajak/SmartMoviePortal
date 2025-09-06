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
    const msg = `You have successfully booked ${seats} seat(s) for the movie ${movie_name}. Your seat number is ${seat_number}.`;
    const utterance = new SpeechSynthesisUtterance(msg);
    window.speechSynthesis.speak(utterance);
}



// For movie recommendations
function speakRecommendations(original, recs) {
    const msg = `Top 5 movies similar to ${original} are ${recs.join(', ')}.`;
    const utterance = new SpeechSynthesisUtterance(msg);
    window.speechSynthesis.speak(utterance);
}

