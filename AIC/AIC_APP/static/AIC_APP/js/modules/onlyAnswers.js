$(document).ready(()=>{
    let onlyAnswers = [],currentLength=0,length=0,height=$("#onlyAnswerDisplay").height();

    $("#onlyAnswerInput").on("keyup",(e)=>{
        onlyAnswersInput = $("#onlyAnswerInput").val().split("\n\n");
        const inputLength = onlyAnswersInput = $("#onlyAnswerInput").val().split("\n\n").length;
        if(inputLength==2)
        {
            onlyAnswers.push($("#onlyAnswerInput").val().split("\n\n")[0]);
            console.log(onlyAnswers);
            length=currentLength;
            displayOnlyAnswers();
            $("#onlyAnswerInput").val("");
            length++;
        }
        else if(inputLength>2)
        {
            onlyAnswers = [...onlyAnswers,...$("#onlyAnswerInput").val().split("\n\n")]
            $("#onlyAnswerInput").val("")
            displayOnlyAnswers();
            length++;
        }
        if(length>=1)
        {
            $("#submitBtn").slideDown();
            $(document).scrollTop($(document).height());
        }
        else
        {
            $("#submitBtn").slideUp();
        }   
    })

    $(document).on("focus",".displayOnlyAnswerInput",(e)=>{
        e.target.rows=5;
    })

    $(document).on("blur",".displayOnlyAnswerInput",(e)=>{
        e.target.rows=1;
    })

    $(document).on("change",".displayOnlyAnswerInput",(e)=>{
        const id = e.target.id;
        let value = e.target.value;
        value = value.replaceAll('\n\n','\n');
        if(value=="")
        {
            onlyAnswers.splice(id,1);
        }
        else
        {
            onlyAnswers[id] = value;
        }
        displayOnlyAnswers();
    })


    const displayOnlyAnswers = ()=>{
        $("#onlyAnswerDisplay").empty();
        onlyAnswers.map((value,i)=>{
            displayAnswers(value,i);
            $("#onlyAnswerDisplay").scrollTop(height+$("#onlyAnswerDisplay").height())
            height=$("#onlyAnswerDisplay").height();
        });
    }

    const displayAnswers = (value,i)=>{
        $("#onlyAnswerDisplay").append(`<div class='answersDisplayInput'><span class="fw-bold">Answer : </span><textarea id="${i}" class="displayOnlyAnswerInput" data-bs-toggle="tooltip" title="Click Here To Edit" cols="30" rows="1">${value}</textarea></div>`);
    }

    function urlify(text) {
        var urlRegex = /(https?:\/\/[^\s]+)/g;
        return text.replace(urlRegex, function(url) {
                return '<a href="' + url + '">' + "Click Here For More" + '</a>';
            })
    }

    $(document).on("submit", "#onlyAnswersForm", function(e) {
        e.preventDefault();
        $(".processing").html("Processing").attr("x", "325");
        let input = onlyAnswers.join("\n\n");
        ans = []
        for (let i in input.split("\n\n")) {
            ans.push(urlify(input.split("\n\n")[i].replaceAll('\n', '<br/>')));
        }

        let answersList = {
            "answers": ans
        };
        if (input == "") {
            alert("Please Provide Some Input")
        } else {
            $(".loadingBox").fadeIn();
            $.ajax({
                type: "POST",
                url: "/onlyAnswersData",
                data: { 'inputText': JSON.stringify(answersList) },
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
        }
    })

})