function getBotResponse(input) {
    //rock paper scissors
    if (input == "rock") {
        return "paper";
    } else if (input == "paper") {
        return "scissors";
    } else if (input == "scissors") {
        return "rock";
    }

    // Simple responses
    if (input == "hello") {
        return "Hello there!";
    } else if (input == "HELLO") {
        return "Hello threr!";
    } else if (input == "Hello") {
        return "Hrllo there!";
    } else if (input == "HI") {
        return "Hello!";
    } else if (input == "Hi") {
        return "Hello!";
    } else if (input == "hi") {
        return "Hello!";
    } else if (input == "HOW ARE YOU") {
        return "Good!";
    } else if (input == "How are you") {
        return "Good!";
    } else if (input == "how are you") {
        return "Good!";
    } else if (input == "") {
        return "Good!";
    } else if (input == "goodbye") {
        return "Talk to you later!";
    } else {
        return "Try asking something else!";
    }
}