var etext = document.getElementById("etext");
etext.addEventListener("keyup", function(e) {
    e.preventDefault();
    var sug = document.getElementById("sug");
    // console.log(sug);
    sug.style.visibility = "visible";
    if (document.getElementById("etext").value == "") {
        sug.style.visibility = "hidden";
    }
});





$(document).ready(function() {
    $(document).on("submit", "#eform", function(e) {
        e.preventDefault();
        let input = $('#etext').val();
        // alert($(".box"));
        // $("div").setAtt
        $(".box").append(`<div class= 'item right'> <div class = 'msg'> <p>${input} </p> </div> </div>`);

        $.ajax({
            url: "/takeOutputp",
            method: "POST",
            data: {
                message: input
            },
            success: function(data) {

                $(".box").append(`<div class="item left">
                <div class="icon">
                    <i class="fa fa-user"></i>
                </div>
                <div class="msg">
                    <p>${data}</p>
                </div>
            </div>`);

                $("#etext").val("");
            }
//            error: function(data) {
//
//                $(".box").append(`<div class="item left">
//                <div class="icon">
//                    <i class="fa fa-user"></i>
//                </div>
//                <div class="msg">
//                    <p>sorry!! we can't help you</p>
//                </div>
//            </div>`);
//
//                $("#etext").val("");
//
//
//                $(".box").scrollTop(10000);
//            }
        })
    })
})