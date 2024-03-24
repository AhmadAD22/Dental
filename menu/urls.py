from django.urls import path
from .views import *

urlpatterns = [
    path('products',products,name="menu"),
    path('',Home,name="home"),
    path('product/<int:product_id>',product_details,name="product_details"),
    path('user/create/', create_user, name='create_user'),
]