let angleNormal = 0;
let angleSuper = 0;

function animateMe() {
    angleNormal += 2;
    angleSuper += 5;

    document.getElementById('normalYou').style.transform = "rotate(" + angleNormal + "deg)";
    document.getElementById('superYou').style.transform = "scale(1.1) rotate(" + angleSuper + "deg)";
}

setInterval(animateMe, 50);
// Add your JavaScript here.
