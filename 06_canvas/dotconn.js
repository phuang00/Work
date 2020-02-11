// Peihua Huang (Team superduperguacamole)
// SoftDev1 pd1
// K06 -- Dot Dot Dot
// 2020-02-11

let lastX = -1;
let lastY = -1;

var c = document.getElementById("playground");
var ctx = c.getContext("2d");
//ctx.fillStyle="#ff0000";
//ctx.fillRect(50, 50, 100, 200);

var clear = function(e){
  console.log(e);
  ctx.clearRect(0, 0, c.width, c.height);
  lastX = -1;
  lastY = -1;
}

var draw = function(e){
  // e.offsetX offsets the mouseX by the x-coordinate of the event
  // give the mouse cursor location relative to the target(canvas)
  var x = e.offsetX;
  // same as e.offsetX but for the y-coordinate
  var y = e.offsetY;
  //ctx.beginPath() begins drawing a line/curve
  ctx.beginPath();
  ctx.arc(x, y, 3, 0, 2 * Math.PI);
  if (lastX != -1){
    ctx.moveTo(x, y);
    ctx.lineTo(lastX, lastY);
  }
  ctx.stroke();
  ctx.fill();
  lastX = x;
  lastY = y;
}

var cle = document.getElementById("clear");
cle.addEventListener('click', clear);

c.addEventListener('click', draw);

// e.preventDefault();
// we didn't use it but if we did, it resorts to the default action if the event is not handled
// this would be used if we added event listener to the whole doc and we only want to paint within the canvas
