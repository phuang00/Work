var state = "box";

var c = document.getElementById("slate");
var ctx = c.getContext("2d");
ctx.fillStyle="#ff0000";
ctx.fillRect(50, 50, 100, 200);

var clear = function(e){
  console.log(e);
  ctx.clearRect(0, 0, c.width, c.height);
}

var toggle = function(e){
  if (state == "box"){
    state = "dot";
  }
  else {
    state = "box";
  }
  console.log(state);
}

var draw = function(e){
  
}

var cle = document.getElementById("cle");
cle.addEventListener('click', clear);

var tog = document.getElementById("tog");
tog.addEventListener('click', toggle);

ctx.addEventListener('click', draw);
