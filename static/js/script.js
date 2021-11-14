// Timeout Chip: handles multiple Flask flash messages.
setTimeout(()=> {
    let flashMessage = document.getElementsByClassName("flash-message");

    for (let i = 0; i < flashMessage.length; i++) {
        flashMessage[i].style.display="none";
    }
}, 5000);