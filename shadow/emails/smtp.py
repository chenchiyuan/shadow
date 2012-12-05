# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
import smtplib

def test(name="localhost"):
  smtpserver = server_factory(name=name)
  to = "331098114@qq.com"
  header = 'To:' + to + '\n' + 'From: ' + "chiyuan@tukeq.com" + '\n' + 'Subject:testing \n'
  print(header)
  msg = header + '\n 这是一封注册邮件测试，你好:陈驰远 \n\n'
  smtpserver.sendmail("chiyuan@tukeq.com", to, msg.encode('utf-8'))
  print("done")
  smtpserver.close()


def server_factory(name=''):
  if not name:
    return get_server("postmaster@tukeq.com", "4qejjaix9tm8",
                      domain="smtp.mailgun.org", port=587)
  elif name == 'localhost':
    return get_server("", "")

def get_server(username, password, domain='localhost', port=25):
  smtpserver = smtplib.SMTP(domain, port)
  smtpserver.ehlo()
  smtpserver.starttls()
  if username and password:
    smtpserver.login(username, password)
  return smtpserver