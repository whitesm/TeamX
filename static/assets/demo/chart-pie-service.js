// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Pie Chart Example
// if(myPiechart_Service != undefined) myPieChart_Service.destroy();

var ctx = document.getElementById("myPieChart_Service");
var myPieChart_Service = new Chart(ctx, {
  type: 'pie',
  data: {
    labels: ["긍정", "부정","판별불가"],
    datasets: [{
      data: service_value,
      backgroundColor: ['#007bff', '#dc3545', '#ffc107'],
    }],
  },
});
