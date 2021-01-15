//Source: W3Schools, see README file under 'Sources'.
//This gets the button:
var backToTopButton = document.getElementById("backtotop");

// When a user scrolls down 20px from the top of the page, the button appears.
window.onscroll = function() {
	scrollFunction();
};

function scrollFunction() {
	if(document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
		backToTopButton.style.display = "block";
	} else {
		backToTopButton.style.display = "none";
	}
}

// By clicking on the button, the user scrolls up to the top of the page at once.
function topFunction() {
	document.body.scrollTop = 0; // For Safari
	document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}