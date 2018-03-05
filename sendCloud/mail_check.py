# coding:utf-8
"""
this module is used to check mail, check some fields to promise in the request.
"""

import functools
import re
from functools import reduce

from voluptuous import Schema, ALLOW_EXTRA, All, Optional, Required, Invalid, basestring

email_regex = re.compile(r"^[_a-z0-9-A-Z]+(\.[_a-z0-9-A-Z]+)*@[a-z0-9-A-Z]+(\.[a-z0-9-A-Z]+)*(\.[a-zA-Z]{2,4})$")


def check_email(email):
    email_list = email.split(";")
    check_func = lambda x: email_regex.match(x)
    reduce_func = lambda x, y: x and y

    is_valid = reduce(reduce_func, map(check_func, email_list))
    if is_valid:
        return email
    raise Invalid('email error')


# Verify that common mail sends the required fields
# http://www.sendcloud.net/doc/email_v2/send_email/#_1
common_email_schema = Schema({
    Required("apiUser", msg='params apiUser must exist'):
        All(basestring, msg='params apiUser must basestring'),
    Required("apiKey", msg='params apiKey must exist'):
        All(basestring, msg='params apiKey must basestring'),
    Required("from", msg='params from must exist'):
        All(check_email, msg='params from error'),
    Required("to", msg='params to must exist'):
        All(check_email, msg='params to error, use ; split'),
    Required("subject", msg='params subject must exist'):
        All(basestring, msg='prams subject must basestring'),
    Required("html", msg='params html must exist'):
        All(basestring, msg='params html must exist'),
    "fromName": All(basestring, msg='params fromName error'),
    "labelId": All(int, msg='params labelId is int'),
    "cc": All(basestring, check_email, msg='params cc email error'),
    "bcc": All(basestring, check_email, msg='params bcc email error'),
    "replyTo": All(basestring, check_email, msg='params replyTo email error'),
    "contentSummary": All(basestring, msg='params contentSummary error'),
    "plain": All(basestring, msg='params plain error'),
    Optional("useAddressList", default=False):
        All(bool, msg='params useAddressList is bool'),
}, extra=ALLOW_EXTRA)

# Verify that template mail send the required fields
# http://www.sendcloud.net/doc/email_v2/send_email/#_2
template_email_schema = Schema({
    Required('apiUser', msg='params apiUser must exist'):
        All(basestring, msg='params apiUser must basestring'),
    Required('apiKey', msg='params apiKey must exist'):
        All(basestring, msg='params apiKey must basestring'),
    Required('from', msg='params from must exist'):
        All(check_email, msg='params from error'),
    Required("subject", msg='params subject must exist'):
        All(basestring, msg='prams subject must basestring'),
    Required('templateInvokeName', msg='params templateInvokeName must exist'):
        All(basestring, msg='params templateInvokeName must basestring'),
    Optional("useAddressList", default=False):
        All(bool, msg='params useAddressList is bool'),
    Optional("useNotification", default=False):
        All(bool, msg='params useNotification is bool'),
    "replyTo": All(basestring, check_email, msg='params replyTo email error'),
    "fromName": All(basestring, msg='params fromName error'),
}, extra=ALLOW_EXTRA)


def mail_method(method):
    allow_method = ('common', 'template')

    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, **kwargs):
            try:
                if method in allow_method:
                    if method == 'common':
                        data = common_email_schema(kwargs)
                    elif method == 'template':
                        data = template_email_schema(kwargs)
                else:
                    raise ValueError(
                        'The way you entered is not within the allowed range, please check it.("common", "template")')
            except Invalid as e:
                raise Exception(e.msg)
            return func(self, **data)

        return wrapper

    return decorator
