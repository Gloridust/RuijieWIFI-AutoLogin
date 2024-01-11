import requests
import time
import random
import json

# 加载配置文件
def load_config(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

config = load_config('config.json')  # config文件路径

dataLogin = config['dataLogin']
dataCheck = config['dataCheck']
loginUrl = config['loginUrl']
checkStatusUrl = config['checkStatusUrl']

def work():
    res1 = requests.post(url=checkStatusUrl, headers=header, data=dataCheck)
    res1.encoding = 'utf-8'
    content = str(res1.text.encode().decode("unicode_escape").encode('raw_unicode_escape').decode())
    i = content.find('"result":"')
    if content[i + 10:i + 14] == 'wait' or content[i + 10:i + 17] == 'success':
        print(time.asctime(time.localtime(time.time())), "当前处于在线状态。")
    else:
        print(time.asctime(time.localtime(time.time())), "当前已经下线，正在尝试登录！")
        res2 = requests.post(url=loginUrl, headers=header, data=dataLogin)
        res2.encoding = 'utf-8'
        content2 = str(res2.text.encode().decode("unicode_escape").encode('raw_unicode_escape').decode())
        j = content2.find('"result":"')
        if content2[j + 10:j + 17] == 'success':
            print(time.asctime(time.localtime(time.time())), "登录成功！")

while True:
    try:
        work()
    except Exception as e:
        print(time.asctime(time.localtime(time.time())), "监测出错，请检查网络是否连通。", str(e))
        time.sleep(1)
        continue
    time.sleep(random.randint(30, 60))
