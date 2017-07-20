function csv2Array(str) {
  var csvData = [];
  var lines = str.split("\n");
  for (var i = 0; i < lines.length; ++i) {
    var cells = lines[i].split(",");
    csvData.push(cells);
  }
  return csvData;
}

function drawBarChart(data) {
  var tmpLabels = [], tmpData1 = [], tmpData2 = [];
  for (var row in data) {
    tmpLabels.push(data[row][0])
    tmpData1.push(data[row][1])
    tmpData2.push(data[row][2])
  };

//温度グラフ
  var ctx = document.getElementById("tmpChart").getContext("2d");
  var tmpChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: tmpLabels,
      datasets: [
        { label: "温度(℃)", data: tmpData1, backgroundColor: "rgba(75,192,192,0.4)" },
      ]
    }
  });

//湿度グラフ
  var ctx = document.getElementById("humChart").getContext("2d");
  var humChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: tmpLabels,
      datasets: [
        { label: "湿度(％)", data: tmpData2, backgroundColor: "rgba(200,192,192,0.4)" },
      ]
    }
  });
}

function main() {
  var req = new XMLHttpRequest();
  var filePath = 'data/data.csv';
  req.open("GET", filePath, true);
  req.onload = function() {
    data = csv2Array(req.responseText);
    drawBarChart(data);
  }
  req.send(null);
}

main();
