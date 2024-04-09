<template>
    <view class="archive-page">
        <view class="header">
            <view class="back-button" @click="goBack">
                <image src="/static/fanhui.png" class="back-icon" />
            </view>
            <view class="archive-title">萌物领养</view>
        </view>
        <view class="main-content">
            <view class="adoption-card">
                <image src="/static/maozhua4.png" class="paw-icon"/>
                <view class="animal-image-container"></view>
                <text class="animal-name">{{ selectedAnimal.name }}</text>
                <image src="/static/fengexian.png" class="split-line"/>
                <text class="animal-date">{{ selectedAnimal.date }}</text>
                <view class="view-profile" @click="viewProfile">
                    <image src="/static/mengwudangan.png" class="profile-icon" />
                </view>
                <image src="/static/changfengexian.png" class="long-line"/>
                <view class="adoption-requirements">
                    <text class="requirement-title">领养要求</text>
                    <view class="requirement-list">
                        <view class="requirement-item" v-for="requirement in selectedAnimal.requirements" :key="requirement">
                             <image src="/static/pointer.png" class="pointer-icon"/>
                            <text>{{ requirement }}</text>
                        </view>
                    </view>
                </view>
                <view class="apply">
                    <image src="/static/bianji.png" class="apply-icon"/>
                    <text class="application-count">已申请人数：{{ selectedAnimal.applications }}人</text>
                </view>
                <view class="action-buttons">
                    <view class="collect-button">
                        <image src="/static/shoucang.png" class="collect-icon" />收藏
                    </view>
                    <view class="share-button">
                        <image src="/static/fenxiang.png" class="share-icon" />分享
                    </view>
                </view>
                <view class="apply-button" @click="goToApply">申请领养</view>
            </view>
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
    requirements: ['封窗封网', '定期驱虫', '适龄绝育']
});

function goBack() {
    uni.navigateBack();
}

function goToApply() {
    uni.navigateTo({ url: '/pages/index/Adoption/application' });
}

function viewProfile() {
    uni.navigateTo({ url: `/pages/index/Profile/detail1` });
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
    height:70vh;
    top:15vh;
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
    position: absolute;
    width: 50px; /* 根据实际内容调整宽度 */
    height: 21px;
    left: calc(50% - 40px/2);
    top: 200px; /* 调整以使其位于日期上方 */
    font-family: 'SimHei';
    font-size: 23px;
    line-height: 28px;
    color: #604500;
    mix-blend-mode: normal;
    opacity: 0.9;
}

.split-line {
    width: 20%;
    height: 2px;
    position: absolute;
    margin-top: 37px;
    margin-left: 32vw;
}

/* 日期样式 */
.animal-date {
    position: absolute;
    width: 30vw; /* 根据实际内容调整宽度 */
    height: 18.78px;
    left: calc(50% - 68px/2);
    top: 232px; /* 调整以使其位于雪花下方 */
    font-family: 'PingFang SC';
    font-size: 14px;
    line-height: 20px;
    color: #979797;
}




.view-profile {
    width: 70vw;
    height: 69px;
    border-radius: 20px;
    margin-top: 8vh;
    display: flex;
    position: relative;
    align-items: center;
    justify-content: center;
    left:5vw;
    font-size: 25px;
}

.long-line{
    width:70vw;
    height:1px;
    margin-left:5vw;
    margin-bottom: 0vh;
}

.requirement-title {
    font-size: 27px;
    color:#604500;
    margin-top: 5vh;
    font-family:SimHei;
    line-height: 45px;
    margin-left:5vw;
}

.pointer-icon{
    width:7vw;
    height:7vw;
    margin-bottom: 4.5vw;
    margin-right:3vw;
    position:relative;
}

.requirement-list{
    margin-top: 1vh;

}

.requirement-item {
    display: flex;
    font-size: 20px;
    color: #604500;
    margin-top: -0.5vh;
    margin-left:5vw;
    font-family:SimHei;
}

.apply{
    display:flex;
    margin-bottom: 2vh;
}

.application-count {
    font-size: 24px;
    color: #604500;
    margin-top: 0vh;
    font-family:SimHei;
    line-height: 28px;
    margin-left:5vw;
}

.apply-icon{
    width: 28px;
    height: 28px;
    margin-top: 0vh;
    margin-right: 0vw;
    margin-left: 5vw;
}


.profile-icon {
    width: 90vw;
    height: 10vh;
}
.action-buttons {
    display: flex;
    justify-content: space-around;
    width: 100%;
    margin-top: 2vh;
}

.collect-button,
.share-button {
    width: 120px;
    height: 55px;
    background: rgba(254, 153, 0, 0.32);
    border-radius: 50px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
    color: #ff9900;
}

.apply-button {
    width: 100vw;
    height: 55px;
    position:absolute;
    background: #FF9900;
    color: #FFFFFF;
    text-align: center;
    line-height: 49px;
    border-radius: 0;
    font-size: 23px;
    margin-top: 20px;
    right:-5.1vw;
    top:100%;
    font-family: SimHei;
}

.collect-icon{
    width: 30px;
    height: 30px;
    margin-right: 5px;
}

.share-icon{
    width: 30px;
    height: 30px;
    margin-right: 5px;
}
</style>
