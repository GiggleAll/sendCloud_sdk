#coding:utf-8                                                                   

import requests                                                                 

url = "http://sendcloud.sohu.com/webapi/mail.send_template.json"                         

API_USER = '...'
API_KEY = '...'

params = {                                                                      
    "api_user": API_USER,
    "api_key" : API_KEY,                                             
    "to" : "test@maillist.sendcloud.org",
    "from" : "sendcloud@sendcloud.org",
    "fromname" : "SendCloud",                                                    
    "subject" : "SendCloud python template address_list",                              
    "template_invoke_name" : "sendcloud_template",
    "use_maillist" : "true",
    "resp_email_id": "true",
}                                                                               

filename = "..."
display_filename = "..."

files = { "file1" : (display_filename, open(filename,"rb"))}

r = requests.post(url, files=files, data=params)

print(r.text)

