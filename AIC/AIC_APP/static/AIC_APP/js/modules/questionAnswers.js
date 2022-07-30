$(document).ready(()=>{
        let questionAnswers = [],currentLength=0,length=0,height=$("#questionAnswerDisplay").height();


        $("#questionAnswerInput").on("keyup",(e)=>{
            questionAnswersInput = $("#questionAnswerInput").val().split("\n\n");
            const inputLength = questionAnswersInput = $("#questionAnswerInput").val().split("\n\n").length;
            if(inputLength==2)
            {
                questionAnswers.push($("#questionAnswerInput").val().split("\n\n")[0]);
                if($("#questionAnswerInput").val().split("\n\n")[1].length>0)
                {
                    questionAnswers.push($("#questionAnswerInput").val().split("\n\n")[1]);
                }
                console.log(questionAnswers);
                length=currentLength;
                displayQuestionAnswers();
                $("#questionAnswerInput").val("");
                length++;
            }
            else if(inputLength>2)
            {
                questionAnswers = [...questionAnswers,...$("#questionAnswerInput").val().split("\n\n")]
                $("#questionAnswerInput").val("")
                displayQuestionAnswers();
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

        $(document).on("focus",".displayQuestionAnswerInput",(e)=>{
            e.target.rows=5;
        })
    
        $(document).on("blur",".displayQuestionAnswerInput",(e)=>{
            e.target.rows=1;
        })

        $(document).on("change",".displayQuestionAnswerInput",(e)=>{
            const id = e.target.id;
            let value = e.target.value;
            value = value.replaceAll(/\n{2,100000}/g,'\n');
            if(value=="")
            {
                if(id%2==0)
                {
                    questionAnswers.splice(id,2);
                }
                else
                {
                    questionAnswers.splice(id-1,2);
                }
            }
            else
            {
                questionAnswers[id] = value;
            }
            displayQuestionAnswers();
        })

        const displayQuestionAnswers = ()=>{
            $("#questionAnswerDisplay").empty();
            questionAnswers.map((value,i)=>{
                i%2==0?displayQuestion(value,i):displayAnswers(value,i)
                $("#questionAnswerDisplay").scrollTop(height+$("#questionAnswerDisplay").height())
                height=$("#questionAnswerDisplay").height();
            });
        }

        const displayQuestion = (value,i)=>{
            $("#questionAnswerDisplay").append(`<div class='questionAnswersDisplayInput'><span class="fw-bold">Question: </span><textarea id="${i}" class="displayQuestionAnswerInput" data-bs-toggle="tooltip" title="Click Here To Edit" cols="50" rows="1">${value}</textarea></div>`);
            $("#questionAnswerInputLabel").html("Type Your Answer Here :")
        }

        const displayAnswers = (value,i)=>{
            $("#questionAnswerDisplay").append(`<div class='questionAnswersDisplayInput'><span class="fw-bold">Answer: </span><textarea id="${i}" class="displayQuestionAnswerInput" data-bs-toggle="tooltip" title="Click Here To Edit" cols="50" rows="1">${value}</textarea></div>`);
            $("#questionAnswerInputLabel").html("Type Your Question Here :")
        }

        function urlify(text) {
            var urlRegex = /(https?:\/\/[^\s]+)/g;
            return text.replace(urlRegex, function(url) {
                    return '<a href="' + url + '">' + "Click Here For More" + '</a>';
                })
        }
    
        $(document).on("submit", "#questionAnswersForm", function(e) {
            e.preventDefault();
            if(questionAnswers.length%2!=0)
            {
                alert("Question Answers are not in proper format")
            }
            $(".processing").html("Processing").attr("x", "325");
            questions = []
            answers = []
            for(i in questionAnswers)
            {
                if(i%2==0)
                {
                    questions.push(questionAnswers[i]);
                }
                else
                {
                    answer = urlify(questionAnswers[i].replaceAll('\n', '<br/>'))
                    answers.push(answer);
                }
            }
            let questionAnswersList = { "questions": questions, "answers": answers };
            console.log(questionAnswersList);
            if (questionAnswers.length == 0) {
                alert("Please Provide Some Input")
            } else {
                $(".loadingBox").fadeIn();
                $.ajax({
                    type: "POST",
                    url: "/questionAnswerData",
                    data: { 'inputText': JSON.stringify(questionAnswersList) },
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