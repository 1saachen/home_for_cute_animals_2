<template>
    <view class="container">
        <view class="detail-section">
            <image class="animal-photo" :src="application.photoUrl"></image>
            <view class="info">
                <text class="name">名字：{{ application.name }}</text>
                <text class="time">申请时间：{{ application.time }}</text>
                <text class="status"
                    :class="{ 'approved': application.status === 'approved', 'rejected': application.status === 'rejected', 'pending': application.status === 'pending' }">审核状态：{{
                        statusText(application.status) }}</text>
            </view>
        </view>
        <button v-if="application.status === 'pending'" class="revoke-btn" @click="revokeApplication">撤销申请</button>
    </view>
</template>

<script>
export default {
    data() {
        return {
            application: {}
        };
    },
    onLoad(option) {
        const { id } = option;
        // 根据id获取领养申请详情，这里使用示例数据
        this.application = {
            id,
            name: '小白',
            time: '2024-01-01',
            status: 'pending',
            photoUrl: '/static/sample-dog.jpg'
        };
    },
    methods: {
        statusText(status) {
            switch (status) {
                case 'pending':
                    return '正在审核';
                case 'approved':
                    return '审核通过';
                case 'rejected':
                    return '审核不通过';
                default:
                    return '未知状态';
            }
        },
        revokeApplication() {
            // 实现撤销申请的逻辑，可能需要调用后端接口
            console.log('撤销申请');
            uni.showModal({
                title: '提示',
                content: '确定要撤销这条申请吗？',
                success: res => {
                    if (res.confirm) {
                        console.log('用户点击确定');
                        // 执行撤销操作，成功后返回上一页
                        uni.navigateBack();
                    }
                }
            });
        }
    }
}
</script>

<style scoped>
.container {
    padding: 20px;
}

.detail-section {
    display: flex;
    margin-bottom: 20px;
}

.animal-photo {
    width: 100px;
    height: 100px;
    margin-right: 20px;
}

.info {
    flex-grow: 1;
}

.name,
.time,
.status {
    margin-bottom: 10px;
}

.approved {
    color: green;
}

.rejected {
    color: red;
}

.pending {
    color: orange;
}

.revoke-btn {
    background-color: #FF3B30;
    color: white;
}
</style>
