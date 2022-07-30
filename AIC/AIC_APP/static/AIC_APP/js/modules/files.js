$(document).ready(()=>{
    $("#fileType").on("change",(e)=>{
        if(e.target.value=="none")
        {
            $("#fileInput").prop("disabled",true);
            $("#fileInput").prop("accept",`.${e.target.value}`);
            $("#fileInput").addClass("bg-secondary text-light");
        }
        else
        {
            $("#fileInput").prop("disabled",false);
            $("#fileInput").prop("accept",`.${e.target.value}`);
            $("#fileInput").removeClass("bg-secondary text-light");
        }
    })

    $(document).on("submit", "#fileForm", (e)=>{
        e.preventDefault();
        $(".processing").html("Uploading File").attr("x", "306");
        $(".loadingBox").fadeIn();
        const form = $("#fileForm");
        let formData = new FormData(form[0]);
        console.log(form[0])
        console.log(formData)
        $.ajax({
            type: "POST",
            url: "/fileSubmit",
            data: formData,
            processData:false,
            contentType:false,
            MimeType:"multipart/form-data",
            success:(response)=> {
                $(".loadingBox").fadeOut();
                window.location.href = "QueShow";
            },
            error: (e)=>{
                $(".loadingBox").fadeOut();
                alert("Error")
            }
        });

    })


    $("#fileInput").on("change",(e)=>{
        $("#submitBtn").slideDown();
    })
    
})