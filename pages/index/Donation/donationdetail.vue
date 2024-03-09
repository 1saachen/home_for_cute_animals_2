<template>
  <view class="archive-page">
    <view class="header">
      <view class="back-button" @click="goBack">
        <image src="/static/fanhui.png" class="back-icon" />
      </view>
      <view class="archive-title">萌物募捐</view>
    </view>

    <view class="main-content">
      <view class="adoption-card">
        <image src="/static/maozhua4.png" class="paw-icon" />
        <view class="animal-image-container"></view>
        <text class="animal-name">{{ selectedAnimal.name }}</text>
        <image src="/static/fengexian.png" class="split-line-short"/>
        <view class="fundraising-card">
          <view class="progress-container">
            <view class="text">
              <text class="progress-title">已筹款：</text>
              <text class="progress-amount">{{ selectedAnimal.fundraisedAmount }} / {{ selectedAnimal.targetAmount }}元</text>
            </view>
            <view class="progress-bar">
              <view class="progress" :style="{ width: selectedAnimal.fundraisingProgress + '%' }"></view>
            </view>
          </view>
        </view>
        <view class="information-section">
          <view class="info-item" v-for="info in selectedAnimal.information" :key="info.title">
            <image src="/static/pointer.png" class="pointer-icon" />
            <text class="info-title">{{ info.title }}</text>
            <text class="info-content">{{ info.content }}</text>
          </view>
        </view>
        <view class="split-line"></view>
        <image src="/static/star.png" class="star"/>
        <view class="commitbox">
          <text class="commitment">我们承诺：所有筹款均用于流浪动物救助保护！欢迎跟进监督公开账务!</text>
        </view>
        <image src="/static/share2.png" class="share" />
      </view>
      <view class="apply-button" @click="goToPay">我想捐款</view>
    </view>
  </view>
</template>

<script setup>
import { ref } from 'vue';

const selectedAnimal = ref({
  name: '雪花',
  image: '/static/雪花.png',
  date: '2024-02-08',
  status: ['已绝育', '已免疫', '已驱虫'],
  applications: 0,
  requirements: ['封窗封网', '定期驱虫', '适龄绝育'],
  fundraisingProgress: 50,
  fundraisedAmount: 1000,
  targetAmount: 2000,
  information: [
    { title: "负责人:", content: "XXX" },
    { title: "募捐背景:", content: "XXXX" },
    { title: "募捐宗旨:", content: "XXXX" },
    { title: "募捐目标:", content: "XXXX" },
    { title: "联系我们:", content: "XXXX" },
    { title: "备注:", content: "XXXX" },
  ]
});

function goBack() {
  uni.navigateBack();
}

function goToPay() {
  uni.navigateTo({ url: '/pages/index/Donation/pay' });
}
</script>


<style scoped>
.archive-page {
    display: flex;
    flex-direction: column;
    position: relative;
    background-color: #FFFAF0;
    padding-top: 50px;
}

.header {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    background-color: #fbde95;
    height: 6vh;
    font-size: 22px;
    color: #4d3806;
}

.back-button {
    position: absolute;
    left: 10px;
    top: 6.7vh;
    z-index: 1000;
}

.back-icon {
    width: 30px;
    height: 30px;
}

.main-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
}

.adoption-card {
    position: absolute;
    width: 80%;
    background: #FFEDBE;
    box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.25);
    border-radius: 16px;
    padding: 20px;
    height: 70vh;
    top: 15vh;
    /*     margin-top: 20px; */
}

.animal-image-container {
    width: 40vw;
    height: 40vw;
    background: url('/static/雪花.png'), #D9D9D9;
    box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.25);
    border-radius: 50%;
    margin: 0 auto;
    background-size: cover;
    background-position: center;
}

.paw-icon {
    width: 10vw;
    height: 8.5vw;
    position: absolute;
    top: -1.5vh;
    left: 80vw;
}

.animal-name {
    position: relative;
    width: 50px;
    /* 根据实际内容调整宽度 */
    height: 21px;
    left: calc(50% - 56px/2);
    top: 2vw;
    /* 调整以使其位于日期上方 */
    font-family: 'SimHei';
    font-size: 28px;
    line-height: 28px;
    color: #604500;
    mix-blend-mode: normal;
    opacity: 0.9;
    margin-bottom: 20px;
}

.split-line-short {
    width: 20%;
    height: 2px;
    position: absolute;
    margin-top: 40px;
    margin-left: 18vw;
}
.fundraising-card {
    /* 样式调整 */
    display: flex;
    text-align: center;
    justify-content: center;
    width: 90%;
    background: #D4B189;
    border-radius: 20px;
    padding: 15px;
    margin-top: 7vw;
    color: #FFFFFF;
    position: relative;
    font-family: SimHei;
}

.progress-container {
    display: flex;
    flex-direction: column;

}

.progress-title {
    font-size: 20px;
    color: #fffffe;
}

.progress-bar {
    width: 70vw;
    height: 15px;
    background-color: #f9f9f9;
    border-radius: 7.5px;
    overflow: hidden;
    margin: 5px 0;
}

.progress {
    height: 15px;
    background-color: #FF9900;
    border-radius: 7.5px;
}

.progress-amount {
    font-size: 18px;
    color: #ffffff;
}

.information-section {
    padding: 10px 0;
}

.info-item {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
}

.pointer-icon {
    width: 25px;
    height: 25px;
    margin-right: 10px;
}

.info-title {
    font-size: 20px;
    font-family:SimHei;
    color: #604500;
    margin-right: 5px;
}

.info-content {
    color: #604500;
}

.split-line {
    height: 1px;
    background: rgba(0, 0, 0, 0.5);
    margin: 10px 0;
}

.commitbox{
    width:55vw;
    margin-left:8vw;
    margin-top:4vw;
}

.commitment {
    font-size: 17px;
    font-family:SimHei;
    color: #ff9900;
}

.apply-button {
    width: 100%;
    height: 55px;
    position: absolute;
    background: #FF9900;
    color: #FFFFFF;
    text-align: center;
    line-height: 49px;
    border-radius: 0;
    font-size: 23px;
    margin-top: 20px;
    top: 80%;
    font-family: SimHei;
}

.star{
    width: 5vw;
    height: 5vw;
    position:absolute;
    bottom:19vw;
    left:5vw;
}

.share{
    width:15vw;
    height:17vw;
    position: absolute;
    right:5vw;
    bottom: 8vw;
}
</style>
