$(document).ready(function () {
    
    // Display message from user input
    eel.expose(displayMessage)
    function displayMessage(message) {
        $(".siri-message li:first").text(message);
        $(".siri-message").textillate('start');
    }

    // Display hood
    eel.expose(showHood)
    function showHood() {
        $("#oval").attr("hidden", false);
        $("#siriWave").attr("hidden", true);
    }

});