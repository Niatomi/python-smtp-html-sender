from pathlib import Path
import smtplib
from src.config import smtp_config
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import re

class EmailSender:

    HTML_TEMPLATE = ''

    def __init__(self) -> None:
        self.set_html_template()

    def set_html_template(self):
        self.HTML_TEMPLATE = ''
        info_template_url = Path('src/html_templates/info_message.html', strict=True).resolve()
        with open(info_template_url) as r:
            self.HTML_TEMPLATE += r.read()

    @classmethod
    def form_header(cls, to: str, subject: str = 'API Message') -> MIMEMultipart:
        msg = MIMEMultipart()
        msg['From'] = smtp_config.login
        msg['To'] = to
        msg['Subject'] = subject
        return msg

    def preprocess_html(self, insert_data):
        data = ''
        for d in insert_data:
            data += f'<p>{d}</p>'
        return re.sub('<% insertPosition %>', data, self.HTML_TEMPLATE)

    def send_email(self, to: str, subject: 'str', data_content):
        msg = self.form_header(to, subject)
        html = MIMEText(self.preprocess_html(data_content), 'html')
        msg.attach(html)
        try:
            mailserver = smtplib.SMTP('smtp.yandex.ru',587)
            mailserver.set_debuglevel(True)
            # Определяем, поддерживает ли сервер TLS
            mailserver.ehlo()

            # Защищаем соединение с помощью шифрования tls
            mailserver.starttls()

            # Повторно идентифицируем себя как зашифрованное соединение перед аутентификацией.
            mailserver.ehlo()
            mailserver.login(smtp_config.login, smtp_config.password)
            mailserver.send_message(msg, smtp_config.login, to)
            mailserver.quit()
            print("Письмо успешно отправлено")
        except smtplib.SMTPException as e:
            print(e)
            print("Ошибка: Невозможно отправить сообщение")

