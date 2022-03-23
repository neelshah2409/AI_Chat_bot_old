$(document).ready(function() {
    $(".btn-submit").hide();
    $('.question').on("keyup", function() {
        let temp = $($(this).parent().children()[2]).children()[0];
        if ($(this).val() == "") {

        } else {
            $(temp).fadeIn();
        }
    })
});