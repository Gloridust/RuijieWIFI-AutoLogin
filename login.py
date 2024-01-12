import requests
import time
import random
import config  # 导入配置文件

# 从配置文件中获取数据
dataLogin = config.dataLogin
dataCheck = config.dataCheck
loginUrl = config.loginUrl
checkStatusUrl = config.checkStatusUrl
header = config.header  # 请求头信息

def check_and_login():
    """
    检查当前在线状态，并根据状态执行相应的操作。
    如果当前处于离线状态，尝试登录。
    """
    # 检查在线状态
    response = requests.post(url=checkStatusUrl, headers=header, data=dataCheck)
    response.encoding = 'utf-8'
    content = response.text.encode().decode("unicode_escape").encode('raw_unicode_escape').decode()
    status_index = content.find('"result":"')

    # 根据状态执行操作
    if content[status_index + 10:status_index + 14] == 'wait' or content[status_index + 10:status_index + 17] == 'success':
        print(time.asctime(time.localtime(time.time())), "当前处于在线状态。")
    else:
        print(time.asctime(time.localtime(time.time())), "当前已经下线，正在尝试登录！")
        # 尝试登录
        login_response = requests.post(url=loginUrl, headers=header, data=dataLogin)
        login_response.encoding = 'utf-8'
        login_content = login_response.text.encode().decode("unicode_escape").encode('raw_unicode_escape').decode()
        result_index = login_content.find('"result":"')

        # 检查登录结果
        if login_content[result_index + 10:result_index + 17] == 'success':
            print(time.asctime(time.localtime(time.time())), "登录成功！")

while True:
    try:
        check_and_login()
    except Exception as e:
        print(time.asctime(time.localtime(time.time())), "监测出错，请检查网络是否连通。", str(e))
        time.sleep(1)
        continue
    time.sleep(random.randint(30, 60))
