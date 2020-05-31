// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Bar Chart Example

// document.getElementById("chart").remove();
// document.getElementById("chart").append('<canvas id="myBarChart" width="100%" height="50"></canvas>');

// for (i in myBarChart.datasets[0].points)
//     myBarChart.removeData();
// if(myBarChart != undefined) myBarChart.destroy();

var ctx = document.getElementById("myBarChart").getContext('2d');



var myBarChart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: score_lists,
    datasets: [{
      label: "Revenue",
      backgroundColor: "rgba(2,117,216,1)",
      borderColor: "rgba(2,117,216,1)",
      data : score_value,
    }],
  },
  options: {
    scales: {
      xAxes: [{
        time: {
          unit: 'score'
        },
        gridLines: {
          display: false
        },
        ticks: {
          maxTicksLimit: 5
        }
      }],
      yAxes: [{
        ticks: {
          min: 0,
          max: 50,
          maxTicksLimit: 5
        },
        gridLines: {
          display: true
        }
      }],
    },
    legend: {
      display: false
    }
  }
});

// if(myBarChart != null) // i initialize myBarChart var with null
//     myBarChart.destroy(); // if not null call destroy
//     myBarChart = new Chart(ctx).Bar(data, options);//render it again ...