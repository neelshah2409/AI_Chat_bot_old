 //faqs
  // select all accordion items
  const accItems = document.querySelectorAll(".accordion__item");

  // add a click event for all items
  accItems.forEach((acc) => acc.addEventListener("click", toggleAcc));
  
  document.getElementById('openall').addEventListener("click", toggleAcc2);
  
  function toggleAcc() {
    // remove active class from all items exept the current item (this)
    accItems.forEach((item) => item != this ? item.classList.remove("accordion__item--active") : null
    );
  
    // toggle active class on current item
    if (this.classList != "accordion__item--active") {
      this.classList.toggle("accordion__item--active");
    }
  
  }
  function toggleAcc2() {
    if (this.innerText=="Close") this.innerText = "Open";
      else this.innerText = "Close";
    accItems.forEach((acc) => acc.classList.toggle("accordion__item--active"));
  
  // accItems.forEach((acc) => acc.classList.remove("accordion__item--active"));
  
  }

$(document).ready(function () {
    $(document).on("click", "#trainModel", function(e) {
      e.preventDefault();
      $(".processing").html("Training In Progress").attr("x", "260");
      $(".loadingBox").fadeIn();
      $.ajax({
          type: "POST",
          url: "/trainModel",
          success: function(response) {
              if (response == "success") {
                  $(".loadingBox").fadeOut();
                  window.location.href = "/home";
              }
              if (response == "failed") {
                  alert("Training Failed");
                  $(".loadingBox").fadeOut();
              }
          },
          error: function(error) {
              alert("Training Failed");
              $(".loadingBox").fadeOut();
          }
      });
    })   
});