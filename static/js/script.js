//Global variables
var currentYear = (new Date()).getFullYear();

//Makes the functions inside available after the document is loaded
$(document).ready(function() {

    //Initializes sidenav on the right, for smaller screens
    $('.sidenav').sidenav({
        edge: "right"
    });

    //Initializes modals
    $('.modal').modal();

    //Initializes select option
    $('select').formSelect();

    //Initializes Scrollspy, with an offset of 50px
    $('.scrollspy').scrollSpy({
        scrollOffset: 50
    });

    /*Initializes Datepicker. 
    It prevents a user from selecting a date in the future, 
    and navigating to a future year in the dropdown menu.
    Sources: Stack Overflow and eppand.com, see README file
    under 'Sources'*/
    $("#year").text((new Date()).getFullYear());
    $('.datepicker').datepicker({
        format: "yyyy/mm/dd",
        changeYear: true,
        maxYear: currentYear,
        maxDate: new Date(),
        showClearBtn: true,
        i18n: {
            done: "Select"
        }
    });
});