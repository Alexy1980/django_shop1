from django.http import JsonResponse
from .models import ProductInBasket

# возвр. ответ сервера
def basket_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    data = request.POST
    product_id = data.get("product_id")
    nmb = data.get("nmb")
    new_product = ProductInBasket.objects.create(session_key=session_key, product_id=product_id, nmb=nmb)
    # считаем общую сумму по данному session_key
    products_total_nmb = ProductInBasket.objects.filter(session_key=session_key, is_active=True).count()
    # отдаем полученный результат в ответ
    return_dict["products_total_nmb"] = products_total_nmb
    print(products_total_nmb)
    return JsonResponse(return_dict)