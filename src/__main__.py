from .smtp import EmailSender

def main():
    es = EmailSender()
    data = [
    'Данные для авторизации в системе',
    'Имя пользователя: niatomi',
    'Пароль: waiodfjg',
    'Подразделение: Самарский ИВЦ',
    'Должность: Программист 1-й категории',
    'Роль в системе: Администратор',
    'Срок действия учётной записи: 12.12.2030'
    ]
    es.send_email(to='playervoker@gmail.com',
                  subject='АС ВИДЕОКОНТРОЛЬ: Изменение учётной записи',
                  data_content=data)

if __name__ == "__main__":
    main()
