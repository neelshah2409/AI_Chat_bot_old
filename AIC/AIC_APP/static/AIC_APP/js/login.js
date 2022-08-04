const toggleSignUp = document.getElementById("signUp");
const toggleSignIn = document.getElementById("signIn");
const overlay = document.getElementById("overlay");
const authentication_box = document.getElementById("auth_box");
toggleSignUp.onclick = ()=>{
        overlay.classList.remove('overlay-right-active');
        overlay.classList.add('overlay-left-active');
        authentication_box.classList.add("right-active");
        authentication_box.classList.remove("left-active");
    };

toggleSignIn.onclick = ()=>{
    overlay.classList.remove('overlay-left-active');
    overlay.classList.add('overlay-right-active');
    authentication_box.classList.add("left-active");
    authentication_box.classList.remove("right-active");
};
const params = new URLSearchParams(window.location.search)
if(params.has('signup'))
{
    toggleSignUp.click();
}