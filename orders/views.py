from django.http import JsonResponse
from .models import ProductInBasket
from .models import ProductInOrder
from .models import Order
from django.shortcuts import render
from .forms import CheckoutContactForm
from django.contrib.auth.models import User
# from django.conf import settings
# from django.core.mail import send_mail

# возвр. ответ сервера
def basket_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    data = request.POST
    product_id = data.get("product_id")
    nmb = data.get("nmb")
    is_delete = data.get("is_delete")
    if is_delete == 'true':
        ProductInBasket.objects.filter(id=product_id).update(is_active=False)
    else:
        # к функции get_or_create можно обращаться через запятую
        new_product, created = ProductInBasket.objects.get_or_create(session_key=session_key, product_id=product_id, is_active=True, defaults={"nmb": nmb})
        if not created:
            new_product.nmb += int(nmb)
            new_product.save(force_update=True)

    # считаем общую сумму по данному session_key, данный код общий для обоих условий
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    products_total_nmb = products_in_basket.count()
    # отдаем полученный результат в ответ
    return_dict["products_total_nmb"] = products_total_nmb
    return_dict["products"] = list()

    for item in products_in_basket:
        product_dict = dict()
        product_dict["id"] = item.id
        product_dict["name"] = item.product.name
        product_dict["price_per_item"] = item.price_per_item
        product_dict["nmb"] = item.nmb
        return_dict["products"].append(product_dict)

    # print(products_total_nmb)
    return JsonResponse(return_dict)

def checkout(request):
    # берем session_key из request
    session_key = request.session.session_key
    # exclude(order__isnull=False) исключает значения, которые уже есть в заказе
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True).exclude(order__isnull=False)
    # форма принимает request.POST или ничего
    form = CheckoutContactForm(request.POST or None)
    if request.POST:
        print(request.POST)
        if form.is_valid():
            print("yes")
            data = request.POST
            # data.get('name') то же, что и data['name'], только проверяет, передано ли значение name. Если нет, то вернется none
            # именем пользователя в б/д будут введенный им номер телефона
            name = data.get('name', 'John Doe')
            phone = data.get('phone')
            email = data.get('email')
            # выбираем уже созданного пользователя
            user, created = User.objects.get_or_create(username=phone, defaults={"first_name": name})
            # делаем заказ
            order = Order.objects.create(user=user, customer_name=name, customer_phone=phone, customer_email=email, status_id=1)
            # проходим циклом по словарю с пом. функции items()
            for name, value in data.items():
                if name.startswith("product_in_basket_"):
                    product_in_basket_id = name.split("product_in_basket_")[1]
                    product_in_basket = ProductInBasket.objects.get(id=product_in_basket_id)
                    product_in_basket.nmb = value
                    product_in_basket.order = order
                    product_in_basket.save(force_update=True)
                    ProductInOrder.objects.create(product=product_in_basket.product, nmb=product_in_basket.nmb, price_per_item=product_in_basket.price_per_item, total_price=product_in_basket.total_price, order=order)
                    # после оформления заказа очищаем корзину заказавшего пользователя
                    mail = "Ваш заказ № {} успешно оформлен! Вы можете оплатить данный заказ, переведя деньги на счет ...".format(product_in_basket_id)
                    if(ProductInBasket.objects.get(session_key=session_key).delete()):
                        success_checkout = "Ваш заказ успешно оформлен!"
                        # send_mail("По заказу № {}".format(product_in_basket_id), mail, settings.EMAIL_HOST_USER, [email], fail_silently=False)

        else:
            print("no")
    return render(request, 'orders/checkout.html', locals())