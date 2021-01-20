/*This script applies to the profile page. There, the number of images on the page is counted.
If the number is zero, a message becomes visible to the user (that there are no images)*/
if(document.images.length == 0) {
	showNoImagesMessage();
}

function showNoImagesMessage() {
	document.querySelector('#no-images').classList.remove('hide');
}