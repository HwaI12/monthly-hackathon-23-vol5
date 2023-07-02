<template>
  <div class="about">
    <div class="amount">
      <!-- 日付 -->
      <p>6/30</p>
      <input class="input_amount" type="text" name="name">
      <p>円</p>
    </div>
    <div class="reasons">
      <!-- 入力理由 -->
      <div class="kuuhaku"></div>
      <div class="reasons-container">
        <input class="input_reasons" type="text" name="name">
      </div>
    </div>
    <div class="but">
      <button :class="{ active: activeButton === 'fix' }" id="click-btn" @click="fix">修正</button>
      <button :class="{ active: activeButton === 'decision' }" id="decision" @click="decision">決定</button>
    </div>
    <footer>
      <div class="output">
        <p>{{ outputText }}</p>
      </div>
    </footer>
    <div id="popup-wrapper">
      <div id="popup-inside">
        <div id="close">×</div>
        <div id="button_fix">
          <button @click="selectButton('生活に必要な支出')">生活に必要な支出</button>
          <button @click="selectButton('自己投資の支出')">自己投資の支出</button>
          <button @click="selectButton('心を豊かにする支出')">心を豊かにする支出</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      activeButton: '', // 選択されているボタン
      outputText: '', // 出力テキスト
      isPopupOpen: false // ポップアップの表示状態
    };
  },
  methods: {
    openPopup() {
      this.isPopupOpen = true;
    },
    closePopup() {
      this.isPopupOpen = false;
    },
    selectButton(button) {
      this.activeButton = button;
      this.outputText = `${button}`;
      this.isPopupOpen = false;
    },
    decision() {
      this.activeButton = 'decision';
      const options = ['生活に必要な支出', '自己投資の支出', '心を豊かにする支出'];
      const randomIndex = Math.floor(Math.random() * options.length);
      this.outputText = options[randomIndex];
    },
    fix() {
      this.activeButton = 'fix';
      this.openPopup();
    }
  },
  mounted() {
    const clickBtn = document.getElementById('click-btn');
    const popupWrapper = document.getElementById('popup-wrapper');
    const close = document.getElementById('close');

    clickBtn.addEventListener('click', () => {
      popupWrapper.style.display = "block";
    });

    popupWrapper.addEventListener('click', e => {
      if (e.target.id === popupWrapper.id || e.target.id === close.id) {
        popupWrapper.style.display = 'none';
      }
    });
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
    margin-bottom: 30px;
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
    margin-bottom: 35px;
  }
  
  .but {
  display: flex;
  justify-content: space-between;
  width: 20%;
  }

  .but button {
    flex-grow: 1;
    margin-right: 10px;
    margin-left: 10px;
  }

  #decision{
    background-color: #f6d247;
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
  .output {
    font-family: 'Kosugi Maru', sans-serif;
    color: #c52920;
    font-size: 60px;
    font-weight: bold;
    text-align: center;
  }
  
  #popup-wrapper {
  background-color: rgba(0, 0, 0, .5);
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: none;
}

#popup-inside {
  text-align: center;
  width: 600px;
  height: 300px;
  background: white;
  margin: 140px auto 145px;
  padding: 20px;
  position: relative;
  line-height: 2;
}

#button_fix{
  margin: 30px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

#button_fix button{
  font-family: 'Kosugi Maru', sans-serif;
  color: #c52920;
  background-color: #fff;
  border: 3px solid #c52920;
  font-size: 25px;
  padding: 15px 25px;
  font-weight: bold;
  margin-bottom: 30px;
  width: 300px;
  height: 60px;
  text-align: center;
  outline: none;
  cursor: pointer;
}

#message p {
  color: #2a324e;
  text-decoration: none;
  font-size: 20px;
  width: 600px;
  height: 300px;
  margin:0px;
  display: flex;
  align-items: center;
}

#close {
  font-size: 60px;
  font-weight: bold;
  color: #c52920;
  position: absolute;
  top: -20px;
  right: 5px;
  cursor: pointer;
}

  </style>

