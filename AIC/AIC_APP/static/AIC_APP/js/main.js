function change(x) {

  x.childNodes[1].style.display = "none";
  x.childNodes[3].style.display = "block";
}

function chnageAgain(x) {

  x.childNodes[1].style.display = "block";
  x.childNodes[3].style.display = "none";

}

// benefits 
$(document).ready(function(){
  $('.carousel').slick({
    speed: 500,
    slidesToShow: 3,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 2000,
    dots:true,
    centerMode: true,
    responsive: [{
      breakpoint: 1024,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 1,
        // centerMode: true,

      }

    }, {
      breakpoint: 1000,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 2,
        dots: true,
        infinite: true,

      }
    },  {
      breakpoint: 770,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1,
        dots: true,
        infinite: true,
        autoplay: true,
        autoplaySpeed: 2000,
      }
    }]
  });
});



//   steps 

class StepsComponent {
  constructor(stepsSelector, contentsSelector) {
    this.current = 1;
    this.stepsNode = document.querySelector(stepsSelector);
    this.contentsNode = document.querySelector(contentsSelector);

    this.totalSteps = this.stepsNode.children.length;

    this.stepsNode.querySelectorAll("button").forEach((step) => {
      step.addEventListener("click", (e) => {
        const targetStep = parseInt(e.target.dataset.step);

        this.contentsNode
          .querySelectorAll(".content")
          .forEach((content) => content.classList.remove("active"));
        this.stepsNode
          .querySelectorAll("button")
          .forEach((content) => content.classList.remove("active"));

        this.contentsNode
          .querySelector(`.content[data-step="${targetStep}"]`)
          .classList.add("active");
        this.stepsNode
          .querySelector(`button[data-step="${targetStep}"]`)
          .classList.add("active");

        this.stepsNode
          .querySelectorAll("div")
          .forEach((content) => content.classList.remove("active"));
        if (targetStep - 1 > 0) {
          const num = targetStep - 1;
          for (let i = 1; i <= num; i++) {
            this.stepsNode
              .querySelector(`div:nth-of-type(${i})`)
              .classList.add("active");
          }
        }
      });
    });
  }
}

new StepsComponent("#steps", "#contents");


//faqs
// select all accordion items
const accItems = document.querySelectorAll(".accordion__item");

// add a click event for all items
accItems.forEach((acc) => acc.addEventListener("click", toggleAcc));

function toggleAcc() {
// remove active class from all items exept the current item (this)
accItems.forEach((item) => item != this ? item.classList.remove("accordion__item--active") : null
);

// toggle active class on current item
if (this.classList != "accordion__item--active") {
  this.classList.toggle("accordion__item--active");
}
}






