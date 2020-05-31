// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Pie Chart Example
// myPieChart_Deliver.destroy();

var ctx = document.getElementById("myPieChart_Deliver");
var myPieChart_Deliver = new Chart(ctx, {
  type: 'pie',
  data: {
    labels: ["긍정", "부정","판별불가"],
    datasets: [{
      data: deliver_value,
      backgroundColor: ['#007bff', '#dc3545', '#ffc107'],
    }],
  },
});
