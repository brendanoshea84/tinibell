from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.products, name="products"),
    path('product_detail/<product_id>', views.product_detail, name="product_detail")
]