{
    header = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '955',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        // 非必要请勿启用
        // 'Cookie': '', 
        'Host': '172.16.3.19',
        'Origin': 'http://172.16.3.19',
        // 填入你的请求头中的数据
        'Referer': '',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
    }

    "dataLogin": {
    // 以下内容从Post请求中获取，密码填写加密后的密码
      "userId": "你的账号",
      "password": "加密后的密码",
      "service": "网络接入方式",
      "queryString": "queryString",
    //   不用填写以下内容
      "operatorPwd": "",
      "operatorUserId": "",
      "validcode": "",
      "passwordEncrypt": "true",
    //   填写Post内容
      "userIndex": "userIndex"
    },
    "dataCheck": {
    //   填写Post内容
      "userIndex": "userIndex"
    },
    "loginUrl": "http://172.16.3.19/eportal/InterFace.do?method=login",
    "checkStatusUrl": "http://172.16.3.19/eportal/InterFace.do?method=getOnlineUserInfo"
  }
  