<template>
    <view class="success-page">
        <view class="back-button" @click="goBack">
                    <image src="/static/fanhui.png" class="back-icon" />
                </view>
        <view class="text">长按二维码付款</view>
        <image  class="picture" src="/static/QRcode.png"/>
    </view>
</template>
<script>
export default {
    methods: {
        goBack() {
            uni.navigateBack(); // 实现返回上一页
        },
        confirmAction() {
            // TODO: 添加确定按钮的点击逻辑
            uni.navigateTo({ url: '/pages/index/Adoption' });
        },
        cancelAction() {
            // TODO: 添加撤销按钮的点击逻辑
            uni.navigateTo({ url: '/pages/index/Adoption' });
        }
    }
}
</script>
<style>
.success-page {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    position: relative;
    width: 100%;
    height: 100vh;
    background-color: #fffbf0;
}

.text{
    font-family:SimHei;
    font-weight:600;
    font-size:25px;
    line-height:35px;
    color:#FF9900;
    margin-bottom:5vw;
}

.picture{
    width:50vw;
    height:50vw;
}

.success-icon {
    width: 35vw;
    /* 根据实际图标大小调整 */
    height: 35vw;
    /* 根据实际图标大小调整 */
    display: flex;
    margin-left: 10vw;
    margin-top: -10vh;
    margin-bottom: 2vh;
}

.message {
    display: flex;
    align-items: center;
    justify-content: center;
}

.detail {
    display: flex;
    align-items: center;
    justify-content: center;
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
.success-message {
    font-family: 'PingFang SC';
    font-weight: 600;
    font-size: 40px;
    color: #FF9900;
    margin-bottom: 2vh;
    align-items: center;
    justify-content: center;
}

.success-detail {
    font-family: 'PingFang SC';
    font-size: 20px;
    color: #979797;
    margin-bottom: 40px;
}

.button {
    width: 228px;
    height: 48.95px;
    border-radius: 5px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 20px;
    cursor: pointer;
    filter: drop-shadow(0px 4px 30px rgba(0, 0, 0, 0.2));
}

.confirm-button {
    background: #1CC600;
    color: #FFFFFF;
    font-size: 25px;
}

.cancel-button {
    background: #FFFFFF;
    color: #000000;
    border: 1px solid #D8D8D8;
    font-size: 25px;
}
</style>