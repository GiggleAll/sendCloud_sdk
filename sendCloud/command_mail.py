#!/usr/bin/env python
# -*- coding:utf-8 -*
from sendCloud.mail import Mail
from sendCloud.mail_check import mail_method
from config import dc


class CommandMail(Mail):
    def __init__(self):
        super(CommandMail, self).__init__()
        self.send_mail_url = dc.common_url

    @mail_method('common')
    def send_email(self, **kwargs):
        """
                * apiUser: API_USER
                * apiKey; API_KEY
                * from: send email addr
                * to: send to email, split by ';' eg: a@123.com;b@123.com
                * subject: email title
                * html: email content, format:text/html
                * contentSummary: email summary
                * fromName:send name
                * cc: copy to,split by ";" eg:a@123.com;b@123.com
                * bcc: secret copy to, split by ; eg:a@123.com;b@123.com
                * replyTo: default reply to, less than 3
                * useAddressList: default False, if to is list than set this True
                :param kwargs:
                :return:
                """
        return super(CommandMail, self).send_email(**kwargs)


if __name__ == '__main__':
    params = {'apiUser': dc.api_user, 'apiKey': dc.api_key, 'from': dc.sender, 'to': 'zhichaozhang3@gmail.com',
              'subject': 'test for common email', 'html': 'hello world', 'fromName': 'test for sendcloud'}
    common_email = CommandMail()
    result = common_email.send_email(**params)
    print('test', result['message'])
