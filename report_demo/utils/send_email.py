# coding: utf-8
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


class EmailSend:
    """邮件"""

    @staticmethod
    def email_add_file(send_type, file_path: list, file_name: list, _msg):
        """
        添加单种类型附件
        :param send_type: 发送类型(txt image html)
        :param file_path: 文件路径
        :param file_name: 文件名
        :param _msg: 消息对象
        """
        # 文件路径与文件名需要一一对应
        if not all([file_path, file_name]):
            return '文件路径或文件名不能为空'
        file_path_len = len(file_path)
        file_name_len = len(file_name)
        if file_path_len == file_name_len:
            for i in range(len(file_path)):
                if send_type == 'txt':
                    attach_file = MIMEApplication(open(file_path[i]).read())
                elif send_type == 'image':
                    attach_file = MIMEImage(open(file_path[i], 'rb').read())
                else:
                    attach_file = MIMEText(open(file_path[i], 'r').read())
                attach_file.add_header('Content-Disposition', 'attachment', filename=file_name[i])
                _msg.attach(attach_file)
            return '邮件附件添加成功'
        else:
            return '文件路径与文件名长度不匹配'

    def for_email(self, send_user, receive_user, password, sub_title, content, send_type, file_path, file_name):
        """
        发送邮件
        :param send_user: 发件人地址
        :param receive_user: 收件人地址
        :param password: 发件人授权码
        :param sub_title: 邮件主题
        :param content: 邮件正文
        :param send_type: 发送类型(txt image html)
        :param file_path: 文件路径
        :param file_name: 文件名
        """
        mail_server = 'smtp.163.com'
        port = '465'
        msg = MIMEMultipart('related')
        msg['From'] = formataddr(["ME", send_user])
        msg['To'] = formataddr(["YOU", receive_user])
        msg['Subject'] = sub_title
        txt = MIMEText(content, 'plain', 'utf-8')
        msg.attach(txt)

        # 添加附件
        for i in range(len(send_type)):
            self.email_add_file(send_type[i], file_path[i], file_name[i], msg)

        server = smtplib.SMTP_SSL(mail_server, port)
        server.login(send_user, password)
        server.sendmail(send_user, receive_user, msg.as_string())
        server.quit()


# 测试代码
# sender = '123@163.com'
# receive = '123@qq.com'
# pass_wd = '123'
# sub_title = '123'
# content = '123'
# # send_type = ['txt', 'image', 'html']
# # file_path = [['abc.txt'], ['1.png', '../data/image/2.png'], ['abc.html']]
# # file_name = [['abc.txt'], ['1.png', '2.png'], ['abc.html']]

# send_type = ['image']
# file_path = [['/Applications/py_data/dn_test/test/data/image/1.png', '../data/image/2.png']]
# file_name = [['1.png', '2.png']]

# for_email(sender, receive, pass_wd, sub_title, content, send_type, file_path, file_name)
