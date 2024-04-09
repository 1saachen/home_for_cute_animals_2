<template>
    <view class="index-page">
        <view class="header">
            <!-- 返回按钮 -->
            <view class="archive-title">·欢迎来到萌物有珈</view>
        </view>
        <image src="/static/homepagepic.png" class="top-image" mode="aspectFill"></image>

        <view class="avatar-container">
            <image :src="isLogged ? userAvatar : '/static/denglu.png'" class="avatar"></image>
            <view class="nickname-box">
                <button open-type="chooseAvatar" class="nickname-text" type="balanced" @chooseavatar="handleLogin">
                    {{ isLogged ? userNickname : '登录' }}
                </button>
            </view>
        </view>
        <image src="/static/gerenzhongxin.png" class="grzx-icon" @click="goToCenter"/>
        <view class="background"></view>
        <view class="menu-wrapper">
            <view class="menu-section">
                <!-- 我的消息 -->
                <view class="menu-item" @click="navigateToMessages">
                    <image src="/static/xiaoxi.png" class="xiaoxi-icon"></image>
                    <text class="menu-text">我的消息</text>
                </view>

                <!-- 我的领养申请 -->
                <view class="menu-item" @click="navigateToAdoptionApplications">
                    <image src="/static/lingyang.png" class="lingyang-icon"></image>
                    <text class="menu-text">我的领养申请</text>
                </view>

                <!-- 其他菜单项... -->
                <view class="menu-item" @click="navigateToDonationRecords">
                    <image src="/static/juanzeng.png" class="juanzeng-icon"></image>
                    <text class="menu-text">我的捐赠记录</text>
                </view>
                <view class="menu-item" @click="navigateToVolunteerRecords">
                    <image src="/static/zhiyuan.png" class="zhiyuan-icon"></image>
                    <text class="menu-text">我的志愿记录</text>
                </view>
                <view class="menu-item" @click="contactUs">
                    <image src="/static/lianxi.png" class="lianxi-icon"></image>
                    <text class="menu-text">联系我们</text>
                </view>
                <view class="menu-item" @click="navigateToFeedback">
                    <image src="/static/fankui.png" class="fankui-icon"></image>
                    <text class="menu-text">问题反馈</text>
                </view>
            </view>
        </view>

    </view>
</template>




<script setup>
import { ref, onMounted } from 'vue';

// 定义响应式状态
const isLogged = ref(false);
const userNickname = ref('用户昵称');
const userAvatar = ref('/static/denglu.png'); // 默认头像路径

// 定义具体的导航函数
const goToCenter = () => navigateTo('/pages/profile/personalCenter/personalCenter');
const navigateToAdoptionApplications = () => navigateTo('/pages/profile/adoptionApplications/adoptionApplications');
const navigateToDonationRecords = () => navigateTo('/pages/profile/donationRecords/donationRecords');
// 添加其他导航函数
// 页面加载时检查用户信息
onMounted(() => {
  const userInfo = uni.getStorageSync('userInfo'); // 从本地存储获取用户信息
  if (userInfo) {
    isLogged.value = true; // 更新登录状态
    userNickname.value = userInfo.nickname; // 更新用户昵称
    userAvatar.value = userInfo.avatarUrl; // 更新用户头像
  }
});

// 方法用于导航
const navigateTo = (url) => {
  uni.navigateTo({ url });
};


// 其他方法按需定义...
</script>


<style scoped>
.index-page {
    display: flex;
    flex-direction: column;
    background-color: linear-gradient(#e1c6a0, #feebbd);
    position: relative;
    height: 100vh;

}

.grzx-icon {
    width: 30vw;
    height: 11vw;
    position: absolute;
    top: 11vh;
    left: 1vw;

}

.archive-title {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin-top:5vh;
    background-color: #fbde95;
    height: 6vh;
    width:100vw;
    font-size: 22px;
    color: #4d3806;
    font-family:SimHei;
}


.nickname-box {
    position: absolute;
    width: 30vw;
    height: 5vh;
    left: -3vw;
    top: 100%;
    background: transparent;
    border: none;
    display: flex;
    align-items: center;
    justify-content: center;
}

.nickname-text {
    font-size: 25px;
    line-height: 3vh;
    color: #604500;
    margin-top: 2vh;
    margin-left: 0vw;
    background: transparent;
    border: none;
    width: 100%;
}

.avatar-container {
    position: absolute;
    width: 24vw;
    height: 24vw;
    top: 30vh;
    left: 38vw;
}

.avatar {
    width: 100%;
    height: 24vw;
    background: #FFF6C9;
    /* 头像背景颜色 */
    border: 2rpx solid #604500;
    /* 头像边框 */
    border-radius: 50%;
    /* 圆形头像 */
}

.top-image {
    width: 100vw;
    height: 40vh;
    filter: blur(2px);
    /* 根据实际图片高度调整 */
    z-index: -2;
}

.background {
    z-index: -1;
    position: absolute;
    top: 37vh;
    width: 100vw;
    height: 63vh;
    background: linear-gradient(#d2b28c, #fdeabc);
    opacity: 0.8;
}

.menu-wrapper {
    position: absolute;
    width: 84vw;
    height: 44vh;
    left: 8vw;
    top: 52vh;
    background: rgba(255, 251, 241, 0.5);
    box-shadow: 0px 12px 8px 0px #00000040;
    border-radius: 12px;
}

.menu-section {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    /* 内容靠左对齐 */
    background: linear-gradient(#f0e1c9, #fdf2d6);
    /* 渐变背景 */
    padding: 0px;
    /* 根据需要调整内边距 */
    width: 84vw;
    /* 根据需要调整宽度 */
    height: 44vh;
    margin-top: 1vh;
    border-radius: 12px;
}


.menu-item {
    display: flex;
    text-align: left;
    align-items: center;
    justify-content: left;
    font-size: 4vh;
    color: #604500;
    margin-top: 0vh;
    margin-left: 1.5vw;
    height: 8vh;
    width: 79vw;
    padding-left: 2vw;
    border-color: #604500;
    border-bottom: 1px solid #604500;

}

.menu-text {
    font-size: 22px;
    font-family: SimHei;
    color: #604500;
    margin-top: 0vh;
    margin-bottom: 1vh;
    font-weight: bold;
}

.xiaoxi-icon {
    width: 10vw;
    height: 7vw;
    margin-right: 8vw;
}

.lingyang-icon {
    width: 9vw;
    height: 10vw;
    margin-right: 9vw;
}

.juanzeng-icon {
    width: 8vw;
    height: 10vw;
    margin-right: 10vw;
}

.zhiyuan-icon {
    width: 12vw;
    height: 7vw;
    margin-right: 6vw;
}

.lianxi-icon {
    width: 10vw;
    height: 9vw;
    margin-right: 8vw;
}

.fankui-icon {
    width: 10vw;
    height: 10vw;
    margin-right: 8vw;
}
</style>