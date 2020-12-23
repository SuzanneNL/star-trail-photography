var currentYear = (new Date).getFullYear();

$(document).ready(function(){
$('.sidenav').sidenav({edge: "right"});
$('.modal').modal();
$('select').formSelect();
$('.scrollspy').scrollSpy({
    scrollOffset: 0
    });
$("#year").text( (new Date).getFullYear() );
$('.datepicker').datepicker({
    format: "dd mmmm, yyyy",
    changeYear: true,
    maxYear: currentYear,
    maxDate: new Date(),
    showClearBtn: true,
    i18n: {
        done: "Select"
    }
});
});