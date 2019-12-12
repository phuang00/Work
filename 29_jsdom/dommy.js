var changeHeading = function(e) {
  var h = document.getElementById("h");
  if (e.type == 'mouseout'){
    h.innerHTML = "Hello World!";
  }
  else{
    h.innerHTML = e.target.innerHTML;
  };
};

var removeItem = function(e) {
  e.target.remove();
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
  console.log(e);
  var list = document.getElementById("fiblist");
  var item = document.createElement("li");
  item.innerHTML = addFib2(e);
  list.appendChild(item);
  //??? // create list
};

var addFib2 = function(e) {
  console.log(e);
  var ans;
  var len = fib_list.length;
  if (len < 2){
    ans = fib(len);
  }
  else {
    ans = fib_list[len - 1] + fib_list[len - 2];
  }
  fib_list.push(ans);
  return ans;
  // dynamic programming, add to list
};

var fb = document.getElementById("fb");
fb.addEventListener('click', addFib);
