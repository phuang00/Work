// Peihua Huang, Jackie Lin (Team Har Gow Siu Mai)
// SoftDev2 pd1
// K18 -- Come Up For Air
// 2020-04-20

var btn = document.getElementById('render');

var i;
for (i = 0; i < datas.length; i++){
  datas[i]['date'] = new Date(datas[i]['date'], 0, 1, 0, 0, 0, 0);
};


var render = function(e){
  var space = document.getElementById('line1');
  space.innerHTML = "";

  var data = datas.slice(0, 20);

  // set the dimensions and margins of the graph
  var margin = {top: 10, right: 30, bottom: 30, left: 100},
      width = 460 - margin.left - margin.right,
      height = 400 - margin.top - margin.bottom;

  // append the svg object to the body of the page
  var svg = d3.select("#line1")
    .append("svg")
      .attr("width", width + margin.left + margin.right)
      .attr("height", height + margin.top + margin.bottom)
    .append("g")
      .attr("transform",
            "translate(" + margin.left + "," + margin.top + ")");

  // Add X axis --> it is a date format
  var x = d3.scaleTime()
    .domain(d3.extent(data, function(d) { return d.date; }))
    .range([ 0, width ]);
  svg.append("g")
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(x));

  // Add Y axis
  var y = d3.scaleLinear()
    .domain([0, d3.max(data, function(d) { return +d.value; })])
    .range([ height, 0 ]);
  svg.append("g")
    .call(d3.axisLeft(y));

  // Add the line
  svg.append("path")
    .datum(data)
    .attr("fill", "none")
    .attr("stroke", "steelblue")
    .attr("stroke-width", 1.5)
    .attr("d", d3.line()
      .x(function(d) { return x(d.date) })
      .y(function(d) { return y(d.value) })
      );
  svg.selectAll(".dot")
      .data(data)
    .enter().append("circle") // Uses the enter().append() method
      .attr("class", "dot") // Assign a class for styling
      .attr("cx", function(d) { return x(d.date) })
      .attr("cy", function(d) { return y(d.value) })
      .attr("r", 2)
      .attr("fill", "steelblue");

  console.log(data);
  console.log(d3.extent(data, d => d.date));


};

btn.addEventListener('click', render);
