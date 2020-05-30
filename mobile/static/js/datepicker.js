$(function(){
    $("#datepicker").datepicker({
        dateFormat: "dd-mm-yy",
        changeMonth: true,
        changeYear: true,
        yearRange: '1900:2000',
        inline: true
    });
    $( "#datepicker" ).datepicker( "setDate", null );
});