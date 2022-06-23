> GLaDOS是一个可以让你科学上网的vpn网站。

#### 注册地址：

1、打开 https://github.com/glados-network/GLaDOS ，找到[***Register*** ]，打开链接，填写邮箱进行登录。

2、输入激活码 `QUT5C-7EQF9-RVBX0-WO5VG`，进行激活，获得3天试用。

3、每天手动进行checkin一次，能增加一天。

4、该脚本就是让你无需每天挂念去手动签到，自动完成glados签到，并支持企业微信推送。

#### 脚本功能：

1、通过Github Action自动定时运行[checkin.py](https://github.com/talkzhang/glados-signin/blob/master/checkin.py)脚本。

2、通过cookies自动登录（[https://glados.rocks/console/checkin](https://glados.rocks/console/checkin))，脚本会自动进行checkin。

3、然后通过企业微信群聊中机器人，自动发通知到企业微信上，由于一个人无法建群，可以先请两三个好友建群后好友退出即可。

#### 食用姿势：

##### 1.、先“Fork”本仓库。（不需要修改任何文件！）

![](https://cdn.jsdelivr.net/gh/talkzhang/imgs-bed@master/image/20220622184524.png)

##### 2、 注册GLaDOS，方法见上。

##### 3、 登录GLaDOS后获取cookies

这一步很重要，相当于获取你账户的身份，cookies信息用于后面**配置到github的actions信息内**。

简单获取方法：

1、 打开浏览器，https://glados.rocks/console/account，我的账户页面。

![](https://cdn.jsdelivr.net/gh/talkzhang/imgs-bed@master/image/20220622184913.png)

2、浏览器快捷键F12，打开调试窗口

![](https://cdn.jsdelivr.net/gh/talkzhang/imgs-bed@master/image/20220622185105.png)

点击这个***account***：

![](https://cdn.jsdelivr.net/gh/talkzhang/imgs-bed@master/image/20220622185253.png)

把这个***cookie***的值复制下来，等下会用。

##### 4、配置Secrets

在自己的仓库 `Settings`里可以支持创建3个 `Secrets`，分别是：（如果不开启通知，只需要创建一个COOKIE即可）

- COOKIE（**必填**）
- SERVE（企业微信通知开关，默认是off，填on的话，会同时开启cookie失效通知和签到成功通知）
- ROTURL（填写企业微信机器人webhook地址，不开启企业微信通知则不用填）

![](https://cdn.jsdelivr.net/gh/talkzhang/imgs-bed@master/image/20220623102830.png)

Name和value都懂吧，就是上面说的三个，可以只填一个COOKIE，但那样的话不支持企业微信通知。如果三个都需要填写的，就new三次，即填写三次name和value。

##### 4、利用actions定时签到

![](https://cdn.jsdelivr.net/gh/talkzhang/imgs-bed@master/image/20220623103247.png)

Actions->All workflows->glados-checkin->Enable workflow，开启该workflow即可。

1. 以上设置完毕后，每天10:50、14：50（大概推算时间，具体以实际为准，因为actions执行依靠队列、时间区等因素）会自动触发，并会执行自动checkin，如果开启企业微信通知，会自动发通知到企业微信上。
2. **如果以上都不会的话，注册GLaDOS后，每天勤奋点记得登录后手动进行checkin即可。**

   [***如果是Edu邮箱，可免费升级为360天。***]

参考原链接地址：[https://github.com/hbstarjason/glados-checkin](https://github.com/hbstarjason/glados-checkin)
