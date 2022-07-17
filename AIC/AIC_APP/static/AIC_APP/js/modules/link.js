$(document).ready(()=>{

    $("#advanceEnable").on("change",(e)=>{
        if($("#advanceEnable").is(":checked"))
        {
            $("#linkQuestionClassInput").prop("disabled",false)
            $("#linkAnswerClassInput").prop("disabled",false)
        }
        else
        {
            $("#linkQuestionClassInput").prop("disabled",true)
            $("#linkAnswerClassInput").prop("disabled",true)
        }
    });

    $("#linkInput").on("keyup",(e)=>{
        if(e.target.value!="")
        {
            $("#submitBtn").slideDown();
        }
        else
        {
            $("#submitBtn").slideUp();
        }
    })

    $(document).on("submit", "#linkForm", function(e) {
        e.preventDefault();
        console.log()
        $(".processing").html("Processing").attr("x", "325");
        const input = $("#linkInput").val();
        const questionClass =  $("#linkQuestionClassInput").val();
        const answerClass =  $("#linkAnswerClassInput").val();
        $(".loadingBox").fadeIn();
        $.ajax({
            type: "POST",
            url: "/linkSubmit",
            data: { link: input, questionClass,answerClass },
            success: function(response) {
                if (response == "success") {
                    $(".loadingBox").fadeOut();
                    window.location.href = "QueShow";
                }
                if (response == "failed") {
                    alert("Failed");
                    $(".loadingBox").fadeOut();
                }
            },
            error: function(error) {
                alert("Process Failed");
                $(".loadingBox").fadeOut();
            }
        });
    })


})