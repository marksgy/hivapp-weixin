var svr = require("utils/server.js")

App({
  globalData: {
  },
  user: {
    login: function () {
      var self = this
      wx.login({
        success: function (loginRes) {
          console.log(loginRes)
          if (loginRes.code) {
            wx.getUserInfo({
              success: function (res) {
                svr.http.get("/login", true,
                  function (payload) {
                    wx.setStorageSync("player_login_token", payload);
                  },
                  { code: loginRes.code, encrypted_data:
                  res.encryptedData, iv: res.iv }
                );
              }
            });
          } else {
            console.log("获取用户登录态失败！" + loginRes.errMsg)
          }
        }
      })
    },
    getToken: function () {
      return wx.getStorageSync("user_login_token")
    },
    refresh: function () {
      wx.removeStorageSync("user_login_token")
      this.login()
    },
    loadCurrentUser: function () {
      svr.http.get("/server/publics/auth/user?fields=detail", false,
        function (payload) {
          var u = wx.getStorageSync("user_login_token")
          u.user = payload
          wx.setStorageSync("user_login_token", u)
        }
      )
    }
  },

  onLaunch: function () {
    var self = this
    self.user.login()
    // wx.checkSession({
    //   success: function () {
    //     if (!self.user.getToken()) {
    //       self.user.login()
    //     } else {
    //       self.user.loadCurrentUser()
    //     }
    //   },
    //   fail: function () {
    //     self.user.login()
    //   }
    // })
  }
})