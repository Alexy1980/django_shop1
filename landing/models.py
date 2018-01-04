from django.db import models

# название модели соответствует названию таблицы в базе данных
class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128)
    # выводим записи по названию полей
    def __str__(self):
       # вместо %s будут подставлены значения в скобках
       return "Пользователь: %s, email: %s" % (self.name, self.email)

    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'
