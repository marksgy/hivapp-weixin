function formatTime(date) {
	var formatNumber = function (n) {
		n = n.toString()
		return n[1] ? n : '0' + n
	}

	var year = date.getFullYear()
	var month = date.getMonth() + 1
	var day = date.getDate()

	var hour = date.getHours()
	var minute = date.getMinutes()
	var second = date.getSeconds()

	return [year, month, day].map(formatNumber).join('-') + ' ' + [hour, minute, second].map(formatNumber).join(':')
}

function page(fetchFunc, size, setFunc) {
	var page = {
		lastPayload: null, elements: [], loading: false,

		_load: function (page) {
			if (this.loading) {
				return;
			}
			this.loading = true;
			var self = this;
			fetchFunc(page, size,
				function (payload) {
					self.lastPayload = payload;
					self.elements = self.elements.concat(payload.content);
					self.loading = false;
					setFunc(self);
				},
				self.elements.length == 0);
		},
		next: function () {
			if (this.hasNext()) {
				this._load(this.lastPayload.number + 1);
			}
		},
		hasNext: function () {
			return this.lastPayload != null ? !this.lastPayload.last : false;
		}
	};
	page._load(0);
	return page;
}

function redirectTo(currentPages, url) {
	console.log(currentPages);
	var routeUrl = null;
	if (url.indexOf("/") == 0) {//绝对路径
		routeUrl = url.substring(1);
	} else {//相对路径
		var currentRoute = currentPages[currentPages.length - 1].__route__;
		var lastSlashIndex = currentRoute.lastIndexOf("/");
		if (lastSlashIndex == -1) {//当前为根目录
			routeUrl = url;
		} else {//当前为子目录，截取子目录路径，再拼装相对路径
			routeUrl = currentRoute.substring(0, lastSlashIndex + 1) + url;
		}
	}
	var samePageIdx = null;
	for (var i = 0; i < currentPages.length; i++) {
		if (currentPages[i].__route__ == routeUrl) {
			samePageIdx = i;
			break;
		}
	}
	if (samePageIdx != null) {
		wx.navigateBack({ delta: currentPages.length - 1 - samePageIdx });
	} else {
		var tabBarList = ["pages/my/b5f", "pages/exam/list", "pages/my/main"], isTabBar;
		for (var i = 0, len = tabBarList.length; i < len; i++) {
			if (tabBarList[i] == routeUrl) {
				isTabBar = true;
				break;
			}
		}
		if (isTabBar) {
			wx.switchTab({ url: "/" + routeUrl });
		} else {
			wx.redirectTo({ url: url });
		}
	}
}

module.exports = {
	formatTime: formatTime,
	page: page,
	redirectTo: redirectTo
}
