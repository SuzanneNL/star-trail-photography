/*Function sendMail connects contact form to the star-trail-photography template from EmailJS
After submitting the form and a short time out, a success flash message becomes visible.*/
function sendMail(contactForm) {
	emailjs.send("service_8n27bcn", "star-trail-photography", {
		"from_name": contactForm.name.value,
		"from_email": contactForm.emailaddress.value,
		"message": contactForm.message.value
	});
	setTimeout(() => {
		messageSent();
	}, 600);
	return false; // To block from loading a new page
}

//Shows success flash message
function messageSent() {
	document.querySelector('#after-submit').classList.remove('hide');
}