# -*- coding:utf-8 -*-
__author__ = 'zichen'
__create__ = '2018/9/1 18:11'
from django.core.mail import send_mail
import random
from py27AndDj198.settings import EMAIL_FROM

from users.models import EmailVeryfyRecord


def random_str(random_length=8):
    """
    随机字符串
    :param random_length: 用户指定随机字符个数
    :return:
    """
    str = ''
    # 字符种子
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789';
    # 最大随机位置
    length = len(chars)-1
    for i in range(random_length):
        # 随机位置
        random_len = random.randint(0, length)
        # 将随机字符加入返回字符串
        str += chars[random_len]
    return str


def send_register_email(email, send_type='register'):
    email_record = EmailVeryfyRecord()
    email_record.code = random_str(16)
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ''
    email_content = ''

    if send_type == 'register':
        email_title = 'zc在线注册激活链接'
        email_content = '请点击下面的链接以激活您的账号：http://127.0.0.1:8000/active/{0}'.format(email_record.code)

        # 发送邮件
        # 参数解析：subject:主题标题, message：内容, from_email：发送者, recipient_list：接受者(list类型)
        send_status = send_mail(email_title, email_content, EMAIL_FROM, [email])
        if send_status:
            pass

