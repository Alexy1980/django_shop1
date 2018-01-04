from django.contrib import admin
from .models import *
from landing.models import Subscriber

class SubscriberAdmin (admin.ModelAdmin):
    # list_display = ["name", "email"]
    list_display = [field.name for field in Subscriber._meta.fields]
    # поле фильтр
    list_filter = ['name']
    # поле поиска по имени
    search_fields = ['name']
    fields = ["email"]
    # exclude = ["email"]
    class Meta:
        model = Subscriber
# берем модули site и register и регистрируем модель
admin.site.register(Subscriber, SubscriberAdmin)