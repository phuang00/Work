var fact = function(n) {
	if (n == 1){
    return 1;
  }
  else {
    return n * (fact(n - 1));
  }
};

var fibonacci = function(n) {
  if (n == 0){
		return 0;
	}
	if (n == 1){
		return 1;
	}
	return fibonacci(n - 1) + fibonacci(n - 2);
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
  var list = ['William', 'Joseph', 'Calvin', 'Ethan', 'Moody', 'Mo', 'Big Mo', 'Peihua', 'Saad', 'Benjamin', 'Justin', 'Alice', 'Hilary', 'Ayham', 'Michael', 'Matthew', 'Jionghao', 'Devin', 'David', 'Jacob', 'Will', 'Hannah', 'Alex'];
  return list[Math.floor(Math.random() * list.length)];
};

var eventHelper = function(btn) {
	var ans;
	if (btn == "fxn1"){
		ans = fibonacci(5);
		console.log(ans);
		document.getElementById("p1").innerHTML = "fibonacci(5) = " + ans;
	}
	else if (btn == "fxn2"){
		ans = gcd(15, 225);
		console.log(ans);
		document.getElementById("p2").innerHTML = "gcd(15, 225) = " + ans;
	}
	else if (btn == "fxn3"){
		ans = randomStudent();
		console.log(ans);
		document.getElementById("p3").innerHTML = "randomStudent() = " + ans;
	}
};

var btn1 = document.getElementById("fxn1");
btn1.addEventListener('click', function(){
	eventHelper(btn1.id);
});

var btn2 = document.getElementById("fxn2");
btn2.addEventListener('click', function(){
	eventHelper(btn2.id);
});

var btn3 = document.getElementById("fxn3");
btn3.addEventListener('click', function(){
	eventHelper(btn3.id);
});
