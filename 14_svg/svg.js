// Peihua Huang, Tiffany Cao (Team ???)
// SoftDev2 pd1
// K13 -- Ask Circles [Change || Die] While Moving etc.
// 2020-03-31

var pic = document.getElementById("vimage");
var btn_clear = document.getElementById("clear");
var btn_move = document.getElementById("move");
var btn_xtra = document.getElementById("xtra");
var id = 0;
var inc_x = 1;
var inc_y = 1;


var clear = function(e){
  while (pic.lastChild){
    pic.removeChild(pic.lastChild);
  }
  window.cancelAnimationFrame(id);
  id = 0;
};

var draw = function(e){
  if (e.target == pic){
    var x = e.offsetX;
    var y = e.offsetY;
    var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    c.setAttribute("cx", x);
    c.setAttribute("cy", y);
    c.setAttribute("r", "15");
    c.setAttribute("fill", "blue");
    c.addEventListener('click', change);
    pic.appendChild(c);
  }
};

var change = function(e){
  //console.log(e);
  if (e.target.getAttribute("fill") == "blue"){
    e.target.setAttribute("fill", "cyan");
  }
  else{
    var x = Math.floor(Math.random() * pic.getAttribute("width"));
    var y = Math.floor(Math.random() * pic.getAttribute("height"));
    e.target.setAttribute("cx", x);
    e.target.setAttribute("cy", y);
    e.target.setAttribute("fill", "blue");
  }
};

var move = function(e){
  var d = document.getElementsByTagNameNS("http://www.w3.org/2000/svg", "circle");
  for (var i = 0; i < d.length; i++){
    console.log(d[i]);
    var dot = d[i];
    var x = parseInt(dot.getAttribute("cx"));
    var y = parseInt(dot.getAttribute("cy"));
    if (x > pic.getAttribute("width") - 15){
      inc_x = -1;
    }
    else if (x < 0){
      inc_x = 1;
    }
    if (y > pic.getAttribute("height") - 15){
      inc_y = -1;
    }
    else if (y < 0){
      inc_y = 1;
    }
    x += inc_x;
    y += inc_y;
    dot.setAttribute("cx", x);
    dot.setAttribute("cy", y);
    // if (d != 0) {
    //   id = window.requestAnimationFrame(float);
    // }
  }
  if (id != 0) {
    id = window.requestAnimationFrame(move);
  }
};

btn_clear.addEventListener('click', clear);

btn_move.addEventListener('click', function(e){
    window.cancelAnimationFrame(id);
    id = window.requestAnimationFrame(move);
  }
);

pic.addEventListener('click', draw);