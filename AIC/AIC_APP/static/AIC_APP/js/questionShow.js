


$(document).ready(function () {
  var obj = {};
  var nary=[];

// obj[name] = val;

// ary.push(obj);
  var temp = `static/AIC_APP/intents${id}.json`;
  let temp1 = "";
  var temp2d="";
var qcount=0;
  let iterate = 0;
  $.getJSON(temp, function (jd) {
    // console.log(jd);
    for (let i in jd) {
      // console.log(jd[i]);
     
      for (let j = 0; j < jd[i].length; j++) {
      let temp5=[];
      var qc=0
        temp1 += `<div class="accordion__item accordion__item--active">`;
        for (n in jd[i][j]['patterns']) {
          temp1 += `<button class="accordion__btn">
            <span class="accordion__caption"><i class="far fa-lightbulb"></i>${jd[i][j]['patterns'][n]}</span>
          </button>`;
          temp2d+=`Question${qcount} : ${jd[i][j]['patterns'][n]}\n`;
          temp5.push(jd[i][j]['patterns'][n]);
          qc++;
        }

        temp1 += `<div class="accordion__content">
            <p>${jd[i][j]['responses']}</p>
          </div>
          <span name='${iterate}' id='deleteQuestionSet' style="cursor: pointer;"><button type="button" class="closeall btn mt-2 mb-2 float-right mb-3">Delete</button></span></div>`;
        iterate++;
        temp2d+=`Answer : ${jd[i][j]['responses']}\n\n`;
        temp4=jd[i][j]['responses'];
        // obj[temp3] = temp4;
        nary.push( {"que":[...temp5],"ans": temp4} );
        qcount++;
        
        

      }
    }
    console.log(nary);
    $('#questionGenerationdisplay').html(temp1);
    $('#temp2d').html(temp2d);
  });


      document.getElementById('textfile').onclick = function(code) 
		{
      var txt = document.getElementById('temp2d');

      this.href = 'data:text/plain;charset=utf-11,' + encodeURIComponent(txt.innerHTML);
        };


        function createCSV(array){
          // var keys = Object.keys(array[0]); //Collects Table Headers
          
          var result = "sep=$\n"; //CSV Contents
          //  result += keys.join(','); //Comma Seperates Headers
          //  result += '\n'; //New Row
          
          array.forEach(
            // function(item){ //Goes Through Each Array Object
            // // keys.forEach(function(key){//Goes Through Each Object value
            // console.log(JSON.stringify(item));
            //   result += JSON.stringify(item) + ','; //Comma Seperates Each Key Value in a Row
            // // })
            // result += '\n';//Creates New Row

          // }


          (i)=>{
            let que = "",ans=""
            for(j in i["que"]){
                que += `${Number(j)+1}.${i["que"][j]}  `;
            }
            que+="$"+i["ans"]+"\n";
            result+=que;
            console.log(result);
          }
          )

          
          return result;
        }
      document.getElementById('csvfile').onclick = function(code) 
		{
      csv = 'data:text/csv;charset=utf-8,' + createCSV(nary); //Creates CSV File Format
      excel = encodeURI(csv); //Links to CSV 
      this.href=excel;
        }

  $('#searchBox').on('keyup', function () {
    var ip = $('#searchBox').val();
    var temp = `static/AIC_APP/intents/intents${id}.json`;
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
    var temp = `static/AIC_APP/intents/intents${id}.json`;
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
          success: function (data) {;
            $('#questionGenerationdisplay').html(temp1);
          },
          error: function (data) {
            alert("Error");
          }
        })

      });
    }, 1000);
  });









  $(document).on("click", "#trainmodelbutton", function (e) {
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






  $(document).on("click",'#resetbutton',function(e){
      e.preventDefault();
      $.ajax({
        type:"PUT",
        url:"/resetAll",
        success:()=>{
          window.location.href="/QueShow";
        },
        error:()=>{
          alert("Error");
        }
      })
  })
});