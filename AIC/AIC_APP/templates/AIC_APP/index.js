var etext = document.getElementById("etext");
etext.addEventListener("keyup", function(e) {
    e.preventDefault();
    var sug = document.getElementById("sug");

    sug.style.visibility = "visible";
    if (document.getElementById("etext").value == "") {
        sug.style.visibility = "hidden";
    }
})