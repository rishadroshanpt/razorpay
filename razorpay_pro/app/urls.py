from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path("payment/", views.order_payment, name="payment"),
]