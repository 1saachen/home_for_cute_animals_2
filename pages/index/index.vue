<template>
    <view class="index-page">
        <image src="/static/homepagepic.png" class="top-image" mode="aspectFill"></image>
        <view class="nickname-box">
            <button class="nickname-text" type="balanced" @click="navigateTo('/pages/index/Login/login')">
                {{ isLogged ? userNickname : '登录' }}
            </button>
            <image src="/static/fanhui1.png" class="fanhui"></image>
        </view>
        <view class="avatar-container">
            <image :src="isLogged ? userAvatar : '/static/denglu.png'" class="avatar"></image>
        </view>
        <view class="gradient-section"></view>
        <view class="menu-section">
            <view class="menu-title-with-lines">
                <view class="decor-line left-line"></view>
                <text class="menu-title">&nbsp;菜单&nbsp;</text>
                <view class="decor-line right-line"></view>
            </view>
            <view class="menu-box">
                <view class="menu-item" @click="navigateTo('/pages/index/Profile')">
                    <image src="/static/dangan.png" class="dangan-pic"></image>
                    <text class="menu-text">萌物档案</text>
                </view>
                <view class="sub-menu">
                    <view class="sub-menu-item" @click="navigateTo('/pages/index/Adoption')">
                        <image src="/static/mcly.png" class="sub-pic1"></image>
                        <text class="sub-text">萌物领养</text>
                    </view>
                    <view class="sub-menu-item" @click="navigateTo('/pages/index/Volunteer')">
                        <image src="/static/zybm.png" class="sub-pic2"></image>
                        <text class="sub-text">志愿报名</text>
                    </view>
                    <view class="sub-menu-item" @click="navigateTo('/pages/index/Donation')">
                        <image src="/static/mwjz.png" class="sub-pic3"></image>
                        <text class="sub-text">萌物募捐</text>
                    </view>
                </view>
            </view>
        </view>
    </view>
</template>


<script setup>
import { ref, onMounted } from 'vue';

const isLogged = ref(false);
const userNickname = ref('用户昵称');
const userAvatar = ref('/static/user-avatar.png');

function navigateTo(url) {
    uni.navigateTo({ url });
}

onMounted(() => {
  // 页面加载时从本地存储中获取用户信息
  const userInfo = uni.getStorageSync('userInfo');
  if (userInfo) {
    // 如果本地存储中有用户信息，则更新响应式变量的值
    userNickname.value = userInfo.nickname;
    userAvatar.value = userInfo.avatarUrl;
    isLogged.value = true; // 假设存在用户信息即用户已登录
  }
});

function validateUserInfo(userInfo) {
  // 确保昵称存在且不为空，否则使用默认值
  userNickname.value = userInfo.nickname && userInfo.nickname.trim() !== '' ? userInfo.nickname : '未命名用户';
  userAvatar.value = userInfo.avatarUrl ? userInfo.avatarUrl : '/static/user-avatar.png';
  isLogged.value = true; // 假设存在用户信息即用户已登录
}

function handleLogin() {
    if (!isLogged.value) {
        uni.login({
            provider: 'weixin',
            success: function(loginRes) {
                console.log('登录成功：', loginRes);
                uni.getUserInfo({
                    provider: 'weixin',
                    success: function(infoRes) {
                        console.log('用户信息：', infoRes);
                        isLogged.value = true;
                        userNickname.value = infoRes.userInfo.nickName;
                        userAvatar.value = infoRes.userInfo.avatarUrl;
                    }
                });
            }
        });
    }
}
</script>


<style scoped>
.index-page {
	display: flex;
	flex-direction: column;
	background-color: #d3b188;

}

.nickname-box {
	position: absolute;
	width: 30vw;
	height: 5vh;
	left: 0;
	top: 7vh;
	background: #FFDE8A;
	border-radius: 0 12px 12px 0;
	display: flex;
	align-items: center;
	justify-content: center;
}

.nickname-text {
	font-size: 20px;
	line-height: 24px;
	color: #604500;
	margin-top: -2px;
	margin-left: -2vw;
	    background: #FFDE8A;
    border: none;
    width: 100%;
}

.fanhui {
	width: 21px;
	height: 21px;
	top: 99px;
}

