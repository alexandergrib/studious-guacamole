// Timeout Chip: handles multiple Flask flash messages.
setTimeout(()=> {
    let flashMessage = document.getElementsByClassName("flash-message");

    for (let i = 0; i < flashMessage.length; i++) {
        flashMessage[i].style.display="none";
    }
}, 5000);


const setActive = () => {
    console.log(location.pathname);
    let navLinks =  document.getElementsByClassName('nav-link')
    console.log(navLinks);
    for(let link of navLinks) {
        const classes = link.classList;
        console.log(classes);
        if(classes.contains('active')) {
            link.classList.remove('active');
        }
    }
    switch(location.pathname){
        case '/home':
            document.getElementById('home-page').classList.add('active');
            break;
        case '/health_check':
            document.getElementById('health-page').classList.add('active');
            break;
        case '/blog':
            document.getElementById('blog-page').classList.add('active');
            break;
        case '/profile/':
            document.getElementById('profile-page').classList.add('active');
            break;
        case '/blog/add':
            document.getElementById('add-page').classList.add('active');
            break;
        case '/login':
            document.getElementById('login-page').classList.add('active');
            break;
        case '/register':
            document.getElementById('signup-page').classList.add('active');
            break;
    }
}

document.addEventListener('DOMContentLoaded', setActive);



