from django.db import models
from products.models import Product
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Status(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    # изменяется при update
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    # выводим записи по названию полей
    def __str__(self):
       # вместо %s будут подставлены значение
       return "Статус: %s" % self.name

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказа'


# название модели соответствует названию таблицы в базе данных
class Order(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, default=None, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_name = models.CharField(max_length=128, blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=48, blank=True, null=True, default=None)
    customer_address = models.CharField(max_length=128, blank=True, null=True, default=None)
    status = models.ForeignKey(Status, default=1, on_delete=models.CASCADE)
    comments = models.TextField(blank=True, null=True, default=None)
    # изменяется при create
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    # изменяется при update
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    # выводим записи по названию полей
    def __str__(self):
       return "Заказ: %s %s" % (self.id, self.status.name)
    # описание
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)

# товары в заказе
class ProductInOrder(models.Model):
    # ссылка на заказ
    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
    nmb = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    # изменяется при create
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    # изменяется при update
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    # выводим записи по названию полей
    def __str__(self):
       # вместо %s будут подставлены значение
       return "%s" % self.product.name

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'

    # переопределяем метод save() модели ProductInOrder
    def save(self, *args, **kwargs):
        price_per_item = self.product.price
        self.price_per_item = price_per_item
        # переопределяем поле total_price
        self.total_price = int(self.nmb) * self.price_per_item

        super(ProductInOrder, self).save(*args, **kwargs)

def product_in_order_post_save(sender, instance, created, **kwargs):
    order = instance.order
    all_products_in_order = ProductInOrder.objects.filter(order=order, is_active=True)
    # считаем общую стоимость заказов
    order_total_price = 0
    for item in all_products_in_order:
        order_total_price += item.total_price

    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)

class ProductInBasket(models.Model):
    # ссылка на заказ
    session_key = models.CharField(max_length=128, blank=True, null=True, default=None)
    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
    nmb = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    # изменяется при create
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    # изменяется при update
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    # выводим записи по названию полей
    def __str__(self):
       # вместо %s будут подставлены значение
       return "%s" % self.product.name

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'

    # переопределяем метод save() модели ProductInOrder
    def save(self, *args, **kwargs):
        price_per_item = self.product.price
        self.price_per_item = price_per_item
        # переопределяем поле total_price
        self.total_price = int(self.nmb) * self.price_per_item

        super(ProductInBasket, self).save(*args, **kwargs)

# вызываем метод product_in_order_post_save()
post_save.connect(product_in_order_post_save, sender=ProductInOrder)