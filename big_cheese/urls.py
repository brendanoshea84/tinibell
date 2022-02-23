from . import views
from django.urls import path

urlpatterns = [
    path('add_product/', views.add_product, name='add_product'),
    path('update_product/', views.update_product, name='update_product'),
    path('update_product/<item_id>', views.submit_product, name="submit_product"),
    path('add_event/', views.add_event, name='add_event'),
    path('update_event/', views.update_event, name='update_event'),
    path('update_event/<item_id>', views.submit_event, name="submit_event"),
    path('user_mgmt/', views.user_mgmt, name='user_mgmt'),
    path('site_ctrl/', views.site_ctrl, name='site_ctrl'),
    path('pickup_location/', views.pickup_location, name="pickup_location"),
    path('pickup_location/<item_id>', views.update_location, name="update_location"),
    path('add_location/', views.add_location, name="add_location"),
]