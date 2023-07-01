from pathlib import Path
import smtplib
from src.config import smtp_config
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os


class EmailSender:

    def __init__(self) -> None:
        self.read_templates()


    def read_templates(self):
        self.info_template = ''
        info_template_url = Path('src/html_templates/info_message.html', strict=True).resolve()
        with open(info_template_url) as r:
            self.info_template += r.read()
        print(self.info_template)

    @classmethod
    def form_header(cls, to: str, subject: str = 'API Message') -> MIMEMultipart:
        msg = MIMEMultipart()
        msg['From'] = smtp_config.login
        msg['To'] = to
        msg['Subject'] = subject
        return msg

    def send_email(self, to: str, subject: 'str'):
        msg = self.form_header(to, subject)
        html = MIMEText(self.info_template, 'html')
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
            mailserver.sendmail(smtp_config.login,'playervoker@gmail.com',msg.as_string())
            mailserver.quit()
            print("Письмо успешно отправлено")
        except smtplib.SMTPException as e:
            print(e)
            print("Ошибка: Невозможно отправить сообщение")

