from django.urls import path
from .views import *

urlpatterns = [
    path('',main_dashboard,name="main_dashboard"),
    path('product/create/', create_product, name='create_product'),
    path('product/update/<int:pk>/', update_product, name='update_product'),
    path('product/delete/<int:pk>/', delete_product, name='delete_product'),
    path('product/list/', product_list, name='product_list'),
    #Category
    path('category_list',category_list,name="category_list"),
    path('delete_category/<int:pk>',delete_category,name="delete_category"),
    path('create_category',create_category,name="create_category"),
    path('category/edit/<int:pk>/', edit_category, name='edit_category'),
     
]
