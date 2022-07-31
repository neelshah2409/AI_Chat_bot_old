$(document).ready(()=>{

    $("#advanceEnable").on("change",(e)=>{
        if($("#advanceEnable").is(":checked"))
        {
            $("#linkBaseClassInput").prop("disabled",false)
            $("#linkQuestionClassInput").prop("disabled",false)
            $("#linkAnswerClassInput").prop("disabled",false)
        }
        else
        {
            $("#linkBaseClassInput").prop("disabled",true)
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
        let query;
        if($("#advanceEnable").is(":checked"))
        {
            const baseClass =  $("#linkBaseClassInput").val();
            const questionClass =  $("#linkQuestionClassInput").val();
            const answerClass =  $("#linkAnswerClassInput").val();
            query = {link:input,baseClass,questionClass,answerClass};
        }
        else
        {
            query = {link:input};
        }
        console.log(query);
        $(".loadingBox").fadeIn();
        $.ajax({
            type: "POST",
            url: "/linkSubmit",
            data: query,
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