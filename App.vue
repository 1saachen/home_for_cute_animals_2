<script>
  export default {
    onLaunch: function() {
      console.log('App Launch');
      //获取openid、UnionID、session_key
      uni.login({
        provider: 'weixin',
        success: function(loginRes) {
          if (loginRes.code) {
            // 在这里请求后端接口
          }
        }
      });
    },
    onShow: function() {
      console.log('App Show');
    },
    onHide: function() {
      console.log('App Hide');
    },
  };
</script>

<style>
  /*每个页面公共css */
</style>