$(document).ready(function() {
    $(".btn-submit").hide();
    $('#questions').on("keyup", function() {
        if ($(this).val() == "") {
            $(".btn-submit").fadeOut();
        } else {
            $(".btn-submit").fadeIn();
        }
    })
});