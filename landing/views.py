from django.shortcuts import render
from .forms import SubscriberForm
from products.models import *
from categories.models import *

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
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products = Product.objects.filter(is_active=True)
    categories = Category.objects.filter(is_active=True)
    # выбираем по типу товара
    products_images_phones = products_images.filter(product__type__id=2)
    products_images_laptops = products_images.filter(product__type__id=1)
    products_images_new = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__is_new=True)

    return render(request, 'landing/home.html', locals())

