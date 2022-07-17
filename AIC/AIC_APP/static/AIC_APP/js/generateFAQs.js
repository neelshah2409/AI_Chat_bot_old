// $(document).ready(()=>{
//     $(".description-carousel").owlCarousel({
//         margin:0,
//         items:1,
//         center:true,
//         autoplay:true,
//         loop:true,
//         // animateIn:"animate__flipInX",
//         animateOut:"animate__lightSpeedOutLeft",
//         // stagePadding:0,
//         smartSpeed:2000,
//         dots:false
//     });

//     $(".card-carousel").owlCarousel({
//         margin:0,
//         items:5,
        
//         autoplay:true,
//         animateIn:"animate__slideInRight",
//         animateOut:"animate__slideOutLeft",
//         stagePadding:50,
//         center:true,
//         loop:true,
//         smartSpeed:450,
//         responsive:{
//             0:{
//                 items:1,
//                 stagePadding:0,
//                 margin:20
//             },
//             321:{
//                 items:1,
//                 stagePadding:0,
//                 autowidth:true,
//                 margin:0
//             },
//             415:{
//                 items:1,
//                 stagePadding:0,
//                 margin:10
//             },
//             500:{
//                 items:2,
//                 stagePadding:0,
//                 autowidth:true,
//             },
//             600:{
//                 items:2,
//                 stagePadding:0,
//                 margin:0
//                 // loop:true,
//                 // center:true
//             },
//             800:{
//                 items:3,
//                 loop:true,
//                 margin:1,
//                 center:true,
//                 stagePadding:-20
//             },
//             1200:{
//                 items:4,
//                 loop:true,
//                 margin:10,
//                 center:true,
//                 stagePadding:0
//             }
//         }
//     });
    
// })


$(document).ready(function () {
    $('.description-carousel').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        fade: true,
        asNavFor: '.card-carousel',
        
      });
      $('.card-carousel').slick({
        slidesToShow: 3,
        slidesToScroll: 1,
        asNavFor: '.description-carousel',
        dots: true,
        arrows: false,
        centerMode: true,
        focusOnSelect: true,
      });
                      
});