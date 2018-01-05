from django.shortcuts import render
from .forms import SubscriberForm
from products.models import *

def landing(request):
    # отрисовываем html шаблон
    name = 'Вася'
    currentTime = "07.12.2017"
    form = SubscriberForm(request.POST or None)
    # чтобы принять данные из формы
    if request.method == "POST" and form.is_valid():
        # посмотреть, что передается в POST запросе
        # print(request.POST)
        # print(form.cleaned_data)
        # посмотреть поле name
        # data = form.cleaned_data
        # print(data["name"])
        # сохраняем данные
        new_form = form.save()
    return render(request, 'landing/landing.html', locals())

def home(request):
    # выводим только активные товары
    products_images = ProductImage.objects.filter(is_active=True, is_main=True)
    return render(request, 'landing/home.html', locals())
