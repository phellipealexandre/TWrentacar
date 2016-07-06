from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^customers/$', views.customers, name='customers'),
    url(r'^customers/register/$', views.customers_register, name='customers_register'),
    url(r'^customers/submit/$', views.customer_submit, name='customers_submit'),
    url(r'^cars/$', views.cars, name='cars'),
    url(r'^cars/register/$', views.cars_register, name='cars_register'),
    url(r'^cars/submit/$', views.car_submit, name='cars_submit'),
]