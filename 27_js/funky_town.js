var fact = function(n) {
	if (n == 1){
    return 1;
  }
  else {
    return n * (fact(n - 1));
  }
};

var fibonacci = function(n) {
  var first = 0;
  var second = 1;
  while (n > 0){
    var temp = first;
    first = second;
    second = temp + second;
    n -= 1;
  }
  return first;
};

var gcd = function(a, b) {
  var dend, dsor, r;
  if (a > b){
    dend = a;
    dsor = b;
    r = a % b;
  }
  else{
    dend = b;
    dsor = a;
    r = b % a;
  }
  while (r > 0){
    dend = dsor;
    dsor = r;
    r = dend % dsor;
  }
  return dsor;
};

var randomStudent = function() {
  var list = ["student a", "b,", "c"]
  return list.length;
};
