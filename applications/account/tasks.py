from django.core.mail import send_mail
from config.celery import app


@app.task
def send_test_message():
    import time
    time.sleep(10)
    send_mail(
        'Extra theme py29',
        f'Это тестовое сообщение',
        'a.kudaikulov04@gmail.com',
        ['a.kudaikulov04@gmail.com']
    )


@app.task
def send_activation_code(email, code):
    send_mail(
        'Extra theme py29',
        f'Перейдите по этой ссылке чтобы активировать аккаунт: \n\n http://localhost:8000/api/v1/account/activate/{code}',
        'a.kudaikulov04@gmail.com',
        [email]
    )


@app.task
def send_forgot_password_code(email, code):
    send_mail(
        'Extra theme py29',
        f'Вот ваш код для восстановления пароля, никому не показывайте его: {code}',
        'a.kudaikulov04@gmail.com',
        [email]
    )


@app.task
def send_spam():
    send_mail(
        'Extra theme py29',
        f'Загляни на наш сайт!!!',
        'a.kudaikulov04@gmail.com',
        ['a.kudaikulov04@gmail.com']
    )
