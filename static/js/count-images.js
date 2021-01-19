if (document.images.length == 0) {
    showNoImagesMessage()
}

function showNoImagesMessage() {
	document.querySelector('#no-images').classList.remove('hide');
}