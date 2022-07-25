#!/usr/bin/env python
# encoding: utf-8
# @author:Yuchengyu
# @time: 2022/7/15 0015 10:01

import requests
import re
from collections import OrderedDict


hosts = 'http://47.107.178.45'
session=requests.session()  #创建session 的对象
# 1、进入论坛首页
res01 = session.get(url=hosts + '/phpwind/')
body01=res01.content.decode('utf-8')
csrf_token= re.findall('name="csrf_token" value="(.+?)"/',body01)[1];
# 2、提交用户名和密码的登录信息
get_params={'m':'u',
            'c':'login',
            'a':'dologin'}
form_data={
    'username':'test741963',
    'password':'a2128199',
    'csrf_token':csrf_token,
    'csrf_token':csrf_token

}
# " name="csrf_token" value="c053782985539d17"/></form>
headers={
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With':'XMLHttpRequest',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9'
}
res02=session.post(url=hosts+'/phpwind/index.php',
                    params=get_params,
                    data=form_data,
                    headers=headers
                    )

body02=res02.content.decode('utf-8')
login_id=re.findall('statu=(.+?)"',body02)[0];
# print(login_id)
#登录成功后的跳转
get_params={'m':'u',
            'c':'login',
            'a':'welcome',
            '_statu':login_id}
res03=session.get(url=hosts+'/phpwind/index.php',
                    params=get_params,
                  )
# print(res03.content.decode('utf-8'))

#4、发帖
get_params={
    'c':'post',
    'a':'doadd',
    '_json':'1',
    'fid':'12'
}
headers={
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With':'XMLHttpRequest',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    # 'Content-Type':'multipart/form-data; boundary=----WebKitFormBoundaryPR7KETf8BZFA1WQv',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9'
}
# mul_form_data={
#     'atc_title':'test_012301',
#     'atc_content':'12132312',
#     'pid':'',
#     'tid':'',
#     'special':'default',
#     'reply_notice':1,
#     'csrf_token':csrf_token
# }
mul_form_data=OrderedDict(
    [
        ('atc_title',(None,'test_012131011')),
        ('atc_content',(None,'1231132')),
        ('pid',(None,'')),
        ('tid',(None,'')),
        ('special',(None,'default')),
        ('reply_notice',(None,1)),
        ('csrf_token',(None,csrf_token))
    ]
)
res04=session.post( url = hosts+'/phpwind/index.php',
                    params=get_params,
                    headers=headers,
                    files = mul_form_data
                    )

print(res04.content.decode('utf-8'))