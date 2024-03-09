<template>
  <view class="login-page" style="background-color: white; text-align: center;">
    <text class="title">登录页</text>
    <image src="/static/logo.png" alt="Logo" class="logo"></image>
    <view>
      <image src="/static/login.png" alt="Login" @click="redirectToWechatAuth" class="click-button"></image>
    </view>
    <view class="agreement-container">
      <view @click="toggleAgreement" class="radio-container">
        <view class="agreement-radio" :class="{ 'radio-selected': hasAgreed }"></view>
        <text class="agreement-text">我已阅读并同意《用户协议》和《隐私协议》</text>
      </view>
    </view>
    <view>
      <image src="/static/request.jpg" alt="Request" @click="handleRequest" v-if="!hasAgreed" class="request"></image>
    </view>
  </view>
</template>


<script setup>
import { ref } from 'vue';

const hasAgreed = ref(false);

function redirectToWechatAuth() {
  if (hasAgreed.value) {
    // 用户已同意，执行跳转逻辑
    uni.navigateTo({url: '/pages/index/Login/authorization'});
  } else {
    // 用户未同意，弹出提示框
    uni.showModal({
      title: '提示',
      content: '请先阅读并同意用户协议和隐私政策',
      showCancel: false
    });
  }
}

function toggleAgreement() {
  hasAgreed.value = !hasAgreed.value;
}


function handleRequest() {
  if (hasAgreed.value) {
    // 处理请求逻辑
    console.log('处理请求');
  } else {
    uni.showModal({
      title: '提示',
      content: '请先阅读并同意用户协议和隐私政策',
      showCancel: false
    });
  }
}
</script>


<style scoped>
/* 在这里添加样式 */

.login-page {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 7vh;
  height: 100vh;
}

.title {
  font-size: 20px;
  margin-bottom: 10vh;
}

.logo {
  width: 107px;
  height: 147px;
  margin-bottom: 5vh;
}

.click-button {
  width: 70vw;
  height: 4.7vh;
  margin: 20px;
}

.radio-container {
  display: flex;
  align-items: center;
  cursor: pointer;
}

.agreement-radio {
  width: 20px;
  height: 20px;
  border: 2px solid #999;
  border-radius: 50%;
  margin-right: 10px;
  position: relative;
}

.radio-selected::before {
  content: '';
  position: absolute;
  width: 12px;
  height: 12px;
  background-color: #000;
  border-radius: 50%;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.agreement-text {
  display: inline-block;
  vertical-align: middle;
}

.request{
  width:40vw;
  height:5vh;
  margin-left:-30vw;
}
</style>



