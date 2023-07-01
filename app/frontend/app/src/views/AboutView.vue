<template>
    <div class="about">
      <div class="amount">
        <!-- 日付 -->
        <p>7/1</p>
        <input class="input_amount" type="text" name="name">
        <p>円</p>
      </div>
      <div class="reasons">
        <!-- 入力理由 -->
        <div class="kuuhaku"></div>
        <div class="reasons-container">
          <input class="input_reasons" type="text" name="name">
        </div>
        <button :class="{ active: activeButton === 'decision' }" @click="decision">決定</button>
      </div>
      <footer>
        <div class="output">
            <p>{{ outputText }}</p>
        </div>
        <!-- <button :class="{ active: activeButton === 'fix' }" class="fix" @click="fix">修正</button> -->
      </footer>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        activeButton: '',
        outputText: '' // 追加: 出力するテキストを保持するデータ
      };
    },
    methods: {
      decision() {
        this.activeButton = 'decision';
        // ランダムにテキストを選択して出力
        const options = ['生活費', '自己投資', '心'];
        const randomIndex = Math.floor(Math.random() * options.length);
        this.outputText = options[randomIndex];
      },
      fix() {
        this.activeButton = 'fix';
      }
    }
  };
  </script>
  
  <style scoped>
  .about {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center; /* 中央寄せにする */
    background-color: #f4f5f3ff;
    height: 570px;
  }
  
  .amount {
    display: flex;
    align-items: center;
    font-size: 60px;
    color: #c52920;
    font-family: 'Kosugi Maru', sans-serif;
    font-weight: bold;
    height: 110px;
    padding: 0px 20px;
    border-bottom: 4px solid;
    border-image: linear-gradient(to right, #f6d247 24%, #c52920 24%); 
    border-image-slice: 1; /* これがないと効かない */
    margin-bottom: 60px;
  }
  
  .input_amount {
    font-family: 'Kosugi Maru', sans-serif;
    color: #c52920;
    background-color: #f4f5f3ff;
    font-size: 60px;
    font-weight: bold;
    padding: 10px;
    text-align: center;
    height: 60px;
    width: 295px;
    border: none;
    outline: none; /* フォーカス時のアウトラインを消す */
    letter-spacing: 5px;
  }
  
  .reasons {
    display: flex;
    align-items: center;
    justify-content: center; /* 中央寄せにする */
    margin-top: 20px;
    background-color: #fff;
    padding: 30px;
    margin-bottom: 30px;
  }
  
  .kuuhaku {
    border: 3px;
    width: 106px;
    height: 61px;
  }
  
  .input_reasons {
    font-family: 'Kosugi Maru', sans-serif;
    color: #c52920;
    font-size: 60px;
    font-weight: bold;
    padding: 10px;
    text-align: center;
    height: 120px;
    width: 600px;
    border: none;
    outline: none; /* フォーカス時のアウトラインを消す */
  }
  
  .reasons-container {
    display: flex;
    align-items: center;
    justify-content: center;
  }
  
  button {
    font-family: 'Kosugi Maru', sans-serif;
    color: #c52920;
    background-color: #fff;
    border: 3px solid #c52920;
    font-size: 25px;
    padding: 15px 25px;
    font-weight: bold;
  }
  
  footer {
    align-items: center;
    display: flex;
    position: fixed;
    flex-direction: row;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #f6d247;
    padding: 10px;
    text-align: center;
    height: 119px;
    font-family: 'Kosugi Maru', sans-serif;
    justify-content: space-around; 
  }
  
  .fix{
    margin-left: 0%;
  }
  
  .output {
    font-family: 'Kosugi Maru', sans-serif;
    color: #c52920;
    font-size: 60px;
    font-weight: bold;
    text-align: center;
  }
  
  .active {
    background-color: #f6d247;
    color: #c52920;
  }
  </style>