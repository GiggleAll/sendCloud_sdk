# coding:utf-8
import json

import requests


class Mail(object):
    def __init__(self):
        # TODO will change this code
        self.send_mail_url = 'http://api.sendcloud.net/apiv2/mail/send'

    def _post_data(self, url, **kwargs):
        resp = requests.post(url, data=kwargs)
        return resp

    def send_email(self, **kwargs):
        resp = self._post_data(self.send_mail_url, **kwargs)
        if resp.status_code == 200:
            try:
                content = json.loads(resp.content)
                content = {
                    "result": content.get("result"),
                    "message": content.get("message")
                }
            except ValueError:
                content = {"result": False, "message": "return is not json"}
        else:
            content = {
                "result": False,
                "message": "send email error http code %s" % resp.status_code
            }
        print('content', content)
        return content
