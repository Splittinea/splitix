document.addEventListener("DOMContentLoaded", () => {

    // Backend init
    new QWebChannel(qt.webChannelTransport, channel => {

        /* 
        Accessing backend object from the channel provided at

        class HomeScreen(QMainWindow) :
            def __init__(self) :
                ...
                self.channel = QWebChannel()
                self.backend = Backend()
                ...
    
        */

        const backend = channel.objects.backend;
        
        document.querySelectorAll(".custom-btn").forEach(btn => {     // -> homeScreen.html => <div class="custom-btn">
            const label = btn.querySelector("span").innerText.trim(); // -> homeScreen.html => <div class="buttons">

            // Buttons control depending of provided label

            // Backend location : ../homeScreen.py => class Backend(QObject)
            switch (label) {
                case "NEW PROJECT": btn.onclick = () => backend.newProject(); break;    // -> ../homeScreen.py => def newProject()
                case "OPEN PROJECT": btn.onclick = () => backend.openProject(); break;  // -> ../homeScreen.py => def openProject()
                case "IDE SETTINGS": btn.onclick = () => backend.openSettings(); break; // -> ../homeScreen.py => def openSettings()
                case "EXIT IDE": btn.onclick = () => backend.exitApp(); break;          // -> ../homeScreen.py => def exitApp()
            }

        });
    });
});