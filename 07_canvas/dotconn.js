// Peihua Huang (Team Pencils)
// SoftDev1 pd1
// K07 --
// 2020-02-12
//
// let mode = 0;
let radius = 0;
let increment = 1;

var c = document.getElementById("playground");
var ctx = c.getContext("2d");


//
// var sta = function(e){
//   mode = 1;
// }
//
// var end = function(e){
//   mode = 0;
// }

var animate = function(e){
  if (radius < 0){
    increment = -increment;
    radius = 0;
  }
  else if (radius > c.width/2) {
    increment = -increment;
  }
  ctx.clearRect(0, 0, c.width, c.height);
  console.log(radius);
  ctx.beginPath();
  ctx.arc(c.width/2, c.height/2, radius, 0, 2 * Math.PI);
  ctx.stroke();
  ctx.fill();
  radius += increment;
  window.requestAnimationFrame(animate);
}

// var start = document.getElementById("start");
// var stop = document.getElementById("stop");
// start.addEventListener('click', sta);
// stop.addEventListener('click', end);

window.requestAnimationFrame(animate);
