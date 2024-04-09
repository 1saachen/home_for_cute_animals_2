<template>
    <view class="archive-page">
        <view class="header">
            <view class="back-button" @click="goBack">
                <image src="/static/fanhui.png" class="back-icon" />
            </view>
            <view class="archive-title">萌物募捐</view>
        </view>
        <view class="view-accounts-button" @click="viewPublicAccounts">
            <text class="text">点击查看公开账务</text>
        </view>
        <view class="main-content">
            <scroll-view class="record-list" scroll-y="true">
                <view class="animal-list-container">
                    <view class="animal-card" v-for="(animal, index) in animals" :key="index" @click="goToDetail(animal)">
                        <view class="image-container">
                            <image :src="animal.image" class="animal-image" />
                        </view>
                        <view class="rescue-info">
                            <text class="rescue-title">{{ animal.rescueType }}</text>
                            <text class="rescue-background">{{ animal.background }}</text>
                            <view class="progress-bar-container">
                                <text class="fundraised-amount">已筹款：{{ animal.fundraisedAmount }}元</text>
                                <text class="target-amount">目标金额：{{ animal.targetAmount }}元</text>
                                <view class="progress-bar">
                                    <view class="progress" :style="{ width: animal.fundraisingProgress * 180 / 100 + 'px' }">
                                        <text class="progress-percentage" :style="{ right: (100 - animal.fundraisingProgress) + '%' }">{{ animal.fundraisingProgress }}%</text>
                                    </view>
                                </view>
                            </view>
                        </view>
                    </view>
                </view>
            </scroll-view>
        </view>
    </view>
</template>

<script setup>
import { ref } from 'vue';

const animals = ref([
    {
        name: '雪花',
        image: '/static/雪花.png',
        gender: '♀',
        status: ['已绝育', '已免疫', '已驱虫'],
        applications: 0,
        rescueType: '救助流浪猫',
        background: '小区发现流浪猫，需要救助',
        fundraisingProgress: 50,
        fundraisedAmount: 1000,
        targetAmount: 2000
    },
]);

function goBack() {
    uni.navigateBack(); 
}

function goToDetail(animal) {
    console.log("Selected Animal: ", animal);
    // 这里添加跳转到详情页的逻辑
    uni.navigateTo({ url: `/pages/index/Donation/donationdetail?name=${animal.name}` });
}

function viewPublicAccounts() {
    // 这里添加查看公开账务的逻辑
}
</script>

<style scoped>
.archive-page {
    display: flex;
    flex-direction: column;
    position: relative;
    background-color: #FFFAF0;
    padding-top: 5vh;
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

.archive-title {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin-top: 0vh;
    background-color: #fbde95;
    height: 6vh;
    font-size: 22px;
    color: #4d3806;
}

.view-accounts-button {
    position: absolute;
    display: flex;
    justify-content: center;
    align-items: center;
    width: 70vw;
    height: 4vh;
    left: calc(50% - 319px / 2);
    top: 12vh;
    background: #FF9900;
    box-shadow: inset 0px 0.5px 0px rgba(0, 0, 0, 0.18), 2px 2px 4px rgba(0, 0, 0, 0.25);
    border-radius: 8px;
    font-family: 'PingFang SC';
    font-size: 22px;
    text-align: center;
    color: #FFFFFF;
    padding-bottom: 3vh;
}

.text {
    font-family: SimHei;
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 100%;
    margin-top: 2vh;
}


.main-content {
    display: flex;
    height: 100vh;
    flex-direction: column;
    align-items: center;
    margin-top: 8.5vh;
}

.record-list {
    flex: 1;
    width: 100%;
}

.animal-list-container {
    display: flex;
    flex-wrap: wrap;
    flex-direction: column;
    align-items: center;
    justify-content: space-around;
    padding: 20px;
}

.animal-card {
    width: 80vw;
    height: 15vh;
    background: #FFEDBE;
    box-shadow: 4px 4px 20px rgba(0, 0, 0, 0.25);
    border-radius: 20px;
    padding: 10px;
    display: flex;
    align-items: center;
    margin-bottom: 2vh;
}

.image-container {
    width: 18vh;
    height: 12vh;
    margin-left: 1.5vw;
    top: 30px;
    background: #D9D9D9;
    border-radius: 5px;
}

.animal-image {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.rescue-info {
    width: 70%;
    padding-left: 10px;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.rescue-title {
    padding-left: 0vw;
    padding-top: 0vh;
    margin-bottom:5px;
    width: 100%;
    height: 4vh;
    font-family: 'PingFang SC';
    font-size: 24px;
    color: #604500;
}

.rescue-background {
    font-size: 10px;
    color: #604500;
    margin-bottom: 10px;
}

.progress-bar {
    width: 100%;
    height: 12px;
    background-color: #f9f9f9;
    border-radius: 6px;
    margin-top: 5px;
    flex-grow: 1;
}

.progress-bar-container {
    width: 100%;
    margin-top: 5px;
}

.progress {
    height: 12px;
    background-color: #FF9900;
    border-radius: 6px;
    padding-top: 0px;
    position: relative;
}

/* 进度百分比样式 */
.progress-percentage {
    position: absolute; /* 相对于进度条定位 */
    right: 0; /* 右对齐 */
    top: 0px; /* 在进度条上方显示 */
    font-family: 'PingFang SC';
    font-size: 8px;
    color: #fbfafa;
    line-height: 10px;
    background: #FF9900;
    border-radius: 6px;
    padding: 0 3px; /* 文本内边距 */
    transform: translateX(50%); /* 向右偏移，保持文本居中 */
}

.fundraised-amount {
    font-size: 10px;
    color: #604500;
    margin-bottom: 5px;
    flex: 1;
    text-align: left;
    white-space: nowrap;
}

.target-amount {
    font-size: 10px;
    color: #604500;
    margin-bottom: 5px;
    position:relative;
    flex: 1;
    text-align: right;
    white-space: nowrap;
    right: -20px;
}</style>
