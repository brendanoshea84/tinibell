from . import views
from django.urls import path

urlpatterns = [
    path('', views.big_cheese, name='big_cheese'),
]