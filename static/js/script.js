
let anonymous_checkbox = document.getElementById("anonymous_checkbox");
let userNameForm = document.getElementById("user_full_name");
let userNickName = document.getElementById("user_nickname");
let editProfile = document.getElementById('edit-profile');
let editProfileForm = document.getElementById('edit-profile-form');


anonymous_checkbox.addEventListener('change', function(){
    if ( this.checked) {
        userNameForm.classList.add ('hide');
        userNickName.classList.remove ('hide');
    }else {
            userNameForm.classList.remove('hide');
            userNickName.classList.add('hide');
    }
})

editProfile.addEventListener('click', () => editProfileForm.classList.remove('hide'));