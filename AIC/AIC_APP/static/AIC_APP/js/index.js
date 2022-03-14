$(document).ready(function() {
    let etext = $("#etext");
    $(".box").scrollTop(1000);
    $('#eform').on("submit", function(e) {
        e.preventDefault();
        let input = $('#etext').val();
        $('#etext').val('');
        // alert($(".box"));
        // $("div").setAtt
        let temp1 = $(`<div class="item right d-flex justify-content-between gap-2 align-items-center">
                                <div class="msg px-2">
                                    <p>${input}</p>
                                </div>
                                <div class="icon">
                                    <i class="bi bi-person-fill"></i>
                                </div>
                            </div>`);
        $(".box").append(temp1);
        // $(".box").scrollTop(height);
        $(".box").animate({ scrollTop: $('.box').prop("scrollHeight") }, 700);
        $("#etext").prop('disabled', true);
        $.ajax({
            url: "/takeOutputdp",
            method: "POST",
            data: {
                message: input,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function(data) {
                let temp = $(`<div class="item left d-flex align-items-start">
                                <div class="icon">
                                    <img src="../images/chatbot.svg">
                                </div>
                                <div class="msg">
                                    <p>${data}</p>
                                </div>
                            </div>`);
                $(".box").append(temp);
                $("#etext").prop('disabled', false);
                $("#etext").val("");
                temp.fadeIn(200);
                $(".box").animate({ scrollTop: $('.box').prop("scrollHeight") }, 700);

            },
            error: function(data) {

                $(".box").append(`<div class="item left">
                                   <div class="icon">
                                       <i class="fa fa-user"></i>
                                   </div>
                                   <div class="msg">
                                       <p>sorry!! we can't help you</p>
                                   </div>
                               </div>`);
                console.log($(".box").children().last().height());
                $(".box").animate({ scrollTop: $('.box').prop("scrollHeight") }, 600);
                $("#etext").val("");
                $("#etext").prop('disabled', false);
            }
        })
    })
})