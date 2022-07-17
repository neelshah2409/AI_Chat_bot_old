$(document).on("submit", "#feedbackForm", function(e) {
    let feedback = false;
    let chatbot = `<svg id="Layer_1" data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 122.88 119.35"><title>chatbot</title><path style="fill:#fff;" d="M57.49,29.2V23.53a14.41,14.41,0,0,1-2-.93A12.18,12.18,0,0,1,50.44,7.5a12.39,12.39,0,0,1,2.64-3.95A12.21,12.21,0,0,1,57,.92,12,12,0,0,1,61.66,0,12.14,12.14,0,0,1,72.88,7.5a12.14,12.14,0,0,1,0,9.27,12.08,12.08,0,0,1-2.64,3.94l-.06.06a12.74,12.74,0,0,1-2.36,1.83,11.26,11.26,0,0,1-2,.93V29.2H94.3a15.47,15.47,0,0,1,15.42,15.43v2.29H115a7.93,7.93,0,0,1,7.9,7.91V73.2A7.93,7.93,0,0,1,115,81.11h-5.25v2.07A15.48,15.48,0,0,1,94.3,98.61H55.23L31.81,118.72a2.58,2.58,0,0,1-3.65-.29,2.63,2.63,0,0,1-.63-1.85l1.25-18h-.21A15.45,15.45,0,0,1,13.16,83.18V81.11H7.91A7.93,7.93,0,0,1,0,73.2V54.83a7.93,7.93,0,0,1,7.9-7.91h5.26v-2.3A15.45,15.45,0,0,1,28.57,29.2H57.49ZM82.74,47.32a9.36,9.36,0,1,1-9.36,9.36,9.36,9.36,0,0,1,9.36-9.36Zm-42.58,0a9.36,9.36,0,1,1-9.36,9.36,9.36,9.36,0,0,1,9.36-9.36Zm6.38,31.36a2.28,2.28,0,0,1-.38-.38,2.18,2.18,0,0,1-.52-1.36,2.21,2.21,0,0,1,.46-1.39,2.4,2.4,0,0,1,.39-.39,3.22,3.22,0,0,1,3.88-.08A22.36,22.36,0,0,0,56,78.32a14.86,14.86,0,0,0,5.47,1A16.18,16.18,0,0,0,67,78.22,25.39,25.39,0,0,0,72.75,75a3.24,3.24,0,0,1,3.89.18,3,3,0,0,1,.37.41,2.22,2.22,0,0,1,.42,1.4,2.33,2.33,0,0,1-.58,1.35,2.29,2.29,0,0,1-.43.38,30.59,30.59,0,0,1-7.33,4,22.28,22.28,0,0,1-7.53,1.43A21.22,21.22,0,0,1,54,82.87a27.78,27.78,0,0,1-7.41-4.16l0,0ZM94.29,34.4H28.57A10.26,10.26,0,0,0,18.35,44.63V83.18A10.26,10.26,0,0,0,28.57,93.41h3.17a2.61,2.61,0,0,1,2.41,2.77l-1,14.58L52.45,94.15a2.56,2.56,0,0,1,1.83-.75h40a10.26,10.26,0,0,0,10.22-10.23V44.62A10.24,10.24,0,0,0,94.29,34.4Z"/></svg>`;
    $(".box").scrollTop(500);
    $('#feedback').on("click", function(e) {
        e.preventDefault();
    })
    $('#eform').on("submit", function(e) {

        $(".submitBtn").addClass("submitBtnOut", 500);
        $(".submitBtnOut").removeClass("submitBtn");
        feedback = false;
        e.preventDefault();
        let input = $('#etext').val();
        $('#etext').val('');
        let temp1 = $(`<div class="item right d-flex justify-content-start gap-2 align-items-center m-3 col-10">
                                <div class="icon col-2">
                                    <i class="bi bi-person-fill"></i>
                                </div>
                                <div class="msg px-2 text-start">
                                    <p>${input}</p>
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
                let temp = $(`<div class="item left d-flex justify-content-start gap-2 align-items-center m-3 col-10">
                                <div class="icon col-2">
                                    ${chatbot}
                                </div>
                                <div class="msg text-start">
                                    <p>${data}</p>
                                </div>
                            </div>
                            `);
                $(".box").append(temp);
                $("#etext").prop('disabled', false);
                $("#etext").val("");
                temp.fadeIn(200);
                $(".box").animate({ scrollTop: $('.box').prop("scrollHeight") }, 750);
                setTimeout(function() {
                    $(".submitBtnOut").removeClass("submitBtnOut").delay(100).addClass("submitBtn", 0);
                }, 200);

            },
            error: function(data) {
                $(".box").append(`<div class="item left d-flex justify-content-start gap-2 align-items-center m-3 col-10">
                                   <div class="icon col-2">
                                       ${chatbot}
                                   </div>
                                   <div class="msg text-start">
                                       <p>sorry!! we can not help you</p>
                                   </div>
                               </div>`);
                $(".box").animate({ scrollTop: $('.box').prop("scrollHeight") }, 600);
                $("#etext").val("");
                $("#etext").prop('disabled', false);
            }
        })
    })

    $('#feedback').on("click", function() {
        if (!feedback) {
            let temp1 = $(`<div class="item right d-flex justify-content-start gap-2 align-items-center m-3 col-10">
                                <div class="icon">
                                    <i class="bi bi-person-fill"></i>
                                </div>
                                <div class="msg p-2">
                                    <form class="m-0 text-center" method="post" id="feedbackForm">
                                        <h4 class="text-light m-0 text-center py-2 rounded-2">Feedback</h4>
                                        <textarea name="improvementFeatures" placeholder="Enter Your Feedback" id="feedbackInput" rows="4" class="form-control"></textarea>
                                        <button type="submit" class="btn text-light">Submit</button>
                                    </form>
                                </div>
                            </div>`);
            $(".box").append(temp1);
            $(".box").animate({ scrollTop: $('.box').prop("scrollHeight") }, 600);
            $("#etext").val("");
            $("#etext").prop('disabled', false);
            feedback = true;
        }
    })
    e.preventDefault();
    let input = $('#feedbackInput').val();
    $(".right:last-child").html(`<div class="icon col-2">
                                <i class="bi bi-person-fill"></i>
                            </div>
                            <div class="msg text-start px-2">
                                <p>Feedback Submitted</p>
                            </div>`);
    $('#etext').val('');
    $.ajax({
        type: "POST",
        url: "/improveFeatures",
        data: { messege: input },
        success: function(response) {
            if (response == "success") {
                $(".box").append(`<div class="item left d-flex justify-content-start gap-2 align-items-center m-3 col-10">
                                   <div class="icon col-2">
                                       ${chatbot}
                                   </div>
                                   <div class="msg text-start">
                                       <p>Your Feedback is Submitted Successfully !!</p>
                                   </div>
                               </div>`);
                $(".box").animate({ scrollTop: $('.box').prop("scrollHeight") }, 600);
                $("#etext").val("");
                $("#etext").prop('disabled', false);
                feedback = false;
            }
            if (response == "failed") {
                $(".box").append(`<div class="item left d-flex justify-content-start gap-2 align-items-center m-3 col-10">
                                       <div class="icon col-2">
                                           ${chatbot}
                                       </div>
                                       <div class="msg text-start">
                                           <p>Sorry Your Feedback Can not be Submitted Right Now !!</p>
                                       </div>
                                    </div>`);
                $(".box").animate({ scrollTop: $('.box').prop("scrollHeight") }, 600);
                $("#etext").val("");
                $("#etext").prop('disabled', false);
                feedback = false;
            }
        },
        error: function(error) {
            $(".box").append(`<div class="item left d-flex justify-content-start gap-2 align-items-center m-3 col-10">
                               <div class="icon col-2">
                                   ${chatbot}
                               </div>
                               <div class="msg text-start">
                                   <p>Sorry Your Feedback Can't be Submitted Right Now !!</p>
                               </div>
                           </div>`);
            $(".box").animate({ scrollTop: $('.box').prop("scrollHeight") }, 600);
            $("#etext").val("");
            $("#etext").prop('disabled', false);
            feedback = false;
        }
    });
})