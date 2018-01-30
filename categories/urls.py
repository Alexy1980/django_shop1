from django.urls import path, include
from django.conf.urls import url
from categories import views

urlpatterns = [
    # url(r'^', views.landing, name='landing')
    url(r'^category/(?P<category_id>\w+)/$', views.category, name='category')
]