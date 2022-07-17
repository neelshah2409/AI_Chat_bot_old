$(document).ready(()=>{
        $("#paragraphInput").on("keyup",(e)=>{
            if(e.target.value.length>=1)
            {
                $("#submitBtn").slideDown();
                $(document).scrollTop($(document).height());
            }
            else
            {
                $("#submitBtn").slideUp();
            }   
        })

        $(document).on("submit", "#paragraphForm", function(e) {
        e.preventDefault();
        $(".processing").html("Processing").attr("x", "325");
        let input = $("#paragraphInput").val();
        console.log($("#paragraphInput"));
        if (input == "") {
            alert("Please Provide Some Input")
        } else {
            $(".loadingBox").fadeIn();
            $.ajax({
                type: "POST",
                url: "/fetchInputTextArea",
                data: { inputText: input },
                success: function(response) {
                    if (response == "success") {
                        $(".loadingBox").fadeOut();
                        window.location.href = "QueShow";
                    }
                    if (response == "failed") {
                        alert("Failed");
                        $(".loadingBox").fadeOut();
                        window.location.href = "QueShow";
                    }
                },
                error: function(error) {
                    alert("Process Failed");
                    $(".loadingBox").fadeOut();
                }
            });
        }
    })
        
})