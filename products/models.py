from django.db import models
from categories.models import Category

# название модели соответствует названию таблицы в базе данных
class Product(models.Model):
    category = models.ForeignKey(Category, blank=True, null=True, default=None, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, blank=True, null=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    description = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    # изменяется при create
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    # изменяется при update
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    # выводим записи по названию полей
    def __str__(self):
       # вместо %s будут подставлены значение
       return "%s" % self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/img/products_images/')
    is_active = models.BooleanField(default=True)
    # изменяется при create
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    # изменяется при update
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    # выводим записи по названию полей
    def __str__(self):
       # вместо %s будут подставлены значение self.id
       return "%s" % self.id

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'