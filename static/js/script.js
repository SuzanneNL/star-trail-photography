  $(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    $('.datepicker').datepicker({
        format: "dd mmmm, yyyy",
        maxDate: new Date(),
        showClearBtn: true,
        i18n: {
            done: "Select"
        }
    });
  });