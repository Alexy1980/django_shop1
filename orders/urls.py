from django.urls import path, include
from django.conf.urls import url
from django.contrib import admin
from orders import views

urlpatterns = [
    url(r'^basket_adding/$', views.basket_adding, name='basket_adding')
]