.avatar-container {
	position: relative;
	width: 24vw;
	height: 24vw;
	top: -12vw;
	left: 5vw;
}

.avatar {
	width: 100%;
	/* 填满容器 */
	height: 100%;
	/* 填满容器 */
	background: #FFF6C9;
	/* 头像背景颜色 */
	border: 2rpx solid #604500;
	/* 头像边框 */
	border-radius: 50%;
	/* 圆形头像 */
}

.top-image {
	width: 750rpx;
	height: 50vh;
	/* 根据实际图片高度调整 */
}

.menu-section {
	flex: 1;
	display: flex;
	flex-direction: column;
	align-items: center;
	padding-top: 20rpx;
	background: linear-gradient(180deg, #D4B189 0%, #FFEDBE 100%);
}

.menu-title-with-lines {
	display: flex;
	align-items: center;
	margin-top: -8vh;
	margin-bottom: 1.5vh;
}

.menu-title {
	font-family: PingFang SC;
	font-size: 40rpx;
	line-height: 28rpx;
	color: #604500;
	margin: 0 10rpx;
	/* 调整标题与装饰线之间的间距 */
}

.decor-line {
	width: 40rpx;
	height: 6.9rpx;
	/* 线的高度用宽度表示 */
	background-color: #604500;
	border-radius: 10rpx;
}

.left-line {
	margin-right: 10rpx;
	/* 装饰线与标题的间距 */
}

.right-line {
	margin-left: 10rpx;
	/* 装饰线与标题的间距 */
}

.menu-box {
	width: 83vw;
	background-color: #FFFBF1;
	box-shadow: 0 15rpx 15rpx rgba(0, 0, 0, 0.25);
	border-radius: 100rpx;
	padding: 30rpx;
	height: 34vh;
}

.menu-item {
	display: flex;
	background: #FFE091;
	border-radius: 20rpx;
	text-align: center;
	align-items: center;
	justify-content: center;
	font-size: 4vh;
	color: #604500;
	margin-bottom: 30rpx;
	margin-top: 2vh;
	margin-left: 1.5vw;
	height: 13vh;
	width: 79vw;
	border-radius: 20px;

}

.menu-text {
	font-size: 4vh;
	color: #604500;
	margin-top: 0vh;
	margin-bottom: 1vh;
}

.dangan-pic {
	width: 20vw;
	height: 18.54vw;
	margin-right: 10vw;
	margin-left: -5vw;
	margin-top: 0vh;
}

.paw-icon {
	width: 10vw;
	height: 10vw;
	margin-left: 10vw;
	margin-right: -5vw;

}

.sub-menu {
	display: flex;
	justify-content: space-between;

}

.sub-menu-item {
	position: relative;
	background: #FFE091;
	border-radius: 20px;
	width: 23vw;
	text-align: center;
	font-size: 2vh;
	font-weight: bold;
	color: #604500;
	padding: 20rpx 0;
	margin-left: 1.5vw;
	margin-right: 1.5vw;
	height: 12vh;
}

.sub-pic1 {
	position: absolute;
	/* 设置绝对定位 */
	top: 5vw;
	/* 向上偏移，使图片位于文字盒子之上 */
	width: 15vw;
	height: 6vh;
}

.sub-pic2 {
	position: absolute;
	/* 设置绝对定位 */
	top: 7vw;
	/* 向上偏移，使图片位于文字盒子之上 */
	width: 16vw;
	height: 5vh;
}

.sub-pic3 {
	position: absolute;
	/* 设置绝对定位 */
	top: 5vw;
	/* 向上偏移，使图片位于文字盒子之上 */
	width: 10vw;
	height: 6vh;
	margin-left: 3vw;
}

.sub-text {
	position: relative;
	top: 8vh;
}

.gradient-section {
	position: absolute;
	width: 750rpx;
	/* 设计稿宽度为750px，直接转换为750rpx */
	height: 50vh;
	/* 高度按照设计稿比例转换 */
	top: 762.04rpx;
	/* top 位置按照设计稿比例转换 */
	background: linear-gradient(180deg, #D4B189 0%, #FFEDBE 100%);
	z-index: -1;
}</style>