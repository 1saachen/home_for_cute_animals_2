<template>
    <view class="archive-page">
        <view class="header">
            <view class="back-button" @click="goToIndex">
                <image src="/static/fanhui.png" class="back-icon" />
            </view>
            <view class="archive-title">萌物领养</view>
        </view>
        <view class="main-content">
            <scroll-view class="record-list" scroll-y="true">
                <view class="animal-list-container">
                    <view class="animal-card" v-for="animal in animals" :key="animal.name" @click="() => goToDetail(animal)">
                        <view class="image-container">
                            <image :src="animal.image" class="animal-image" />
                        </view>
                        <text class="animal-name">{{ animal.name }}</text>
                        <text class="animal-gender">{{ animal.gender }}</text>
                        <view class="status-tags">
                            <view class="status-tag" v-for="status in animal.status" :key="status">
                                <text :class="['status-text', status === '未免疫' ? 'status-unimmunized' : '']">
                                    {{ status }}
                                </text>
                            </view>
                        </view>
                        <text class="application-count-title">已申请人数：</text>
                        <text class="application-count">{{ animal.applications }}人</text>
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
        applications: 0
    },
    {
        name: '面包',
        image: '/static/面包.png',
        gender: '♂',
        status: ['已绝育', '未免疫', '已驱虫'],
        applications: 3
    },
    // ...其他动物数据
]);

function goToIndex() {
    uni.switchTab({
        url: '/pages/index/index'
    });
}

function goToDetail(animal) {
    console.log("Selected Animal: ", animal);
    let status = animal.status.join(',');
    uni.navigateTo({
        url: `/pages/index/Adoption/adoptiondetail?name=${animal.name}&image=${animal.image}&gender=${animal.gender}&status=${status}&applications=${animal.applications}`
    });
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




.main-content {
    display: flex;
    height: 100vh;
}


.record-list {
    flex: 1;
    padding: 20px;
}

.record-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    background-color: #FFFFFF;
    border-radius: 20px;
    margin-bottom: 20px;
}

.animal-list-container {
    display: flex;
    flex-wrap: wrap;
    flex-direction: column;
    align-items: center;
    justify-content: space-around;
    padding: 5px;

}

.animal-card {
    width: 80vw;
    height: 15vh;
    left: 2vw;
    top: 1vh;
    background: #FFEDBE;
    box-shadow: 4px 4px 20px rgba(0, 0, 0, 0.25);
    border-radius: 20px;
    display: flex;
    align-items: center;
    padding: 10px;
    margin-bottom: 2vh;
}

.animal-image {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.image-container {
    width: 12vh;
    height: 10vh;
    margin-left: 2vw;
    top: 37px;
    background: #D9D9D9;
    border-radius: 5px;
}

.animal-name {
    padding-left: 3vw;
    padding-top: -10vh;
    width: 62px;
    height: 10vh;
    font-family: 'PingFang SC';
    font-size: 24px;
    text-align: center;
    color: #604500;
}

.animal-gender {

    width: 62px;
    height: 10vh;
    left: 230px;
    top: 37px;
    font-family: 'PingFang SC';
    font-size: 24px;
    color: #604500;
}


.status-tags {
    position: absolute;
    width: 53px;
    height: 100px;
    left: 65vw;
    margin-top: 2vh;
    display: flex;
    flex-direction: column;
}

.status-tag {
    width: 55px;
    height: 30px;
    background: #FF9900;
    border-radius: 5px;
    margin-bottom: 6px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.status-text {
    font-family: 'SimHei';
    font-size: 13px;
    color: #FFFFFF;
    text-align: center;
}

.status-unimmunized {
    background: #FFFFFF;
    width: 55px;
    height: 30px;
     display: flex;
    align-items: center;
    justify-content: center;
        border-radius: 5px;
    color: #FF9900;
}

.application-count {
    position: absolute;
    width: 104px;
    height: 35px;
    left: 38vw;
    margin-top: 10vh;
    font-family: 'PingFang SC';
    font-size: 13px;
    color: #604500;
}

.application-count-title {
    position: absolute;
    width: 104px;
    height: 35px;
    left: 38vw;
    margin-top: 6vh;
    font-family: 'PingFang SC';
    font-size: 13px;
    color: #604500;
}
</style>