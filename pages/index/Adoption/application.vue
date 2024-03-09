<template>
    <template>
        <view class="archive-page">
            <view class="header">
                <!-- 返回按钮 -->
                <view class="back-button" @click="goBack">
                    <image src="/static/fanhui.png" class="back-icon" />
                </view>
                <view class="archive-title">填写申请</view>
            </view>

            <!-- 主体内容 -->
            <view class="main-content">
                <view class="input-container">
                    <text class="input-label">姓名：</text>
                    <input class="input-field" type="text" placeholder="请输入" />
                </view>
                <view class="input-container">
                    <text class="input-label">学院：</text>
                    <input class="input-field" type="text" placeholder="请输入" />
                </view>
                <view class="input-container">
                    <text class="input-label">手机号：</text>
                    <input class="input-field" type="text" placeholder="请输入" />
                </view>
                <view class="input-container">
                    <text class="input-label">QQ号：</text>
                    <input class="input-field" type="text" placeholder="请输入" />
                </view>
                <view class="input-container">
                    <text class="input-label">领养经验：</text>
                    <input class="input-field" type="text" placeholder="请输入" />
                </view>
                <view class="submit-button" @click="showConfirmation">提交</view>
            </view>
            <view v-if="showSubmitConfirmation" class="submit-confirmation">
                <view class="confirmation-box">
                    <view class="box-confirmation-title"></view>

                    <view class="box-confirmation-message"></view>
                    <text class="confirmation-title">确认提交</text>
                    <text class="confirmation-message">申请填写完毕，是否确认提交？</text>
                    <view class="confirmation-buttons">
                        <view class="button cancel-button" @click="cancelSubmission">取消</view>
                        <view class="button confirm-button" @click="confirmSubmission">确认</view>
                    </view>
                </view>
            </view>
        </view>
    </template>
</template>


<script setup>
import { ref } from 'vue';

const selectedAnimal = ref({
    name: '雪花',
    image: '/static/雪花.png',
    date: '2024-02-08',
    status: ['已绝育', '已免疫', '已驱虫'],
    applications: 0,
    requirements: ['封窗封网', '定期驱虫', '适龄绝育'],
});
const showSubmitConfirmation = ref(false);

function goBack() {
    uni.navigateBack();
}

function showConfirmation() {
    showSubmitConfirmation.value = true;
}

function cancelSubmission() {
    showSubmitConfirmation.value = false;
}

function confirmSubmission() {
    console.log("提交申请");
    // 逻辑处理，例如提交表单
    uni.navigateTo({ url: '/pages/index/Adoption/success' }); // 假设跳转到提交成功页面
    showSubmitConfirmation.value = false;
}
</script>


<style scoped>
.archive-page {
    display: flex;
    flex-direction: column;
    position: relative;
    background-color: #FFFAF0;
    padding-top: 50px;
    height: 100vh;
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

.input-container {
    display: flex;
    align-items: center;
    margin-bottom: 20px;
}

.input-label {
    font-family: 'PingFang SC';
    font-size: 20px;
    color: #604500;
    margin-right: 10px;
}

.input-field {
    width: 270px;
    /* 减小宽度以适应标签 */
    height: 44px;
    background: #FFEAC3;
    border-radius: 10px;
    border: none;
    border-bottom: 1px solid #604500;
    font-family: 'PingFang SC';
    font-size: 20px;
    color: #604500;
    padding-left: 10px;
}

.input-field::placeholder {
    color: #bba36f;
    /* 占位符颜色 */
}



.main-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding-top: 20px;
}

.submit-button {
    position: absolute;
    width: 152px;
    height: 52px;
    left: 111px;
    top: 486px;
    background: #FF9900;
    border-radius: 5px;
    font-family: 'PingFang SC';
    font-size: 24px;
    line-height: 52px;
    text-align: center;
    color: #FFFFFF;
    cursor: pointer;
}

.submit-confirmation {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.4);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1000;
}

.confirmation-box {
    background: #FFFFFF;
    box-shadow: 0px 4px 50px rgba(0, 0, 0, 0.25);
    border-radius: 5px;
    width: 70vw;
    height:40vw;
    display: flex;
    padding-top:5vw;
    flex-direction: column;
}

.confirmation-title {
    font-family: 'PingFang SC';
    font-size: 25px;
    color: #000000;
    text-align: center;
    margin-bottom: 15px;
    font-family: SimHei;
}

.confirmation-message {
    font-family: 'SimHei';
    font-size: 22px;
    padding-left:7vw;
    padding-right: 7vw;
    color: #979797;
    text-align: center;
    margin-bottom: 20px;
}

.confirmation-buttons {
    display: flex;
    justify-content: space-between;
    width:100%;
    height:5vw;
}

.button {
    padding: 0px 0px;
    border-radius: 0px;
    width:50%;
    height:14vw;
    text-align: center;
    justify-content: center;
    align-items: center;
    display: flex;
    font-size: 22px;
}

.cancel-button {
    background-color: #fff;
    border: 1px solid #D8D8D8;
    color: #000000;

}

.confirm-button {
    background-color: #FFFFFF;
    border: 1px solid #D8D8D8;
    color: #1ED700;
}
</style>
