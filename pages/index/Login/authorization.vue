<template>
  <view class="container">
    <view class="header">
      <image src="/static/onlylogo.png" class="logo"></image>
      <text class="title">萌物有珈 申请使用</text>
    </view>
    <view class="content">
      <button class="avatar-wrapper" open-type="chooseAvatar" @chooseavatar="onChooseAvatar">
        <image class="avatar" :src="avatarUrl || defaultAvatarUrl"></image>
      </button>
      <input type="text" class="nickname-input" placeholder="请输入昵称" v-model="nickname" />
    </view>
    <button formType="submit" class="submit-btn" @click="onSubmit"><text class="textt">提交</text></button>
  </view>
</template>



<script setup>
import { ref } from 'vue';

const avatarUrl = ref('');
const nickname = ref('');
const defaultAvatarUrl = '/static/denglu.png';

const onChooseAvatar = (e) => {
  avatarUrl.value = e.detail.avatarUrl;
};

const onSubmit = () => {
  if (nickname.value.trim() === '') {
    uni.showToast({
      title: '昵称不能为空',
      icon: 'none',
      duration: 2000
    });
    return;
  }

  uni.setStorageSync('userInfo', {
    avatarUrl: avatarUrl.value || defaultAvatarUrl,
    nickname: nickname.value,
  });
  
  uni.switchTab({
    url: '/pages/index/index'
  });
};

</script>



<style scoped>
.container {
  display: flex;
  flex-direction: column;
  padding: 20px;
}

.header {
  display: flex;
  align-items: center;
  justify-content: left;
  margin-bottom: 20px;
  margin-left:5vw;
  margin-top:4vh;
}

.logo {
  width: 50px; 
  height: 50px; 
  margin-right: 10px;
}

.title {
  font-size: 16px;
  font-weight:bold;
}

.content {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
}

.avatar-wrapper {
  margin-bottom: 20px;
  border-radius: 50%;
  width:23vw;
  background-color: #fff;
}

.avatar {
  width: 80px; 
  height: 80px; 
  border-radius: 50%;
}

.nickname-input {
  width: 40%;
  margin: 0 auto 20px auto; 
  line-height: 1.5;
  font-size: 16px;
  padding: 10px;
  display: block; 
  border: 1px solid #ccc; 
  border-radius: 5px;
  text-align: center; 
}

.submit-btn {
  width:80%;
  height:5.5vh;
  background-color: #1AAD19;
  color: white;
  padding: 0px;
  border-radius: 5px;
}

.submit-btn .textt {
  display: block; 
  margin: 0; 
  line-height: 5.5vh; 
}
</style>

