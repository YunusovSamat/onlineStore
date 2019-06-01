const login_form = document.getElementsByClassName('login_form')[0];
const login_form_open = document.getElementsByClassName('login_form_open')[0];
const login_form_close = document.getElementById('login_close');

login_form_open.onclick = function() {
    login_form.style.display = 'block';
};

login_form_close.onclick = function() {
    login_form.style.display = 'none';
};

login_form.onclick = function (e) {
    if (e.target === login_form) {
        login_form.style.display = 'none';
    }
};

const signup_form = document.getElementsByClassName('signup_form')[0];
const signup_form_open = document.getElementsByClassName('signup_form_open')[0];
const signup_form_close = document.getElementById('signup_close');

signup_form_open.onclick = function() {
    login_form.style.display = 'none';
    signup_form.style.display = 'block';

};

signup_form_close.onclick = function() {
    signup_form.style.display = 'none';
};

signup_form.onclick = function (e) {
    if (e.target === signup_form) {
        signup_form.style.display = 'none';
    }
};