#!/usr/bin/env python
# -*- coding:utf-8 -*
from .mail import Mail


class CommandMail(Mail):
    def __init__(self):
        super(CommandMail, self).__init__()
        self.command_mail_url = 'http://api.sendcloud.net/apiv2/mail/send'


