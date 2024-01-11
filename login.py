import requests
import time

# 登录URL - 需要根据实际情况进行调整
login_url = "http://172.16.3.19/eportal/InterFace.do?method=login"

# 登录所需的数据 - 根据实际表单进行调整
login_data = {
    "userId": "你的用户名",
    "password": "你的密码",
    "service": "选择的服务（如果有的话）",
    # 其他可能需要的字段...
}

# 设置请求头，模拟浏览器
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

while True:
    try:
        # 发送POST请求进行登录
        response = requests.post(login_url, data=login_data, headers=headers)

        # 检查是否登录成功
        if response.status_code == 200:
            print("登录成功")
        else:
            print("登录失败，状态码：", response.status_code)
    except Exception as e:
        print("出错了：", e)

    # 等待时间
    time.sleep(3)
