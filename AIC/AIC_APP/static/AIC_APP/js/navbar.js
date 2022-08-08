$(document).ready(function () {

    $("#userProfile").on("click",(e)=>{
        $.ajax({
            type:"GET",
            url:"/getUserData",
            success:(result)=>{
                $(".profile #email").val(result.data.Email)
                $(".profile #mobile").val(result.data.PhoneNum)
                $(".profile #name").val(result.data.Name)
                $(".profile #organization").val(result.data.CompanyName)
                $(".profile #welcomeMessage").val(result.data.greetmsg);
                $(".profile #sorryMessage").val(result.data.errmsg);
            },
            error:()=>{
                alert("Error");
            }
        })
    })

    $("#profileForm").on("submit",(e)=>{
        e.preventDefault();
        const email = $(".profile #email").val();
        const mobile = $(".profile #mobile").val();
        const name = $(".profile #name").val();
        const organization = $(".profile #organization").val()
        const welcome = $("#welcomeMessage").val();
        const sorry = $("#sorryMessage").val();
        $.ajax({
            type:"POST",
            url:"/updateUserData",
            data:JSON.stringify({name,email,mobile,organization,welcome,sorry}),
            success:(result)=>{
                $("#profileMessage").html("Changes Saved")
                $("#profileMessage").addClass("text-success")
                $(".profile #email").val(result.data.Email)
                $(".profile #mobile").val(result.data.PhoneNum)
                $(".profile #name").val(result.data.Name)
                $(".profile #organization").val(result.data.CompanyName)
                $(".profile #welcomeMessage").val(result.data.greetmsg);
                $(".profile #sorryMessage").val(result.data.errormsg);
            },
            error:()=>{
                alert("Error");
            }
        })
    })

    
});