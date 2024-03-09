<template>
    <view class="archive-page">
        <!-- 返回按钮 -->
        <view class="header">
            <!-- 返回按钮 -->
            <view class="back-button" @click="goBack">
                <image src="/static/fanhui.png" class="back-icon" />
            </view>
            <view class="archive-title">

                我的领养申请
                <!-- <text class="title">萌物档案</text> -->
            </view>
        </view>

        <!-- 搜索栏 -->
        <view class="box" hover-class="boxHover">
            <view class="inner" hover-class="innerHover">
                此区域还未开放
            </view>
        </view>
    </view>
</template>

<script>
export default {
    data() {
        return {
            records: [], // 动物档案数据
        };
    },
    methods: {
        navigateBack() {
            uni.navigateBack(); // 实现返回上一页
        },
        goToSearch() {
            uni.navigateTo({ url: '/pages/search/search' }); // 实现跳转到搜索页
        },
        filterCategory(category) {
            // 根据顶部分区导航过滤档案
        },
        filterDepartment(department) {
            // 根据侧边栏学部分区过滤档案
        },
        viewDetails(record) {
            // 查看动物详细信息
            // 可以将record的信息作为参数传递
            uni.navigateTo({ url: `/pages/detail/detail?id=${record.id}` });
        },
    },
    mounted() {
        // 加载动物档案数据
        this.loadRecords();
    },
    methods: {
        loadRecords() {
            // 实现加载动物档案数据的逻辑
        },
        goBack() {
            uni.navigateBack(); // 实现返回上一页
        },
    }
};
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
    height: 95vh;
    top: 5vh;
}

.box {
    width: 60vw;
    height: 100px;
    position: absolute;
    top: 45%;
    left: 25vw;
    margin: 5px;
    font-size: 30px;
}
</style>
