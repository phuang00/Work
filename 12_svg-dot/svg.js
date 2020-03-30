// Peihua Huang, Elizabeth Doss (Team thiscodeissick)
// SoftDev2 pd1
// K12 -- Connect the Dots
// 2020-03-30

var pic = document.getElementById("vimage");
var btn = document.getElementById("clear");
var lastX = -1;
var lastY = -1;

var clear = function(e){
  while (pic.lastChild){
    pic.removeChild(pic.lastChild);
  }
  lastX = -1;
  lastY = -1;
};

var draw = function(e){
  var x = e.offsetX;
  var y = e.offsetY;
  console.log(x);
  console.log(y);
  var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
  c.setAttribute("cx", x);
  c.setAttribute("cy", y);
  c.setAttribute("r", "5");
  c.setAttribute("fill", "red");
  c.setAttribute("stroke", "black");
  pic.appendChild(c);
  if (lastX != -1){
    var line = document.createElementNS("http://www.w3.org/2000/svg", "line");
    line.setAttribute("x1", lastX);
    line.setAttribute("y1", lastY);
    line.setAttribute("x2", x);
    line.setAttribute("y2", y);
    line.setAttribute("stroke", "black");
    pic.appendChild(line);
  }
  lastX = x;
  lastY = y;
};

btn.addEventListener('click', clear);

pic.addEventListener('click', draw);
