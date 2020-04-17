// Peihua Huang, Jackie Lin (Team Har Gow Siu Mai)
// SoftDev2 pd1
// K18 -- Come Up For Air
// 2020-04-20

var btn = document.getElementById('render');

var render = function(e){
  // d3 stuff
  d3.entries(data.shift);
  console.log(data);
  console.log(data.slice(0, 20));
  console.log(d3.extent(data, d => d.date));
  console.log(d3.extent(data, d => d.value));

};

btn.addEventListener('click', render);
