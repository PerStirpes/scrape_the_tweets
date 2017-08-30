//import { getRandom } from '/utls/generateRandNumber.js'; works with chrome 61

const svg = d3.select("svg"),
    width = +svg.attr("width"),
    height = +svg.attr("height"),
    g = svg.append("g").attr("transform", "translate(18," + (height / 4) + ")");
    
d3.csv('data/tweets_local_results.csv', function(error, twitter) {
    // returns array of tweets
    console.log(twitter)
    const dumbTweets = twitter.map(tweet => tweet.tweets)
    const needsABarOfSoap = dumbTweets[getRandom(0, dumbTweets.length-1)]
    // returns keyed object
    const copy = twitter.map((d) => {
        return {
            date: d.date,
            time: d.time,
            tweet: d.tweets
        }
    })

function update(data) {
  const t = d3.transition()
      .duration(3000);

  let text = g.selectAll("text")
    .data(data, function(d) { return d; });
  text.exit()
       .attr("class", "exit")
    .transition(t)
       .attr("y", 100)
       .style("fill-opacity", 1e-6)
       .remove();
  text.attr("class", "update")
       .attr("y", 0)
       .style("fill-opacity", 1)
    .transition(t)
       .attr("x", function(d, i) { return i * 10});
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


update(dumbTweets[getRandom(0, dumbTweets.length-1)]);

d3.interval(function() {
    update(dumbTweets[getRandom(0, dumbTweets.length - 1)]);
}, 3500);

})

function getRandom(floor, ceiling) {
    return Math.floor(Math.random() * (ceiling - floor + 1)) + floor;
}

