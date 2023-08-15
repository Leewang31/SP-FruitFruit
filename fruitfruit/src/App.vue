<template>
<!--  <button @click="loadAndRunModel">Run Model</button>-->
  <input @change="upload" type="file" id="file" />
  <div v-if="prediction !== null">
    <p>Prediction: {{ prediction }}</p>
  </div>
  <img v-if="imgUrl" :src="imgUrl" alt="Uploaded Image" width="180"/>
</template>

<script>
import * as tf from '@tensorflow/tfjs';

export default {
  name: 'App',
  data() {
    return {
      imgUrl:undefined,
      prediction: null,
      pred_classes : {
        0: "apple",
        1: "banana",
        2: "beetroot",
        3: "bell pepper",
        4: "cabbage",
        5: "capsicum",
        6: "carrot",
        7: "cauliflower",
        8: "chilli pepper",
        9: "corn",
        10: "cucumber",
        11: "eggplant",
        12: "garlic",
        13: "ginger",
        14: "grapes",
        15: "jalepeno",
        16: "kiwi",
        17: "lemon",
        18: "lettuce",
        19: "mango",
        20: "onion",
        21: "orange",
        22: "paprika",
        23: "pear",
        24: "peas",
        25: "pineapple",
        26: "pomegranate",
        27: "potato",
        28: "raddish",
        29: "soy beans",
        30: "spinach",
        31: "sweetcorn",
        32: "sweetpotato",
        33: "tomato",
        34: "turnip",
        35: "watermelon"
      },
      model_json : undefined
    };
  },
  methods: {
    upload(event) {
      const file = event.target.files[0];
      if (file) {
        this.imgUrl = URL.createObjectURL(file); // 이미지 경로 업데이트
        this.loadAndRunModel()
      }
    },
    async preprosess_image(image_path) {
      const img = new Image();
      img.src = image_path;

      await new Promise(resolve => {
        img.onload = resolve;
      });

      const image = tf.browser.fromPixels(img); // 이미지 로드
      const resizedImage = tf.image.resizeBilinear(image, [224, 224]); // 이미지 크기 조정
      const preprocessedImage = resizedImage.div(tf.scalar(255)); // 이미지를 [0, 1] 범위로 스케일 조정
      return preprocessedImage;
    },
    async loadAndRunModel() {

      const model = await tf.loadLayersModel('http://localhost:3000/jsmodel/model.json');
      const img = await this.preprosess_image(this.imgUrl);
      const inputData = img.expandDims(); // 모델의 입력 형태에 맞게 차원 확장
      const prediction = model.predict(inputData);
      const predictionData = await prediction.data();

      const predictedClass = tf.argMax(predictionData, 0); // axis 값은 0으로 설정
      const predictNum = (await predictedClass.data())[0]; // 데이터를 배열로 변환하여 첫 번째 원소 추출

      this.prediction = this.pred_classes[predictNum];// 예측된 클래스의 인덱스
    }
  },

}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
