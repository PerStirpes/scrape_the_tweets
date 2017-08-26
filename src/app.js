var svg = d3.select("svg"),
    width = +svg.attr("width"),
    height = +svg.attr("height"),
    g = svg.append("g").attr("transform", "translate(18," + (height / 4) + ")");

d3.csv('data/tweets_local_results.csv', function(error, twitter) {
    // returns array of tweets
    var dumbTweets = twitter.map(tweet => tweet.tweets)
    var needsABarOfSoap = dumbTweets[getRandom(0, dumbTweets.length-1)]
    // returns keyed object
    var copy = twitter.map((d) => {
        return {
            date: d.date,
            time: d.time,
            tweet: d.tweets
        }
    })

///////////////////////
function update(data) {
  var t = d3.transition()
      .duration(1000);

  // JOIN new data with old elements.
  var text = g.selectAll("text")
    .data(data, function(d) { return d; });

  // EXIT old elements not present in new data.
  text.exit()
       .attr("class", "exit")
    .transition(t)
       .attr("y", 100)
       .style("fill-opacity", 1e-6)
       .remove();

  // UPDATE old elements present in new data.
  text.attr("class", "update")
       .attr("y", 0)
       .style("fill-opacity", 1)
    .transition(t)
       .attr("x", function(d, i) { return i * 10});

  // ENTER new elements present in new data.
  text.enter().append("text")
       .attr("class", "enter")
       .attr("dy", "10em")
       .attr("y", -60)
       .attr("x", function(d, i) { return i * 10; })
       .style("fill-opacity", 1e-6)
       .text(function(d) { return d; })
    .transition(t)
       .attr("y", 0)
       .style("fill-opacity", 1); 
}

// The initial display.
update(dumbTweets[getRandom(0, dumbTweets.length-1)]);

d3.interval(function() {
    update(dumbTweets[getRandom(0, dumbTweets.length - 1)]);
}, 2000);

// end of the callback
})

function getRandom(floor, ceiling) {
    return Math.floor(Math.random() * (ceiling - floor + 1)) + floor;
}