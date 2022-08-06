$(document).ready(()=>{

    $("#advanceEnable").on("change",(e)=>{
        if($("#advanceEnable").is(":checked"))
        {
            $("#linkBaseClassInput").prop("disabled",false)
            $("#linkQuestionClassInput").prop("disabled",false)
            $("#linkAnswerClassInput").prop("disabled",false)
            $("#question").prop("disabled",false)
            $("#answer").prop("disabled",false)
            $("#base").prop("disabled",false)
        }
        else
        {
            $("#linkBaseClassInput").prop("disabled",true)
            $("#linkQuestionClassInput").prop("disabled",true)
            $("#linkAnswerClassInput").prop("disabled",true)
            $("#question").prop("disabled",true)
            $("#answer").prop("disabled",true)
            $("#base").prop("disabled",true)
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

    const convertEquiv = (value)=>{
        if(value=="tag"){
            return "";
        }
        else if(value=="class"){
            return ".";
        }
        else if(value=="id"){
            return "#"
        }
        else{
            alert("Error ! Please Enter Valid Input");
            window.location.href="/linkinput";
        }
    }

    $(document).on("submit", "#linkForm", function(e) {
        e.preventDefault();
        console.log()
        $(".processing").html("Processing").attr("x", "325");
        const input = $("#linkInput").val();
        let query;
        if($("#advanceEnable").is(":checked"))
        {
            const baseClass =  convertEquiv($("#base").val())+$("#linkBaseClassInput").val();
            const questionClass =  convertEquiv($("#question").val())+$("#linkQuestionClassInput").val();
            const answerClass =  convertEquiv($("#answer").val())+$("#linkAnswerClassInput").val();
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