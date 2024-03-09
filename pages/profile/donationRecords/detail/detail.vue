<template>
    <view class="container">
        <view class="detail-section">
            <text class="title">捐赠项目：{{ donationDetail.projectTitle }}</text>
            <text class="time">捐赠时间：{{ donationDetail.time }}</text>
            <text class="amount">捐赠金额：￥{{ donationDetail.amount }}</text>
            <text class="message">捐赠留言：{{ donationDetail.message }}</text>
            <!-- 其他捐赠详情 -->
        </view>
    </view>
</template>

<script>
export default {
    data() {
        return {
            donationDetail: {}
        };
    },
    onLoad(option) {
        const { id } = option;
        // 根据id获取捐赠详情，这里使用示例数据
        this.donationDetail = {
            id,
            projectTitle: '救助流浪猫',
            time: '2024-01-01',
            amount: 100,
            message: '希望能为流浪猫提供更好的生活条件。',
            // 其他详情
        };
    }
}
</script>

<style scoped>
.container {
    padding: 20px;
}

.detail-section {
    display: flex;
    flex-direction: column;
}

.title,
.time,
.amount,
.message {
    margin-bottom: 10px;
}
</style>
