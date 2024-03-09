<template>
  <view class="archive-page">
    <view class="bar" :style="{ 'margin-top': statusBarHeight + 'px', 'height': navBarHeight + 'px' }">
      <view class="back-button" @click="goBack">
        <image src="/static/fanhui.png" class="back-icon" />
      </view>
      <view class="search-bar" @click="goToSearch">
        <uni-search-bar v-model="keyword" placeholder="搜索" radius="15" clearbutton="none"></uni-search-bar>
      </view>
    </view>
    <view class="top-nav">
      <view class="nav-item" @click="filterCategory('onCampus')">
        <image src="../../static/weizhi.png" class="img"></image>
        <text :class="activeNav == 'onCampus' ? 'active' : ''">在校</text>
      </view>
      <view class="nav-item" @click="filterCategory('adopted')">
        <image src="../../static/103.png" class="img"></image>
        <text :class="activeNav == 'adopted' ? 'active' : ''">领养</text>
      </view>
      <view class="nav-item" @click="filterCategory('starCats')">
        <image src="../../static/104.png" class="img"></image>
        <text :class="activeNav == 'starCats' ? 'active' : ''">喵星</text>
      </view>
    </view>
    <view class="main-content">
      <view class="sidebar">
        <view class="department-item" @click="filterDepartment('liberalArts')">
          <image src="/static/weizhi.png" class="department-icon" />
          <text :class="activeName == 'liberalArts' ? 'active' : ''">文理学部</text>
        </view>
        <view class="department-item" @click="filterDepartment('informatics')">
          <image src="/static/weizhi.png" class="department-icon" />
          <text :class="activeName == 'informatics' ? 'active' : ''">信息学部</text>
        </view>
        <view class="department-item" @click="filterDepartment('engineering')">
          <image src="/static/weizhi.png" class="department-icon" />
          <text :class="activeName == 'engineering' ? 'active' : ''">工学部</text>
        </view>
        <view class="department-item" @click="filterDepartment('medical')">
          <image src="/static/weizhi.png" class="department-icon" />
          <text :class="activeName == 'medical' ? 'active' : ''">医学部</text>
        </view>
      </view>
      <scroll-view class="record-list" scroll-y="true">
        <view class="animal-list-container">
          <view class="animal-card" v-for="(animal, index) in animals" :key="index">
            <view class="icons"></view>
            <view class="image-container">
              <image :src="animal.image" class="animal-image" />
              <text class="animal-name">{{ animal.name }}</text>
            </view>
            <view class="details-button" @click="viewDetails(animal)">
              <text>查看详情 ></text>
            </view>
          </view>
        </view>
      </scroll-view>
    </view>
  </view>
</template>


<script setup>
import { ref, onMounted } from 'vue';

const statusBarHeight = ref(0);
const navBarHeight = ref(0);
const activeName = ref('liberalArts');
const activeNav = ref('onCampus');
const keyword = ref('');
const animals = ref([
  {
    name: '蛋白',
    image: '/static/蛋白.png',
    id: '1',
  },
  {
    name: '蛋白',
    image: '/static/蛋白.png',
  },
  // ...其他动物数据
]);

function goBack() {
  uni.navigateBack(); // 实现返回上一页
}

function goToSearch() {
  uni.navigateTo({
    url: '/pages/index/Profile/search',
  }); // 实现跳转到搜索页
}


function filterCategory(category) {
  activeNav.value = category;
}

function filterDepartment(department) {
  activeName.value = department;
}

function viewDetails(animal) {
  uni.navigateTo({
    url: `/pages/index/Profile/detail1?id=${animal.id}`,
  });
}

onMounted(() => {
  if (uni.canIUse('getMenuButtonBoundingClientRect')) {
    const sysInfo = uni.getSystemInfoSync();
    statusBarHeight.value = sysInfo.statusBarHeight;
    const rect = uni.getMenuButtonBoundingClientRect();
    navBarHeight.value = (rect.top - sysInfo.statusBarHeight) * 2 + rect.height;
  } else {
    uni.showToast({
      title: '您的微信版本过低，界面可能会显示不正常',
      icon: 'none',
      duration: 4000,
    });
  }
});
</script>


<style scoped lang="scss">
.archive-page {
    display: flex;
    flex-direction: column;
    position: relative;
    background-color: #fceec5;
    /* 页面背景色 */

    .bar {
        display: flex;
        align-items: center;
        background: #fceec5;
        padding-bottom: 10rpx;
    }

    .search-bar {
        width: 65%;

    }

    .back-button {
        width: 10%;
    }
}

.back-icon {
    width: 30px;
    height: 30px;

}

.search-input {
    width: 100%;
    border-radius: 15px;
    border: none;
    padding: 10px;
    font-size: 16px;
}

.top-nav {
    display: flex;
    justify-content: space-around;
    background-color: #FBDE95;
    /* 导航栏背景色 */
    padding: 10px 0;
    top: 20vh;
}

.nav-item {
    color: #604500;
    /* 文字颜色 */
    font-weight: bold;
    display: flex;
    align-items: center;

    .img {
        margin-right: 8rpx;
        width: 30rpx;
        height: 30rpx;
    }
}

.main-content {
    display: flex;
    height: 100vh;
}

.sidebar {
    // flex: 0 0 20vw;
    width: 22vw;
    background-color: #fefbed;
    /* 侧边栏背景色 */
    padding: 20px 10px;
}

.department-item {
    display: flex;
    align-items: center;
    margin-bottom: 20px;
    /* 间隔 */
}

.department-icon {
    width: 20px;
    height: 20px;
    margin-left: 0vw;
}

.record-list {
    flex: 1;
    padding: 10px;
}

.record-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    background-color: #FFFFFF;
    border-radius: 20px;
}

.animal-list-container {
    display: flex;
    flex-wrap: wrap;
}

.animal-card {
    width: calc((100vw - 22vw - 40px - 2vw) / 2);
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

    &:nth-child(2n) {
        margin-right: 0;
    }

    .icons {
        position: absolute;
        width: 16rpx;
        height: 16rpx;
        background: #FFDE8A;
        border-radius: 50%;
        left: 10px;
    }
}

.image-container {
    // background: url(image.png);
    width: 30vw;
    height: 30vw;
    margin-top: 0vw;
    border-radius: 50%;
    position: relative;
}

.animal-image {
    width: 100%;
    height: 100%;
}

.animal-name {
    position: absolute;
    background: #FFDE8A;
    border-radius: 0px 12px 12px 0px;
    font-family: 'PingFang SC';
    font-size: 14px;
    font-weight: bold;
    width: 150rpx;
    overflow: hidden;
    line-height: 50rpx;
    text-align: center;
    color: #604500;
    bottom: -30rpx;
    left: -10rpx;
    /* Adjust as needed */
    z-index: 10;
}

.details-button {
    font-family: SimHei;
    font-size: 14px;
    line-height: 20px;
    text-align: center;
    color: #604500;
    margin: 46rpx -10vw 0 0;
    /* Adjust as needed */
    cursor: pointer;
}

.active {
    color: #f19747;
}
</style>