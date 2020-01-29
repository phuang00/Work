// Hannah Fried, Peihua Huang
// SoftDev1 pd2
// K29 -- Sequential Progression III
// 2019-12-12

var changeHeading = function(e) {
  var h = document.getElementById("h");
  if (e.type == 'mouseout'){ // if the event is mouseout
    h.innerHTML = "Hello World!"; //set the text inside heading back to 'Hello World!'
  }
  else{
    h.innerHTML = e.target.innerHTML; //replace text inside heading with the text of the item calling it
  };
};

var removeItem = function(e) {
  e.target.remove(); // remove the list item element that the event is being called by
};

var lis = document.getElementsByTagName("li");

for (var i = 0; i < lis.length; i++) {
  lis[i].addEventListener('mouseover', changeHeading); //call changeHeading
  lis[i].addEventListener('mouseout', changeHeading); // call changeHeading back to helloworld
  lis[i].addEventListener('click', removeItem); //remove list item
}

var addItem = function(e) {
  var list = document.getElementById("thelist"); //getElementById list
  var item = document.createElement("li");
  item.innerHTML = "WORD"; //item.innerHTML?
  //maybe more stuff
  item.addEventListener('mouseover', changeHeading); //call changeHeading
  item.addEventListener('mouseout', changeHeading); // call changeHeading back to helloworld
  item.addEventListener('click', removeItem); //remove list item
  list.appendChild(item); //appendChild
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

var fib_list = [];

var addFib = function(e) {
  //console.log(e);
  var list = document.getElementById("fiblist");
  var item = document.createElement("li");
  var n = list.getElementsByTagName("li").length;
  item.innerHTML = fib(n);
  list.appendChild(item);
};

var addFib2 = function(e) {
  //console.log(e);
  var list = document.getElementById("fiblist");
  var item = document.createElement("li");
  var ans;
  var len = fib_list.length;
  if (len < 2){
    ans = fib(len);
  }
  else {
    ans = fib_list[len - 1] + fib_list[len - 2];
  }
  fib_list.push(ans);
  item.innerHTML = ans;
  list.appendChild(item);
  // dynamic programming, add to list
};

var fact = function(n) {
  return (n != 1) ? n * fact(n - 1) : 1;
};

var fact_list = [];

var addFact = function(e) {
  //console.log(e);
  var list = document.getElementById("factlist");
  var item = document.createElement("li");
  var n = list.getElementsByTagName("li").length;
  item.innerHTML = fact(n + 1);
  list.appendChild(item);
};

var addFact2 = function(e) {
  //console.log(e);
  var list = document.getElementById("factlist");
  var item = document.createElement("li");
  var ans;
  var len = fact_list.length;
  if (len < 1) {
    ans = fact(1);
  }
  else {
    ans = fact_list[len - 1] * (len + 1);
  }
  fact_list.push(ans);
  item.innerHTML = ans;
  list.appendChild(item);
  // dynamic programming, add to list
}

var fb = document.getElementById("fb");
fb.addEventListener('click', addFib2);

var ft = document.getElementById("ft");
ft.addEventListener('click', addFact);
