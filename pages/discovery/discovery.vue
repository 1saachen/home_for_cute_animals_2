<template>
    <view class="archive-page">
        <view class="box" hover-class="boxHover">
            <view class="inner" hover-class="innerHover">
                此区域还未开放
            </view>
        </view>
    </view>
    
    <view>-----</view>

    
</template>

<script setup>

</script>

<style lang="scss">
.archive-page {
    display: flex;
    flex-direction: column;
    position: relative;
    background-color: #ffedbe;
    height:95vh;
    top:5vh;
}
.scrollView {
    width: 80%;
    height: 220px;
    border: 1px solid red;
    white-space: nowrap;

    .box {
        width: 120px;
        height: 100px;
        background: green;
        display: inline-block;
        margin: 5px;
    }
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
