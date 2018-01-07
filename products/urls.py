from django.urls import path, include
from django.conf.urls import url
from products import views

urlpatterns = [
    # url(r'^', views.landing, name='landing')
    url(r'^product/(?P<product_id>\w+)/$', views.product, name='product')
]