$(document).ready(function() {
    // gsap.from("#Green_1_", { duration: 3, y: -200, rotation: 360, ease: "bounce" });
    gsap.from("#Green_1_", { duration: 1, rotation: 180, y: -200, scale: 0, ease: "ease.in" });
    gsap.from("#purple_1_", { duration: 2, delay: 1, rotation: 180, x: -200, scale: 0, rotation: 180, ease: "back" });

    gsap.timeline().from("#Gray_1_", { duration: 2, yPercent: 400, xPercent: -200, rotation: 180, opacity: 0, ease: "ease.in" })
    gsap.from("#red_1_", { duration: 1, rotation: -180, opacity: 0, scale: 0.2, delay: 0.5 });
    gsap.from("#blue2_1_", { duration: 1, rotation: -360, opacity: 0, scale: 0.2, delay: 0.5, ease: "stop" });
    gsap.timeline().from("#bluemain_1_", { duration: 1.5, delay: 0.7, rotation: 360, scale: 0, opacity: 0, ease: "power4" });
    gsap.timeline().from("#yellow_1_", { duration: 1.5, delay: 1.5, rotation: -360, scale: 2, opacity: 0, ease: "power4" });

});