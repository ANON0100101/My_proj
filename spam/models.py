from django.db import models


class Contact(models.Model):
    """
        Модель для подписки рассылки
    """
    email = models.EmailField('Почта', unique=True, help_text='Введите почту пользователя')

    def __str__(self) -> str:
        return f'{self.email}'
