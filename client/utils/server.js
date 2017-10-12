var env = "https://39927783.qcloud.la";

/**
 * 处理Http错误
 */
function handleHttpError(data, status, onError) {
	var msg = null;
	if (onError != null) {
		msg = onError(data, status, headers);
	} else if (status == 401) {
		getApp().user.refresh();
		msg = "用户登录信息已过期，请重新打开页面";
	} else if (status == 403) {
		msg = "您无权执行该操作，请联系系统管理员";
	} else if (status >= 400) {
		msg = "服务器抑郁了，罢工一小会儿~[" + status + "]";
	}
	if (msg != null) {
		wx.showModal({ title: "服务器通信故障", content: msg, showCancel: false });
	}
}
/**
 * 处理服务器结果，result为服务器返回的data对象
 */
function handleServerResult(result, onSuccess, onFailure) {
	if (result.success) {// 结果正常则调用onSuccess回调
		// onSuccess为success:true时的回调，参数为payload；
		onSuccess(result.payload);
	} else if (onFailure == null) {// 结果不正常且没有onError则直接提示errorMessage
		wx.showModal({ title: "业务处理失败", content: result.errorMessage, showCancel: false });
	} else {// 结果不正常且有onError则执行onError
		// onError为success:false时的回调，参数为errorCode,errorMessage
		onFailure(result.errorCode, result.errorMessage);
	}
}

function start(foreground) {
	if (foreground) {
		if (typeof foreground == "function") {
			foreground(true);
		} else {
			wx.showToast({ title: '加载中', icon: "loading", mask: true, duration: 10000 });
		}
	}
	var ult = getApp().user.getToken();
	return ult != null ? { Cookie: "user_token=" + ult.id } : null;
}

function stop(foreground) {
	if (foreground) {
		if (typeof foreground == "function") {
			foreground(false);
		} else {
			wx.hideToast();
		}
	}
}

var http = {
	get: function (url, foreground, onSuccess, data, onFailure, onError) {
		var header = start(foreground);
		wx.request({
			url: env + url, header: header, data: data,
			success: function (res) {
				if (res.statusCode == 200) {
					handleServerResult(res.data, onSuccess, onFailure);
				} else {
					handleHttpError(res.data, res.statusCode, onError);
				}
			},
			fail: function (res) {
				console.log(res);
			},
			complete: function () {
				stop(foreground);
			}
		});
	},
	post: function (url, foreground, onSuccess, data, onFailure, onError) {
		var header = start(foreground);
		wx.request({
			url: env + url, method: "POST", header: header, data: data,
			success: function (res) {
				if (res.statusCode == 200) {
					handleServerResult(res.data, onSuccess, onFailure);
				} else {
					handleHttpError(res.data, res.statusCode, onError);
				}
			},
			complete: function () {
				stop(foreground);
			}
		});
	},
	put: function (url, foreground, onSuccess, data, onFailure, onError) {
		var header = start(foreground);
		wx.request({
			url: env + url, method: "PUT", header: header, data: data,
			success: function (res) {
				if (res.statusCode == 200) {
					handleServerResult(res.data, onSuccess, onFailure);
				} else {
					handleHttpError(res.data, res.statusCode, onError);
				}
			},
			complete: function () {
				stop(foreground);
			}
		});
	},
	delete: function (url, foreground, onSuccess, data, onFailure, onError) {
		var header = start(foreground);
		wx.request({
			url: env + url, method: "DELETE", header: header, data: data,
			success: function (res) {
				if (res.statusCode == 200) {
					handleServerResult(res.data, onSuccess, onFailure);
				} else {
					handleHttpError(res.data, res.statusCode, onError);
				}
			},
			complete: function () {
				stop(foreground);
			}
		});
	}
};

module.exports = { http: http };