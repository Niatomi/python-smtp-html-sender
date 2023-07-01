from .smtp import EmailSender

def main():
    es = EmailSender()
    es.send_email(to='playervoker@gmail.com', subject='Тестовое сообщение')

if __name__ == "__main__":
    main()
