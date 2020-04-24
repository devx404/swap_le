// Script for Pie Chart Graph-----------------------------------------------
		i = -1;
		function StudentCounting() {
			i++;
			return studentCounting[i];
		};
		
		var config = {	
			type: 'pie',
			data: {
				datasets: [{
					data: [
						StudentCounting(),
						StudentCounting(),
					],
					backgroundColor: [
						window.chartColors.red,
						window.chartColors.blue,
					],
					label: 'Dataset 1',
					
				}],
				labels: [
					'Male Students',
					'Female Students',
				]
			},
			showDatapoints: true,
			options: {
				responsive: true,
				title: {
					display: true,
					text: 'Total Male/Female Students'
				},
				pieceLabel: {
				    render: 'percentage',
				    fontColor: 'black',
				    precision: 2,
				    fontSize: 25,
				    fontStyle: 'italic'
				},
				
			}
		};
		
		
// Script for Time-Series Graph-------------------------------------------------------------------

		var cfg = {
			type: 'line',
			data: {
				labels: studentUsername,	
				datasets: [{
					label: 'Student Marks of ' + assessmentHeader.toUpperCase(),
					data: studentMarks,
					backgroundColor: window.chartColors.green,
					borderColor: window.chartColors.green,
					type: 'line',
					pointRadius: 3,
					fill: false,
					lineTension: 0,
					borderWidth: 1
				}]
			},
			options: {
				scales: {
					xAxes: [{
						scaleLabel: {
							display: true,
							labelString: 'STUDENT USERNAME'
						}
					}],
					yAxes: [{
						scaleLabel: {
							display: true,
							labelString: 'MARKS'
						}
					}]
				}
			}
		};
	




// window.onload for all mixups graphs and charts -----------------------------------------------------
		window.onload = function() {
			var ctx = document.getElementById('pie-chart').getContext('2d');
			window.myPie = new Chart(ctx, config);
			
			var ctx2 = document.getElementById('time-series-graph').getContext('2d');
			//ctx2.canvas.width = 1000;
			//ctx2.canvas.height = 400;
			window.myTimeSeries = new Chart(ctx2, cfg);
			
		};
