var state = "box";

var c = document.getElementById("slate");
var ctx = c.getContext("2d");
//ctx.fillStyle="#ff0000";
//ctx.fillRect(50, 50, 100, 200);

var clear = function(e){
  console.log(e);
  ctx.clearRect(0, 0, c.width, c.height);
}

var toggle = function(e){
  var mode = document.getElementById("mode");
  if (state == "box"){
    state = "dot";
    mode.innerHTML = "dot";
  }
  else {
    state = "box";
    mode.innerHTML = "box";
  }
  console.log(state);
}

var draw = function(e){
  var x = e.pageX - c.offsetLeft;
  var y = e.pageY - c.offsetTop;
  if (state == "box"){
    ctx.fillRect(x, y, 28, 28);
  }
}

var cle = document.getElementById("cle");
cle.addEventListener('click', clear);

var tog = document.getElementById("tog");
tog.addEventListener('click', toggle);

c.addEventListener('click', draw);
