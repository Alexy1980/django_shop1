from django.shortcuts import render
from categories.models import *
from products.models import *

def category(request, category_id):
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(is_active=True)
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    # products_images_apple = products_images.filter(product__category__id=1)
    # products_images_nokia = products_images.filter(product__category__id=2)
    # products_images_samsung = products_images.filter(product__category__id=3)
    # products_images_huawei = products_images.filter(product__category__id=4)
    # products_images_hp = products_images.filter(product__category__id=5)
    # products_images_lenovo = products_images.filter(product__category__id=6)
    #print(request.session.session_key)
    return render(request, 'categories/category.html', locals())
