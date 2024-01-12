header = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '955',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 非必要请勿启用
    # 'Cookie': '',
    'Host': '172.16.3.19',
    'Origin': 'http://172.16.3.19',
    # 以下数据填写Post请求中的内容
    'Referer': '填写Post请求中的内容',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
}

dataLogin = {
    # 以下内容从Post请求中获取，密码填写加密后的密码
    'userId': '账号',
    'password': '加密后的密码',
    'service': '运营商网络',    # 例如`dianxin` `yidong`
    'queryString': '从Post请求中获取',
    # 不用填写以下内容
    'operatorPwd': '',
    'operatorUserId': '',
    'validcode': '',
    # 填写的是否为加密密码
    'passwordEncrypt': 'true', # 如果密码未加密，更改为'false'
    # 填写Post内容
    'userIndex': '从Post请求中获取'
}

dataCheck = {
    # 填写Post内容
    'userIndex': '从Post请求中获取'
}

# 填写登录界面URL，以下默认是宜宾学院登录地址。如需修改，建议用批量字符串替换功能替换项目所有IP
loginUrl = 'http://172.16.3.19/eportal/InterFace.do?method=login'
checkStatusUrl = 'http://172.16.3.19/eportal/InterFace.do?method=getOnlineUserInfo'
