/*The makeActive function checks the last part of the URL and based on this part,
adds active classes to the corresponding links in the navigationbar.*/
let url = window.location.href;
let urlSplit = url.split('/');
let thisPage = urlSplit.slice(-1);

function makeActive() {
    if (thisPage == "") {
        document.querySelector('#home').classList.add('active');
    } else if (thisPage == "get_images") {
        document.querySelector('#gallery').classList.add('active');
    } else if (thisPage == "contact") {
        document.querySelector('#contact').classList.add('active');
    } else if (thisPage == "log_in") {
        document.querySelector('#login').classList.add('active');
    } else if (thisPage == "profile_page") {
        document.querySelector('#profile').classList.add('active');
    } else if (thisPage == "sign_up") {
        document.querySelector('#signup').classList.add('active-signup');}
}

makeActive();