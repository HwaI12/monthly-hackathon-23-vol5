<template>
  <div class="about">
    <div class="yoko">
      <div class="amount">
        <p>自由</p>
        <input class="input_amount" type="text" name="name">
        <p>円</p>
      </div>
      <button id="click-btn">？</button>
    </div>
    <div id="popup-wrapper">
      <div id="popup-inside">
        <div id="close">×</div>
        <div id="message">
          <p>自由に使えるお金 = (収入+前月からの繰り越し) - (固定費+貯蓄)<br>固定費 = 家賃、光熱費、携帯の通信料金、<br>クレジット等の支払い、ローンの返済、保険・年金<br>逆に生活費は食費、日用雑貨、服飾、美容健康、<br>交際・娯楽、交通・通信、教養、医療に大雑把分けられる</p>
        </div>
      </div>
    </div>
    <div class="percent">
      <div class="percent-container">
        <p class="kuuhaku3"></p>
        <input class="input_percent" type="text" name="name">
        <p class="kuuhaku3">割</p>
        <input class="input_percent" type="text" name="name">
        <p class="kuuhaku3">割</p>
        <input class="input_percent" type="text" name="name">
        <p class="kuuhaku3">割</p>
      </div>
    </div>
    <button :class="{ active: activeButton === 'decision' }" @click="decision">決定</button>
    <footer>
      <p>生活に必要な支出</p>
      <p>自己投資の支出</p>
      <p>心を豊かにする支出</p>
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
    // 追加: ボタンのクリック時の処理
    handleClick() {
      // 処理を追加してください

      // 入力された金額を取得
      const inputAmount = document.querySelector('.input_amount');
      const amountValue = inputAmount.value;

      // 出力するテキストを設定
      this.outputText = `入力された金額は ${amountValue} 円です。`;

      // 入力欄をクリア
      inputAmount.value = '';
    },
    decision() {
        this.activeButton = 'decision';
        // ランダムにテキストを選択して出力
        const options = ['生活費', '自己投資', '心'];
        const randomIndex = Math.floor(Math.random() * options.length);
        this.outputText = options[randomIndex];
    },
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
  padding-top: 20px;
}

.yoko {
  display: flex;
  align-items: center;
}

button {
    font-family: 'Kosugi Maru', sans-serif;
    color: #c52920;
    background-color: #fff;
    border: 3px solid #c52920;
    font-size: 25px;
    padding: 15px 25px;
    font-weight: bold;
    margin-bottom:45px;
  }
.active {
    background-color: #f6d247;
    color: #c52920;
}

.amount {
  display: flex;
  align-items: center;
  font-size: 60px;
  color: #c52920;
  font-family: 'Kosugi Maru', sans-serif;
  font-weight: bold;
  height: 85px;
  padding: 0px 20px;
  border-bottom: 4px solid;
  border-image: linear-gradient(to right, #f6d247 30%, #c52920 30%);
  border-image-slice: 1; /* これがないと効かない */
  margin-bottom: -10px;
}

.jiyu {
  margin-top: 0px;
  font-size: 50px;
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
  width: 300px;
  border: none;
  outline: none; /* フォーカス時のアウトラインを消す */
  letter-spacing: 5px;
  display: flex;
  align-items: center;
}

.percent {
  display: flex;
  align-items: center;
  justify-content: center; /* 中央寄せにする */
  margin: 40px 20px 10px 20px;
  /* margin-top: 20px; */
  /* background-color: #fff; */
  padding: 30px;
  /* margin-bottom: 30px; */
  justify-content: center;
}

.kuuhaku2 {
  border: 3px;
  width: 106px;
  height: 61px;
}

.input_percent {
  font-family: 'Kosugi Maru', sans-serif;
  color: #c52920;
  font-size: 100px;
  font-weight: bold;
  text-align: center;
  height: 200px;
  width: 250px;
  border: none;
  outline: none; /* フォーカス時のアウトラインを消す */
  padding:10px 30px;
}

.percent-container {
  display: flex;
  align-items: center;
  justify-content: center;
}


.kuuhaku3{
  background-color: #fff;
  font-family: 'Kosugi Maru', sans-serif;
  color: #c52920;
  font-size: 50px;
  font-weight: bold;
  height: 220px;
  margin: 0px 100px 0px 0px;
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
#click-btn {
  display: block;
  margin: 0px 0px -10px 10px;
  background-color: #f6d247;
  color: #c52920;
  border-color: #c52920;
  border-radius: 50%; /* Make it round */
  width: 60px; /* Set a fixed width and height to make it appear as a circle */
  height: 60px;
  padding-left: 15px;
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

footer {
  align-items: center;
  display: flex;
  position: fixed;
  flex-direction: row;
  left: 0;
  bottom: 0;
  width: 100%;
  background-color: #f6d247;
  color: #c52920;
  padding: 10px;
  text-align: center;
  height: 119px;
  font-family: 'Kosugi Maru', sans-serif;
  justify-content: center; /* 変更: space-betweenにする */
  font-size: 36px;
}

footer p{
  margin: 0px 95px;
  font-weight: bold;
}

nav{
  background-color: #f6d247;
  padding: 20px;
  font-size: 20px;
}

</style>