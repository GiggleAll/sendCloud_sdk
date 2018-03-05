#!/usr/bin/env python
# -*- coding:utf-8 -*
try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+

import requests

url = "http://api.sendcloud.net/apiv2/mail/send"

API_USER = 'zhichaozhang_test_ZGnoAq'
API_KEY = 'LJB2mqIGvht2FzHo'

params = {
    "apiUser": API_USER,  # 使用api_user和api_key进行验证
    "apiKey": API_KEY,
    "to": "zhangzcwork@qq.com",  # 收件人地址, 用正确邮件地址替代, 多个地址用';'分隔
    "from": "test@LFZNw4boCqCW1kpKcIuCdP2mWcedM0rq.sendcloud.org",  # 发信人, 用正确邮件地址替代
    "fromName": "mytest",
    "subject": "SendCloud python common",
    "html": "欢迎使用SendCloud"
}

filename1 = "1.txt"
display_filename_1 = "aaa"

files = {
    "attachments": (quote(display_filename_1), open(filename1, 'rb'), 'application/octet-stream')
}

r = requests.post(url, files=files, data=params)

print(r.text)
