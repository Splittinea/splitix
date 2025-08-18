document.addEventListener("DOMContentLoaded", () => {
    if (typeof qt === "undefined") {
        console.error("qt object not ready!");
        return;
    }

    new QWebChannel(qt.webChannelTransport, channel => {
        const backend = channel.objects.backend;
        console.log("Backend connected:", backend);

        document.querySelectorAll(".custom-btn").forEach(btn => {
            const label = btn.querySelector("span").innerText.trim();
            switch(label) {
                case "NEW PROJECT": btn.onclick = () => backend.newProject(); break;
                case "OPEN PROJECT": btn.onclick = () => backend.openProject(); break;
                case "IDE SETTINGS": btn.onclick = () => backend.openSettings(); break;
                case "EXIT IDE": btn.onclick = () => backend.exitApp(); break;
            }
        });
    });
});