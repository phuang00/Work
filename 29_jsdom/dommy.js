var changeHeading = function(e) {
  var h = document.getElementById("h");
  h.innerHTML = ;//the list item stuff
};

var removeItem = function(e) {
  //element.remove() stuff
};

var list = document.getElementsByTagName("li");

for (var i=0; i<lis.length; i++) {
  lis[i].addEventListener( 'mouseover', ??? ); //call changeHeading
  list[i].addEventListener( 'mouseout', ???); // call changeHeading back to helloworld
  lis[i].addEventListener( 'click', ???); //remove list item
}

var addItem = function(e) {
  var list = ; //getElementById? list
  var item = document.createElement("li");
  ??? = "WORD"; //item.innerHTML?
}
