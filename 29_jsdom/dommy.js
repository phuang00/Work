var changeHeading = function(e) {
  var h = document.getElementById("h");
  h.innerHTML = ;//the list item stuff
};

var removeItem = function(e) {
  //element.remove() stuff
};

var list = document.getElementsByTagName("li");

for (var i = 0; i < lis.length; i++) {
  lis[i].addEventListener('mouseover', ???); //call changeHeading
  list[i].addEventListener('mouseout', ???); // call changeHeading back to helloworld
  lis[i].addEventListener('click', ???); //remove list item
}

var addItem = function(e) {
  var list = ; //getElementById? list
  var item = document.createElement("li");
  ??? = "WORD"; //item.innerHTML?
  //maybe more stuff
  list.???(item); //appendChild
};

var button = document.getElementById("b");
button.addEventListener('click', addItem);

var fib = function(n) {
  if (n < 2) {
    return 1;
  }
  else {
    return fib(n - 1) + fib(n - 2);
  }
};

var addFib = function(e) {
  console.log(e);
  ??? // create list
};

var addFib2 = function(e) {
  console.log(e);
  // dynamic programming, add to list
};

var fb = document.getElementById("fb");
fb.addEventListener('click', addFib);
