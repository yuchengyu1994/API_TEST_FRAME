#!/usr/bin/env python
# encoding: utf-8
# @author:Yuchengyu
# @time: 2022/7/13 0013 15:27

import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from common import zip_utils
from common.config_utils import read_config

class EmailUtils:
    def __init__(self,smtp_subject,smtp_body,smtp_file_path=None):
        self.smtp_server = read_config.get_smtp_server
        self.smtp_sender = read_config.get_smtp_sender
        self.smtp_senderpassword = read_config.get_smtp_senderpassword
        self.smtp_receiver = read_config.get_smtp_receiver
        self.smtp_cc = read_config.get_smtp_cc
        self.smtp_subject=smtp_subject
        self.smtp_body=smtp_body
        self.smtp_file=smtp_file_path


    def __mail_text_content(self):
        msg = MIMEText(self.smtp_body, "html", "utf-8")
        msg['from'] = self.smtp_sender
        msg['to'] = self.smtp_receiver
        msg['Cc'] = self.smtp_cc
        msg['subject'] = self.smtp_subject
        return msg

    def __mail_zip_content(self):
        msg = MIMEMultipart()
        with open(self.smtp_file, 'rb') as f:
            mime = MIMEBase('zip', 'zip', filename=self.smtp_file.split('\\')[-1])
            mime.add_header('Content-Disposition', 'attachment',
                            filename=('gb2312', '', self.smtp_file.split('\\')[-1]))
            mime.add_header('Content-ID', '<0>')
            mime.add_header('X-Attachment-Id', '0')
            mime.set_payload(f.read())
            encoders.encode_base64(mime)
            msg.attach(mime)
        msg.attach(MIMEText(self.smtp_body, "html", "utf-8"))
        msg['from'] = self.smtp_sender
        msg['to'] = self.smtp_receiver
        msg['Cc'] = self.smtp_cc
        msg['subject'] = self.smtp_subject
        return msg

    def __mail_content(self):
        msg = MIMEMultipart()
        with open(self.smtp_file, 'rb') as f:
            mime = MIMEBase('zip', 'zip', filename=self.smtp_file.split('\\')[-1])
            mime.add_header('Content-Disposition', 'attachment',
                            filename=('gb2312', '', self.smtp_file.split('\\')[-1]))
            mime.add_header('Content-ID', '<0>')
            mime.add_header('X-Attachment-Id', '0')
            mime.set_payload(f.read())
            encoders.encode_base64(mime)
            msg.attach(mime)
        msg.attach(MIMEText(self.smtp_body, "html", "utf-8"))
        msg['from'] = self.smtp_sender
        msg['to'] = self.smtp_receiver
        msg['Cc'] = self.smtp_cc
        msg['subject'] = self.smtp_subject
        return msg


    def __mail_content_filetype(self):
        if self.smtp_file !=None:
            # return self.__mail_zip_content
            if self.smtp_file.split('.')[-1].__eq__('zip'):
                return self.__mail_zip_content()
            elif self.smtp_file.split('.')[-1].__eq__('html'):
                return self.__mail_content()
            else:
                raise Exception("调用方法错误，请调用send_mail，或者存在附件不匹配 zip 或者html格式")
        else:
            return self.__mail_text_content()


    def __mail_content_by_zip(self):
        zip_path = os.path.join(self.smtp_file, '..', '自动化测试报告.zip')
        zip_utils.zip_utils(self.smtp_file, zip_path)
        self.smtp_file=zip_path  #修改为发送的附件压缩后的路径
        print(zip_path)
        msg = self.__mail_content_filetype()
        return msg


    def send_mail(self):
        try:
            smtp = smtplib.SMTP()
            smtp.connect(self.smtp_server)
            smtp.login(user=self.smtp_sender,password=self.smtp_senderpassword)
        except:
            smtp = smtplib.SMTP_SSL()
            smtp.login(user=self.smtp_sender,password=self.smtp_senderpassword)
        mail_content = self.__mail_content_filetype()
        try:
            smtp.sendmail(self.smtp_sender,self.smtp_receiver.split(',')+self.smtp_cc.split(','),mail_content.as_string())
        except Exception as e:
            print('发送失败')
        smtp.quit()

    def zip_send_mail(self):
        try:
            smtp = smtplib.SMTP()
            smtp.connect(self.smtp_server)
            smtp.login(user=self.smtp_sender,password=self.smtp_senderpassword)
        except:
            smtp = smtplib.SMTP_SSL()
            smtp.login(user=self.smtp_sender,password=self.smtp_senderpassword)
        mail_content = self.__mail_content_by_zip()
        try:
            smtp.sendmail(self.smtp_sender,self.smtp_receiver.split(',')+self.smtp_cc.\
                          split(','),mail_content.as_string())
        except Exception as e:
            print('发送失败')
        smtp.quit()
