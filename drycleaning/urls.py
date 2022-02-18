from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('home', views.index),
    #this is for calling the orders function in the view
    path('orders',views.orders),
    path('contact',views.contact)
]