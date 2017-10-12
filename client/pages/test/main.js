// pages/test/main.js
Page({
	data: {
		list: [
			{ // 学校
				"id": 1,
				"name": "华中科技大学",
				"coords": {
					"x": 114.419826,
					"y": 30.518754
				},
				"people": [
					{
						"id": 1,
						"name": "张三",
						"duration": [9, 11, 12, 15]
					}
				]
			}
		],
		markers: [{
			iconPath: "/resources/others.png",
			id: 0,
			latitude: 23.099994,
			longitude: 113.324520,
			width: 50,
			height: 50
		}],
		polyline: [{
			points: [{
				longitude: 113.3245211,
				latitude: 23.10229
			}, {
				longitude: 113.324520,
				latitude: 23.21229
			}],
			color: "#FF0000DD",
			width: 2,
			dottedLine: true
		}],
		controls: [{
			id: 1,
			iconPath: '/resources/location.png',
			position: {
				left: 0,
				top: 300 - 50,
				width: 50,
				height: 50
			},
			clickable: true
		}]
	},
	regionchange(e) {
		console.log(e.type)
	},
	markertap(e) {
		console.log(e.markerId)
	},
	controltap(e) {
		console.log(e.controlId)
	},

	onLoad: function (options) {

	},

	onReady: function () {

	},

	onShow: function () {

	},

	onHide: function () {

	},

	onUnload: function () {

	},

	onPullDownRefresh: function () {

	},

	onShareAppMessage: function () {

	}
})