<!-- ### 教程
https://blog.csdn.net/weixin_37551036/article/details/115415358 -->
<!-- # glados-checkin
![glados-checkin](https://github.com/hbstarjason/glados-checkin/workflows/glados-checkin/badge.svg)

<img src="https://img.shields.io/github/stars/talkzhang/glados-signin" alt="stars" /> -->

#### 注册地址：

1、打开 https://github.com/glados-network/GLaDOS ，找到[<u>***Register***</u>]，打开链接，填写邮箱进行登录。

2、输入激活码`QUT5C-7EQF9-RVBX0-WO5VG`，进行激活，获得3天试用。

3、每天手动进行checkin一次，能增加一天。

4、该脚本就是让你无需每天挂念去手动签到，自动完成glados签到，并支持企业微信推送。



#### 脚本功能：

1、通过Github Action自动定时运行[checkin.py](https://github.com/talkzhang/glados-signin/blob/master/checkin.py)脚本。

2、通过cookies自动登录（[https://glados.rocks/console/checkin](https://glados.rocks/console/checkin))，脚本会自动进行checkin。

3、然后通过企业微信群聊中机器人，自动发通知到企业微信上，由于一个人无法建群，可以先请两三个好友建群后好友退出即可。

#### 食用姿势：

1. 先“Fork”本仓库。（不需要修改任何文件！）

2. 注册GLaDOS，方法见上。

3. 登录GLaDOS后获取cookies。（简单获取方法：浏览器快捷键F12，打开调试窗口，点击“network”获取）

4. 在自己的仓库“Settings”里创建3个“Secrets”，分别是：（不开启通知，只需要创建一个COOKIE即可）

   - COOKIE（**必填**）
   - SERVE（企业微信通知开关，默认是off，填on的话，会同时开启cookie失效通知和签到成功通知）
   - ROTURL（填写企业微信机器人webhook地址，不开启企业微信通知则不用填）

5. 以上设置完毕后，每天10:50、14：50会自动触发，并会执行自动checkin，如果开启企业微信通知，会自动发通知到企业微信上。

6. **如果以上都不会的话，注册GLaDOS后，每天勤奋点记得登录后手动进行checkin即可。**

   [*<u>如果是Edu邮箱，可免费升级为360天。</u>*]
