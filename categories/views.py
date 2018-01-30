from django.shortcuts import render
from categories.models import *
from products.models import *

def category(request, category_id):
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(is_active=True)
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    #print(request.session.session_key)
    return render(request, 'categories/category.html', locals())
