// Peihua Huang and Jackie Lin (Team Pencils)
// SoftDev1 pd1
// K07 -- Canvas Anim
// 2020-02-12

var c = document.getElementById("playground");
var ctx = c.getContext("2d");

let radius = 0;
let increment = 1;
let id = 0;

var start = function(e){
  if (id == 0){
    id = window.requestAnimationFrame(animate);
  }
}

var stop = function(e){
  window.cancelAnimationFrame(id);
  id = 0;
}

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
  ctx.fillStyle = 'blue';
  ctx.fill();
  ctx.closePath();
  radius += increment;
  if (id != 0) {
    id = window.requestAnimationFrame(animate);
  }
}

var startbtn = document.getElementById("start");
var stopbtn = document.getElementById("stop");
startbtn.addEventListener("click", start);
stopbtn.addEventListener("click", stop);
