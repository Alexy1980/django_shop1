from django.db import models

# название модели соответствует названию таблицы в базе данных
class Category(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    # изменяется при update
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    # выводим записи по названию полей
    def __str__(self):
       # вместо %s будут подставлены значение
       return "Категория: %s" % self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
