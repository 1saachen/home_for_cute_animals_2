<template>
    <view class="archive-page">
        
        <view class="header">
            <!-- 返回按钮 -->
            <view class="back-button" @click="goBack">
                <image src="/static/fanhui.png" class="back-icon" />
            </view>
            <view class="archive-title">
                萌物档案
                
            </view>
        </view>


        <!-- 萌物档案标题 -->
        
        <view class="card"><image src="/static/orangecatpaw.png" class="paw-icon" /><text class="name">蛋白</text><text class="title">的档案</text></view>
        
        
        <!-- 动物照片 -->
        <view class="animal-photo-container">
            <image src="/static/蛋白.png" class="animal-photo" />
        </view>
        <image src="/static/bigcatpaw.png" class="big-paw-icon" />
        <!-- 动物基本信息 -->
        <view class="animal-info">
            <view class="info-row"><text class="label">性别</text><text class="value">♂</text></view>
            
            <view class="info-row"><text class="label">品种</text><text class="value">XXXX</text></view>
            
            <view class="info-row"><text class="label">身体特征</text><text class="value">头顶一缕刘海是灰色的，其他毛毛都是白色</text></view>
            
            <view class="info-row"> <text class="label">出没范围</text><text class="value">信息学部XXX</text></view>
           
            <view class="info-row"><text class="label">性格</text><text class="value">有点怕陌生人</text></view>
            
            <view class="info-row"><text class="label">是否绝育</text><text class="value">否</text></view>
            
            <view class="info-row"><text class="label">健康状况</text><text class="value">健康状况良好</text></view>
            
            <view class="info-row"><text class="label">社交情况</text><text class="value">通常会与另外两位小伙伴一起出现玩耍</text></view>
            
            <view class="info-row"><text class="label">其他</text><text class="value">XXX</text></view>
            
            <!-- 其他信息... -->
        </view>

        <!-- 浪花背景图 -->
        <view class="wave-background1">
            <image src="/static/wave-background1.png"></image>

        </view>
        <view class="wave-background2">
            <image src="/static/wave-background2.png"></image>
        </view>
    </view>
</template>

<script setup>
import { ref } from 'vue';

const keyword = ref(''); // 搜索关键词，使用ref创建响应式变量

// 退回上一页的方法
const goBack = () => {
  uni.navigateBack();
};

// 搜索方法，待实现
const search = (value) => {
  console.log('搜索功能待实现');
};

// 可以添加更多方法
</script>


<style scoped>
.archive-page {
    position: relative;
    width: 100%;
    min-height: 100vh;
    background-color: #FFFAF0;
    /* 页面背景色 */
}

.header{
    display:flex;
    flex-direction:column;
    padding-top: 0vh;
}
.back-button {
    position: absolute;
    left: 10px;
    top:6.5vh;
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
    margin-top: 5vh;
    background-color: #fbde95;
    height: 6vh;
    font-size: 22px;
    color: #4d3806;
    
}

.card{
    margin-top:2vh;
    background-color: #ffde8a;
    position: absolute;
    height:4.5vh;
    width:40vw;
    z-index:5;
    border-radius: 0 12px 12px 0;
     box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}
.name {
    position: absolute;
    margin-top: 4px;
    left: 10vw;
    font-size: 22px;
    color: #FF9900;
}

.title{
    position: absolute;
    margin-top: 8px;
    margin-left: 1vw;
    left: 20vw;
    font-size: 18px;
    color: #4d3806;
}
.paw-icon {
    width: 45px;
    height: 40px;
    margin-top: 0.2vh;
    z-index: 7;

}

.big-paw-icon {
    width: 40vw;
    height: 40vw;
    position: absolute;
    top: 32vh;
    right: 0;
    z-index: 0;
}

.animal-photo-container {
    display: flex;
    justify-content: center;
}

.animal-photo {
    width: 70vw;
    height: 70vw;
    max-width: 300px;
    border-radius: 50%;
    margin-top: 10px;
    z-index: 4;
}

.animal-info {
    display: flex;
    flex-direction: column;
    margin-top: 20px;
    flex-wrap: nowrap;
}

.info-row{
    display:flex;
    align-items: center;
    margin-bottom: 15px;
}

.label {
    font-size: 16px;
    color: #604500;
    z-index: 5;
    margin-left: 2vw;
    margin-right: 10px;
    background-image: url('/static/fish.png');
    background-repeat: no-repeat;
    font-size: 16px;
    display: flex;
    padding: 5px 10px;
    background-size: contain;
    font-family: SimHei;
    align-items: center;
    justify-content: center;
    min-width: 80px;
    height: 25px;

}

.value {
    font-size: 16px;
    color: #604500;
    margin-bottom: 10px;
    z-index: 5;
    font-family: SimHei;
}


.wave-background2 {
    width: 100%;
    position: absolute;
    top: 40vh;
}

.wave-background1 {
    width: 100%;
    position: absolute;
    top: 39vh;
}

.wave-background2 image {
    top:30vh;
    width: 100%;
    height: 65vh;
    
}

.wave-background1 image {
    width: 100%;
    height: 45vh;
}

.wave-background1 {
    z-index: 1;
}

.wave-background2 {
    z-index: 2;
}
</style>
