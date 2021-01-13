function sendMail(contactForm) {
    emailjs.send("service_8n27bcn", "star-trail-photography", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.emailaddress.value,
        "message": contactForm.message.value
    })
    setTimeout(() => {
		messageSent();
	}, 600);
    return false;  // To block from loading a new page
}

function messageSent(){
    document.querySelector('#after-submit').classList.remove('hide');
}

