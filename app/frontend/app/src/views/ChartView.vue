<template>
    <div class="chart">
      <div>
        {{ displayedText }}
      </div>
      <footer>
        <div class="fo_button">
          <button class="left_button" :class="{ active: activeButton === 'button_1' }" @click="button_1">全体</button>
          <button :class="{ active: activeButton === 'button_2' }" @click="button_2">生活に必要な支出</button>
          <button :class="{ active: activeButton === 'button_3' }" @click="button_3">自己投資の支出</button>
          <button class="right_button" :class="{ active: activeButton === 'button_4' }" @click="button_4">心を豊かにする支出</button>
        </div>
      </footer>
      <canvas class="canva" ref="chartCanvas"></canvas>
    </div>
  </template>
  
  <script>
  import { Line } from 'chart.js';
  
  export default {
    data() {
      return {
        activeButton: 'button_1',
        displayedText: '',
      };
    },
    mounted() {
      this.button_1();
    },
    methods: {
      displayText(text) {
        this.displayedText = text;
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
                  suggestedMax: 100,
                },
              },
            },
          },
        };
        new Line(ctx, config);
      },
      button_1() {
        this.activeButton = 'button_1';
        const chartData1 = {
          labels: ['1日', '2日', '3日', '4日', '5日', '6日', '7日', '8日', '9日', '10日'],
          datasets: [
            {
              label: 'seikatu',
              data: [0, 14, 19, 30, 45, 49, 50, 70, 88, 90],
              fill: false,
              borderColor: 'rgb(236, 69, 32)',
              tension: 0.1,
            },
            {
              label: 'ziko',
              data: [0, 0, 10, 13, 20, 24, 31, 80, 90, 100],
              fill: false,
              borderColor: 'rgb(11, 173, 232)',
              tension: 0.1,
            },
            {
              label: 'kokoro',
              data: [3, 73, 81, 88, 90, 92, 94, 96, 98, 100],
              fill: false,
              borderColor: 'rgb(241, 126, 42)',
              tension: 0.1,
            },
          ],
        };
        this.renderChart(chartData1);
      },
      button_2() {
        this.activeButton = 'button_2';
        const chartData2 = {
          labels: ['A', 'B', 'C', 'D', 'E', 'F'],
          datasets: [
            {
              label: 'Dataset2',
              data: [30, 40, 50, 60, 70, 80],
              fill: false,
              borderColor: 'rgb(255, 0, 0)',
              tension: 0.1,
            },
          ],
        };
        this.renderChart(chartData2);
      },
      button_3() {
        this.activeButton = 'button_3';
        const chartData3 = {
          labels: ['A', 'B', 'C', 'D', 'E', 'F'],
          datasets: [
            {
              label: 'Dataset3',
              data: [30, 40, 50, 60, 70, 80],
              fill: false,
              borderColor: 'rgb(255, 0, 0)',
              tension: 0.1,
            },
          ],
        };
        this.renderChart(chartData3);
      },
      button_4() {
        this.activeButton = 'button_4';
        const chartData4 = {
          labels: ['A', 'B', 'C', 'D', 'E', 'F'],
          datasets: [
            {
              label: 'Dataset4',
              data: [30, 40, 50, 60, 70, 80],
              fill: false,
              borderColor: 'rgb(255, 0, 0)',
              tension: 0.1,
            },
          ],
        };
        this.renderChart(chartData4);
      },
    },
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
  
  nav {
    background-color: #f6d247;
    padding: 20px;
    font-size: 20px;
  }
  </style>