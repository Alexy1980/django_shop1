from django.shortcuts import render
from products.models import *
from categories.models import *

def product(request, product_id):
    product = Product.objects.get(id=product_id)
    # используем сессионный ключ
    session_key = request.session.session_key
    # если пользователь не авторизован, django последних версий не создает ключ сессий, поэтому создаем его вручную (когда пользователь заходит в Product, у него создается ключ сессии). Ключ сессии уникален для каждого пользователя
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)
    return render(request, 'products/product.html', locals())
