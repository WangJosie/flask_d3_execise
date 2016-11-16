  var width =750,
      height =500; 

  var fill = d3.scale.category20();

  d3.json("tmp.json", function(data) {
    var leaders =data
      .filter(function(d) {return +d.y >3; })
      .map(function(d) {return {text:d.x, size: +d.y}; })
      .sort(function (a, b) {return d3.descending(a.size, b.size); })
      .slice(0, 100); 

  d3.layout.cloud().size([width, height])
      .words(leaders)
      .rotate(function() { return ~~(Math.random() * 2) * 90; })
      .font("Impact")
      .fontSize(function(d) { return d.size; })
      .on("end", draw)
       .start();

  function draw(words) {
     d3.select("#word-cloud").append("svg")
         .attr("width", width)
        .attr("height", height)
      .append("g")
        .attr("transform", "translate("+(width/2)+","+(height /2)+")")
      .selectAll("text")
        .data(words)
      .enter().append("text")
        .style("font-size", function(d) { return d.size + "px"; })
        .style("font-family", "Impact")
        .style("fill", function(d, i) { return fill(i); })
        .attr("text-anchor", "middle")
        .attr("transform", function(d) {
          return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
        })
        .text(function(d) { return d.text; });
  }
