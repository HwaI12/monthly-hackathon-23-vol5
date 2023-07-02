<template>
  <head>
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css2?family=Kosugi+Maru&display=swap" rel="stylesheet">
  </head>
  <div class="chart">
    <div>
      {{ displayedText }}
    </div>
    <!-- フッター部分 -->
    <footer>
      <div class="fo_button">
        <button class="left_button" :class="{ active: activeButton === 'button_1' }" @click="button_1">全体</button>
        <button :class="{ active: activeButton === 'button_2' }" @click="button_2">生活に必要な支出</button>
        <button :class="{ active: activeButton === 'button_3' }" @click="button_3">自己投資の支出</button>
        <button class="right_button" :class="{ active: activeButton === 'button_4' }" @click="button_4">心を豊かにする支出</button>
      </div>
    </footer>
    <!-- グラフ部分 -->
    <canvas class="canva" ref="chartCanvas"></canvas>
  </div>
</template>

<script>
import { Line } from 'chart.js';
import axios from 'axios';

export default {
  data(){
    return{
      activeButton: 'button_1',
      scores: [],
    }
  },
  mounted() {
    this.button_1();
  },
  methods: {
    displayText(text) {
      this.displayedText = text;
    },
    async getData(){
      await axios.get("/calc")
      .then((res) => {
        this.scores = res.data
      })
      .catch((error) => {
        console.log(error)
      })
    },
    renderChart(chartData) {
      const ctx = this.$refs.chartCanvas.getContext('2d');
      
      const config = {
        type: 'line',
        data: chartData,
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            y: {
              beginAtZero: true,
              ticks: {
                stepSize: 20,
                suggestedMax: 100
              }
            }
          }
        }
      }; 
      new Line(ctx, config);
    },
    button_1() {
      this.activeButton = 'button_1';
      const chartData1 = {
        labels: ['6/1', '6/2', '6/3', '6/4', '6/5', '6/6', '6/7', '6/8', '6/9', '6/10', '6/11', '6/12', '6/13', '6/14', '6/15', '6/16', '6/17', '6/18', '6/19', '6/20', '6/21', '6/22', '6/23', '6/24', '6/25', '6/26', '6/27', '6/28', '6/29', '6/30'],
        
        datasets: [
          {
            label: 'life',
            data: [0, 14, 19, 23, 24, 29, 30, 35, 36, 38,
            38, 45, 49, 49, 49, 50, 52, 55, 58, 58, 
            60, 61, 61, 61, 63, 65, 69, 70, 88, 90],
            fill: false,
            borderColor: 'rgb(236, 69, 32)',
            tension: 0.1
          },
          {
            label: 'investment',
            data: [0, 0, 0, 0, 0, 0, 0, 30, 30, 30,
            30, 38, 38, 38, 40, 40, 40, 40, 40, 40, 
            40, 40, 40, 40, 70, 80, 80, 80, 80, 80],
            fill: false,
            borderColor: 'rgb(11, 173, 232)',
            tension: 0.1
          },
          {
            label: 'enrich',
            data:  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 30, 30, 30, 30, 100, 100, 
            100, 100, 100, 100, 100, 100, 100, 100, 100, 100],
            fill: false,
            borderColor: 'rgb(241, 126, 42)',
            tension: 0.1
          },
        ]
      };
      this.renderChart(chartData1);
    },
    button_2() {
      this.activeButton = 'button_2';
      const chartData2 = {
        labels: ['6/1', '6/2', '6/3', '6/4', '6/5', '6/6', '6/7', '6/8', '6/9', '6/10', '6/11', '6/12', '6/13', '6/14', '6/15', '6/16', '6/17', '6/18', '6/19', '6/20', '6/21', '6/22', '6/23', '6/24', '6/25', '6/26', '6/27', '6/28', '6/29', '6/30'],
        datasets: [
          {
            label: 'life',
            data: [900, 1000, 1100, 1140, 1300, 1300, 1500, 1600, 1900, 2200,
            2400,2500, 2500, 2500, 2600, 2800, 3000, 3100, 3300, 
            3900, 4000, 4100, 4100, 4500, 4500, 4800, 5800, 5900, 5900],
            fill: false,
            borderColor: 'rgb(236, 69, 32)',
            tension: 0.1
          },
        ]
      };
      this.renderChart(chartData2);
    },
    button_3() {
      this.activeButton = 'button_3';
      const chartData3 = {
        labels: ['6/1', '6/2', '6/3', '6/4', '6/5', '6/6', '6/7', '6/8', '6/9', '6/10', '6/11', '6/12', '6/13', '6/14', '6/15', '6/16', '6/17', '6/18', '6/19', '6/20', '6/21', '6/22', '6/23', '6/24', '6/25', '6/26', '6/27', '6/28', '6/29', '6/30'],
        datasets: [
          {
            label: 'investment',
            data: [0, 0, 0, 0, 0, 900, 900, 900, 920, 920,
            920 , 1100, 1100, 1100, 1200, 1200, 1200, 1200, 1200, 
            1200, 1200, 1200, 1200, 1200, 2100, 2400, 2400, 2400, 2400],
            fill: false,
            borderColor: 'rgb(11, 173, 232)',
            tension: 0.1
          },
        ]
      };
      this.renderChart(chartData3);
    },
    button_4() {
      this.activeButton = 'enrich';
      const chartData = {
        labels: ['6/1', '6/2', '6/3', '6/4', '6/5', '6/6', '6/7', '6/8', '6/9', '6/10', '6/11', '6/12', '6/13', '6/14', '6/15', '6/16', '6/17', '6/18', '6/19', '6/20', '6/21', '6/22', '6/23', '6/24', '6/25', '6/26', '6/27', '6/28', '6/29', '6/30'],
        datasets: [
          {
            label: 'Dataset4',
            data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0 , 0, 0, 0, 300, 300, 300, 1000, 1500, 
            1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 2400],
            fill: false,
            borderColor: 'rgb(241, 126, 42)',
            tension: 0.1
          },
        ]
      };
      this.renderChart(chartData);
    }
  }
};
</script>

<style scoped>
button {
  color: #2a324e;
  font-size: 18px;
  background-color: #f9f9f9;
  width: 200px;
  height: 65px;
  margin: -3px;
  border: 3px solid #f6d247;
  font-weight: bold;
}

.left_button {
  border-top-left-radius: 30px;
  border-bottom-left-radius: 30px;
}

.right_button {
  border-top-right-radius: 30px;
  border-bottom-right-radius: 30px;
}

footer {
  position: fixed;
  left: 0;
  bottom: 0;
  width: 100%;
  background-color: #f4f5f3ff;
  padding: 10px;
  text-align: center;
  margin: px;
}

.fo_button {
  margin: 30px;
}

.active {
  background-color: #f6d247;
  color: #c52920;
}

.chart {
  width: 650px; 
  height: 500px;
  margin: 30px auto;
}

nav{
  background-color: #f6d247;
  padding: 20px;
  font-size: 20px;
}



</style>