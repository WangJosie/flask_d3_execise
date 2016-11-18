
//$.ajax("tmp.csv", {
  //  success: function(data) {
  //      var csv = d3.csv.parse(data);
  //      console.table(csv);
  //  }
//});

function draw(data) {

/*
  D3.js setup code
*/

    "use strict";
    var margin = 20,
        width = 800 - margin,
        height = 600 - margin;

    d3.select("body")
      .append("h2")
      //.text("Word Count")

    var chart2 = d3.select("body")
      .append("svg")
        .attr("width", width + margin)
        .attr("height", height + margin)
      .append('g')
          .attr('class','chart');

/*
  Dimple.js Chart construction code
*/

    var myChart = new dimple.chart(chart2, data);
    var x = myChart.addMeasureAxis("x", "count");
    myChart.addCategoryAxis("y", "label");
    myChart.addSeries(null, dimple.plot.bar);
    //myChart.addMeasureAxis("x", "Count");
    //x.dateParseFormat = "%Y";
    //x.tickFormat = "%Y";
    //x.timeInterval = 4;
    //myChart.addSeries(null, dimple.plot.line);
    //myChart.addSeries(null, dimple.plot.scatter);
    myChart.draw();
  };

d3.csv("/static/tmp.csv", draw);
/*
Use D3 (not dimple.js) to load the TSV file
and pass the contents of it to the draw function
*/
