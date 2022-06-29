import requests,json,os

# server酱开关，填off不开启(默认)，填on同时开启cookie失效通知和签到成功通知
sever = os.environ["SERVE"]

# 填入glados账号对应cookie
cookie = os.environ["COOKIE"]

# 企业微信机器人地址
rot_url=os.environ['ROTURL']

def start():
    url= "https://glados.rocks/api/user/checkin"
    url2= "https://glados.rocks/api/user/status"
    referer = 'https://glados.rocks/console/checkin'
    #checkin = requests.post(url,headers={'cookie': cookie ,'referer': referer })
    #state =  requests.get(url2,headers={'cookie': cookie ,'referer': referer})
    origin = "https://glados.rocks"
    useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
    payload={ 
        # 'token': 'glados_network'
        'token': 'glados.network'
    }
    headers={
        'accept':'application/json, text/plain, */*',
        # 'accept-encoding':'gzip, deflate, br',
        'accept-language':'zh-CN,zh;q=0.9,en;q=0.8',
        'sec-ch-ua':'" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
        'sec-ch-ua-mobile':'?0',
        'sec-ch-ua-platform':'"Windows"',
        'sec-fetch-dest':'empty',
        'sec-fetch-mode':'cors',
        'sec-fetch-site':'same-origin',
        'cookie': cookie ,
        'origin':origin,
        'user-agent':useragent,
        'content-type':'application/json;charset=UTF-8'
    }
    checkin = requests.post(url,headers=headers,data=json.dumps(payload))
    state =  requests.get(url2,headers={'cookie': cookie ,'referer': referer,'origin':origin,'user-agent':useragent})
    print(checkin.text,'\n')
    print(state.text)
    headers = {"Content-Type": "application/json;charset=UTF-8"}
    text_data = {"content" : checkin.text}
    req_data = {"msgtype" : "text", "text" : text_data}
    res = requests.request('post', rot_url, data=json.dumps(req_data), headers=headers)
    text_data = {"content" : state.text}
    req_data = {"msgtype" : "text", "text" : text_data}
    res = requests.request('post', rot_url, data=json.dumps(req_data), headers=headers)

    # if sever == 'on':
    #     robot_msg=None
    #     if 'message' in checkin.text:
    #         mess = checkin.json()['message']
    #         time = state.json()['data']['leftDays']
    #         time = time.split('.')[0]
    #         print(time)
    #         robot_msg = mess+'，you have '+time+' days left'
    #     else:
    #         robot_msg='cookie过期'
    #     headers = {"Content-Type": "application/json;charset=UTF-8"}
    #     text_data = {"content" : robot_msg}
    #     req_data = {"msgtype" : "text", "text" : text_data}
    #     res = requests.request('post', rot_url, data=json.dumps(req_data), headers=headers)

def main_handler(event, context):
  return start()

if __name__ == '__main__':
    start()

    
