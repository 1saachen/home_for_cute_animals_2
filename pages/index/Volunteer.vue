<template>
    <view class="archive-page">
        <view class="header">
            <view class="back-button" @click="goBack">
                <image src="/static/fanhui.png" class="back-icon" />
            </view>
            <view class="archive-title">志愿报名</view>
        </view>
        <view class="box" hover-class="boxHover">
            <view class="inner" hover-class="innerHover">此区域还未开放</view>
        </view>
    </view>
</template>


<script setup>
import { ref } from 'vue';

const records = ref([]);

function goBack() {
    uni.navigateBack();
}

/* function loadRecords() {
    // 在这里实现加载动物档案数据的逻辑
    // 示例：records.value = fetchRecordsFromAPI();
}

function goToSearch() {
    uni.navigateTo({ url: '/pages/search/search' });
} */

</script>


<style scoped>
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
    top: 1.7vh;
    z-index: 1000;
}

.back-icon {
    width: 30px;
    height: 30px;
    top: 2.7vh;
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

.archive-page {
    display: flex;
    flex-direction: column;
    position: relative;
    background-color: #ffedbe;
    height:95vh;
    top:5vh;
}

.box{
    width: 60vw;
    height: 100px;
    position:absolute;
    top:45%;
    left:25vw;
    margin: 5px;
    font-size: 30px;
}
</style>
