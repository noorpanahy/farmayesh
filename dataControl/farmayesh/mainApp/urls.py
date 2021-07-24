from django.conf.urls import url
from Farmayesh_app import views
from django.contrib import admin
from django.urls import path,include

urlpatterns=[
    url(r'^RegistrationApi/$',views.RegistrationApi,name='Regitration'),
    url(r'^RegistrationApi/([0-9]+)$',views.RegistrationApi),

    url(r'^ResturantApi/$',views.ResturantApi,name='Regitration'),
    url(r'^ResturantApi/([0-9]+)$',views.ResturantApi),

    url(r'^CatagureApi/$',views.CatagureApi,name='Regitration'),
    url(r'^CatagureApi/([0-9]+)$',views.CatagureApi),

    url(r'^FoodApi/$',views.FoodApi,name='Regitration'),
    url(r'^FoodApi/([0-9]+)$',views.FoodApi),

    url(r'^OrderItemApi/$',views.OrderItemApi,name='Regitration'),
    url(r'^OrderItemApi/([0-9]+)$',views.OrderItemApi),

    url(r'^OrderApi/$',views.OrderApi,name='Regitration'),
    url(r'^OrderApi/([0-9]+)$',views.OrderApi),

    url(r'^AdministratorApi/$',views.AdministratorApi,name='Regitration'),
    url(r'^AdministratorApi/([0-9]+)$',views.AdministratorApi)
]
