


$(document).ready(function () {
  var temp = "static/AIC_APP/intents6.json";
  let temp1 = "";
  let iterate = 0;
  $.getJSON(temp, function (jd) {
    console.log(jd);
    for (let i in jd) {
      for (let j = 0; j < jd[i].length; j++) {
        temp1 += `<div class="accordion__item accordion__item--active">`;
        for (n in jd[i][j]['patterns']) {
          temp1 += `<button class="accordion__btn">
            <span class="accordion__caption"><i class="far fa-lightbulb"></i>${jd[i][j]['patterns'][n]}</span>
          </button>`;
        }

        temp1 += `<div class="accordion__content">
            <p>${jd[i][j]['responses']}</p>
          </div>
          <span name='${iterate}' id='deleteQuestionSet' style="cursor: pointer;"><button type="button" class="closeall btn mt-2 mb-2 float-right mb-3">Delete</button></span></div>`;
        iterate++;
      }
    }
    $('#questionGenerationdisplay').html(temp1);
  });

  $('#searchBox').on('keyup', function () {
    var ip = $('#searchBox').val();
    var temp = "static/AIC_APP/intents6.json";
    let temp1 = "";
    let iterate = 0;
    $.getJSON(temp, function (jd) {

      for (let i in jd) {
        for (let j = 0; j < jd[i].length; j++) {
          temp1 += `<div class="accordion__item accordion__item--active">`;
          let isMatched = false;
          const match = jd[i][j]['patterns'].filter(key => key.match(new RegExp(ip, "gi")) != null)
          isMatched = match.some(key => key);
          if (isMatched) {
            for (n in jd[i][j]['patterns']) {
              temp1 += `<button class="accordion__btn">
              <span class="accordion__caption"><i class="far fa-lightbulb"></i>${jd[i][j]['patterns'][n]}</span>
            </button>`;
            }

            temp1 += `<div class="accordion__content">
              <p>${jd[i][j]['responses']}</p>
            </div>
            <span name='${iterate}' id='deleteQuestionSet' style="cursor: pointer;"><button type="button" class="closeall btn mt-2 mb-2 float-right mb-3">Delete</button></span></div>`;
            iterate++;
          }
        }
      }
      $('#questionGenerationdisplay').html(temp1);

    });
  });

  $(document).on("click", "#deleteQuestionSet", function () {
    console.log($(this));
    $(this).parent().hide("fold", 700);
    let deleteIndex = $(this).attr("name");
    var temp = "static/AIC_APP/intents6.json";
    setTimeout(function () {
      $.getJSON(temp, function (jd) {
        jd["intents"].splice(deleteIndex, 1);
        let temp1 = "";
        let iterate = 0;
        for (let i in jd) {
          for (let j = 0; j < jd[i].length; j++) {
            temp1 += `<div class="accordion__item accordion__item--active">`;

            for (n in jd[i][j]['patterns']) {
              temp1 += `<button class="accordion__btn">
          <span class="accordion__caption"><i class="far fa-lightbulb"></i>${jd[i][j]['patterns'][n]}</span>
        </button>`;
            }
            temp1 += `<div class="accordion__content">
          <p>${jd[i][j]['responses']}</p>
        </div>
        <span name='${iterate}' id='deleteQuestionSet' style="cursor: pointer;"><button type="button" class="closeall btn mt-2 mb-2 float-right mb-3">Delete</button></span></div>`;
            iterate++;
          }
        }
        $.ajax({
          url: "/updateJson",
          method: "POST",
          data: {
            updateData: JSON.stringify(jd)
          },
          success: function (data) {
            alert("success");
            $('#questionGenerationdisplay').html(temp1);
          },
          error: function (data) {
            alert("Error");
          }
        })

      });
    }, 1000);
  });









  $(document).on("click", "#trainModel", function (e) {
    e.preventDefault();
    $(".processing").html("Training In Progress").attr("x", "260");
    $(".loadingBox").fadeIn();
    $.ajax({
      type: "POST",
      url: "/trainModel",
      success: function (response) {
        if (response == "success") {
          $(".loadingBox").fadeOut();
          window.location.href = "/home";
        }
        if (response == "failed") {
          alert("Training Failed");
          $(".loadingBox").fadeOut();
        }
      },
      error: function (error) {
        alert("Training Failed");
        $(".loadingBox").fadeOut();
      }
    });
  })
});