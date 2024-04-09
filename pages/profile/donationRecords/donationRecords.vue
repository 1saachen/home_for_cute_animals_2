<template>
    <view class="container">
        <image src="/static/qiandai.png" class="background-pic"/>
        <view class="header">
                <!-- 返回按钮 -->
                <view class="back-button" @click="goBack">
                    <image src="/static/fanhui.png" class="back-icon" />
                </view>
                <view class="archive-title">
                    捐赠记录
                </view>
            </view>
         <view class="donation-item" v-for="(record, index) in donationRecords" :key="index">
            <view class="icons"></view>    
            <view class="head">
                    <view class="title-box"><text class="title">{{ record.projectTitle }}</text></view>
                    <view class="date-box"><text class="date">{{ record.time }}</text></view>
                    
                    
                </view>
                <view class="content">
                    <view class="amount-section">
                        <view class="amount-box"><text class="amount">{{ record.amount }}</text></view>
                        <view class="label-box"><text class="label">捐赠金额（元）</text></view>
                        
                        
                    </view>
                    <view class="status-box">
                        <text class="status" :class="{ 'completed': record.status === 'completed', 'failed': record.status === 'failed' }">{{ statusText(record.status) }}</text>
                    </view>
                    
                </view>
            </view>
    </view>
</template>

<script>
export default {
    data() {
        return {
            donationRecords: [
                // 示例数据
                { id: 1, projectTitle: '救助流浪猫', time: '2024-2-9 12:20:41', amount: 100.00, status: 'completed' },
                { id: 2, projectTitle: '流浪狗疫苗接种', time: '2024-2-10 12:26:41', amount: 200.00, status: 'completed' },
                // 可以添加更多捐赠记录
            ]
        };
    },
    methods: {
        goBack() {
            uni.navigateBack(); // 实现返回上一页
        },
        statusText(status) {
            if (status === 'completed') {
                return '捐赠成功';
            } else if (status === 'failed') {
                return '捐赠失败';
            } else {
                return '处理中';
            }
        }
    }
}
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

.background-pic{
    position:absolute;
    width:60vw;
    height:35vh;
    left:20vw;
    top:30vh;
}
.container {
    display: flex;
    flex-direction: column;
    position: relative;
    background-color: #ffedbe;
    height:95vh;
    top:5vh;
}

.donation-item {
   width: 86vw;
   height:15vh;
    margin-right: 2vw;
    background: #FFFFFF;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 0px 40px 20px 20px;
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 10px;
    padding: 15rpx 0;
    position: relative;
    opacity: 0.9;
    margin-top: 2vh;
    margin-left: 3vh;
    
}
.icons{
        position: absolute;
        width: 30rpx;
        height: 30rpx;
        background: #ffedbe;
        border-radius: 50%;
        left: 10px;
    }
.donation-item .head {

    padding-top: 2px;
}

.donation-item .content {
    display: flex;
    flex-direction: row;
    padding: 10px;
}

.head{
    display: flex;
    justify-content: space-between;
    width: 72vw;
    padding: 0px 10px;
    padding-left:10vw;
    border-bottom: 0.5px solid #604500;
}

.title-box {
    font-family: 'SimHei';
    font-size: 15px;
    color: #604500;
    margin-left:0vw;
    text-align: left;
}

.date-box {
    font-family: 'PingFang SC';
    font-size: 12px;
    color: #979797;
    text-align: right;
}

.content{
    display:flex;
    justify-content: space-between;
    width:90%;
    margin-left:5vw;
}

.amount-section {
    display: flex;
    flex-direction: column;
    left:10vw;
}

.amount {
    font-family: 'PingFang SC';
    font-size: 30px;
    color: #604500;
}

.amount-box{
    margin-top: 2vh;
    margin-left: 0vw;

}

.label {
    font-family: 'SimHei';
    font-size: 12px;
    color: #604500;
}

.status-box {
    font-family: 'SimHei';
    font-size: 18px;
    text-align: center;
    background-color: #ffde8a;
    width:124px;
    height:35px;
    border-radius:12px 0px 0px 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-right: -2vw;
    margin-top: 3vh;
}

.completed {
    color: green;
}

.failed {
    color: red;
}
</style>
