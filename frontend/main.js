$(document).ready(function () {
    
    $('.text').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "fadeIn",
            sync: true,
        },
        out: {
            effect: "fadeOutDown",
            sync: true,
        },
    })

    // Siri Configuration
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 800,
        height: 200,
        style: "ios9",
        amplitude: "1.5",
        speed: "0.30",
        autostart: true,
      });

      // Siri Message Animation
    $('.siri-message').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "fadeInUp",
            sync: true,
        },
        out: {
            effect: "fadeOutDown",
            sync: true,
        },
    })

    // Mic Btn click event
    $("#MicBtn").click(function () { 
        eel.playAssistantSound()
        $("#oval").attr("hidden", true);
        $("#siriWave").attr("hidden", false);
        
    });



});