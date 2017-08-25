
// make console.log write to the page for better in-browser experience
// (function () {
//   var body = document.querySelector('body');
//   body.style['fontFamily'] = 'monospace';
//   body.style['fontSize'] = '2em';
//   console.log = function (x) { body.innerText += x + '\n'; };
// }());


d3.csv('data/tweets_local_results.csv', function (data) { 
     console.log(data);
})

// d3.csv('data/tweets_results.csv', function (data) { 
//      console.log(data);
// })