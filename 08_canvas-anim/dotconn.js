// Peihua Huang and Jackie Lin (Team Pencils)
// SoftDev1 pd1
// K07 -- Canvas Anim
// 2020-02-12

var c = document.getElementById("playground");
var ctx = c.getContext("2d");

var radius = 0;
var increment = 1;
var id = 0;
var x = -1;
var y = -1;
var inc_x = 1;
var inc_y = 1;

var logo = new Image();
logo.src = "logo_dvd.jpg";

var start = function(e){
  window.cancelAnimationFrame(id)
  id = window.requestAnimationFrame(animate);
}

var stop = function(e){
  window.cancelAnimationFrame(id);
  id = 0;
}

var dvd = function(e){
  window.cancelAnimationFrame(id);
  id = 0;
  inc_x = 1;
  inc_y = 1;
  x = Math.floor(Math.random() * (c.width - 75));
  y = Math.floor(Math.random() * (c.height - 75/2));
  id = window.requestAnimationFrame(float);
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

var float = function(e){
  ctx.clearRect(0, 0, c.width, c.height);
  if (x > c.width - 75){
    inc_x = -1;
  }
  else if (x < 0){
    inc_x = 1;
  }
  if (y > c.height - 75/2){
    inc_y = -1;
  }
  else if (y < 0){
    inc_y = 1;
  }
  ctx.drawImage(logo, x, y, 75, 75/2);
  x += inc_x;
  y += inc_y;
  if (id != 0) {
    id = window.requestAnimationFrame(float);
  }
}

var startbtn = document.getElementById("start");
var stopbtn = document.getElementById("stop");
var dvdbtn = document.getElementById("dvd");
startbtn.addEventListener("click", start);
stopbtn.addEventListener("click", stop);
dvdbtn.addEventListener('click', dvd);
