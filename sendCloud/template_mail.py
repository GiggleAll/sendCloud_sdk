#!/usr/bin/env python
# -*- coding:utf-8 -*
from sendCloud.mail import Mail
from sendCloud.mail_check import mail_method
from config import dc


class TemplateMail(Mail):
    def __init__(self):
        super(TemplateMail, self).__init__()
        self.send_mail_url = dc.template_url

    @mail_method('template')
    def send_email(self, **kwargs):
        return super(TemplateMail, self).send_email(**kwargs)


if __name__ == '__main__':
    import json

    sub_vars = {
        'to': ['zhichaozhang3@gmail.com'],
        'sub': {
            '%name%': ['user1'],
            '%money%': ['1000'],
        }
    }

    params = {'apiUser': dc.api_user, 'apiKey': dc.api_key, 'from': dc.sender,
              'templateInvokeName': 'test_template',
              'xsmtpapi': json.dumps(sub_vars),
              'subject': 'test for common email', 'fromName': 'test for sendcloud', "resp_email_id": "true", }
    template_email = TemplateMail()
    result = template_email.send_email(**params)
    print('test', result['message'])
