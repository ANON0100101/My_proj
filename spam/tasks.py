from django.core.mail import send_mail
from config.celery import app
from spam.models import Contact


@app.task
def send_product_news(title, price):
    emails = [i.email for i in Contact.objects.all() if i.email]


    send_mail(
        'Extra theme py29',
        f'Привет. \n Загляни на наш сайт у нас вышел новый продукт {title} цена которого {price}',
        'a.kudaikulov04@gmail.com',
        emails

    )




