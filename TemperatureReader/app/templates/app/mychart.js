define(['d3', 'wq/pandas', 'wq/chart'], function(d3, pandas, chart) {

var svg = d3.select('svg');
var plot = chart.timeSeries();
pandas.get('timeseries.csv', function(data) {
    svg.datum(data).call(plot);
});

});