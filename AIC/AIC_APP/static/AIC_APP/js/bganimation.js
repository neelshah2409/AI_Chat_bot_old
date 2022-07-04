$(document).ready(function() {
    // gsap.from("#Green_1_", { duration: 3, y: -200, rotation: 360, ease: "bounce" });
    gsap.from("#polygon polygon", { duration: 1, opacity: 0, y: -200, stagger: 0.2 });
    gsap.timeline().from("#chatbox div", { duration: 0.7, delay: 1.5, opacity: 0, scale: 0, stagger: 0.2, y: -400, ease: "ease.in" });

    gsap.timeline().from("#Green_2_", { duration: 1, rotation: 180, y: -200, scale: 0, ease: "ease.in" })
        .from("path", { scaleX: 0, duration: 0.7, ease: "power2" })
        .from("ellipse", { scaleX: 0, duration: 0.5, ease: "power2" })
        .from("circle", { scaleX: 0, duration: 0.5, ease: "power2" })
        .from("#Lineset1_2_ .st0", { scaleX: 0, duration: 0.7, stagger: 0.1, repeat: -1, yoyo: 0.2 })
        .from("#Lineset2_2_ .st0", { scaleX: 0, duration: 0.7, stagger: 0.1, repeat: -1, yoyo: 0.2 })
        .from("#Lineset3_2_ .st0", { scaleX: 0, duration: 0.7, stagger: 0.1, repeat: -1, yoyo: 0.2 });

    gsap.from("#purple_2_", { duration: 2, delay: 1, rotation: 180, x: -200, scale: 0, rotation: 180, ease: "back" });

    gsap.timeline().from("#Gray_2_", { duration: 2, yPercent: 400, xPercent: -200, rotation: 180, opacity: 0, ease: "ease.in" })
    gsap.from("#red_2_", { duration: 1, rotation: -180, opacity: 0, scale: 0.2, delay: 0.5 });
    gsap.from("#blue2_2_", { duration: 1, rotation: -360, opacity: 0, scale: 0.2, delay: 0.5, ease: "stop" });
    gsap.from("#bluemain_2_", { duration: 1.5, delay: 0.7, rotation: 360, scale: 0, opacity: 0, ease: "power4" });
    gsap.timeline().from("#yellow_2_", { duration: 1.5, delay: 1.5, rotation: -360, scale: 2, opacity: 0, ease: "power4" });
});