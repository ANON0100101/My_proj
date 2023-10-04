from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from spam.tasks import send_product_news

User = get_user_model()


class Category(models.Model):
    """
        Модель категории
    """
    name = models.SlugField(primary_key=True, unique=True, max_length=50)
    parent = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        if self.parent:
            return f'{self.parent} -> {self.name}'
        return self.name


class Product(models.Model):
    """
        модель продукта
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=89)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return f'{self.title}'


@receiver(post_save, sender=Product)
def post_save_product_signal(sender, instance, created, **kwargs):
    if created:
        send_product_news.delay(instance.title, instance.price)
