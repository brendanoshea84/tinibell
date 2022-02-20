from . import views
from django.urls import path

urlpatterns = [
    path('add_product/', views.add_product, name='add_product'),
    path('update_product/', views.update_product, name='update_product'),
    path('update_product/<item_id>', views.submit_product, name="submit_product"),
    path('add_event/', views.add_event, name='add_event'),
    path('update_event/', views.update_event, name='update_event'),
    path('user_mgmt/', views.user_mgmt, name='user_mgmt'),
    path('site_ctrl/', views.site_ctrl, name='site_ctrl'),
]