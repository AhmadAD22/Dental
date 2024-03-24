from django.urls import path
from .views import *

urlpatterns = [
path('api/add-to-cart/', AddToCartAPIView.as_view(), name='add_to_cart_api'),
path('api/cart-items/<int:user_id>/', CartItemsAPIView.as_view(), name='cart_items_api'),
path('update-cart-item-quantity/', CartItemQuantityUpdateAPIView.as_view(), name='update_cart_item_quantity'),

path('confirm/', confirm_order, name='confirm_order'),
path('user/orders/', user_orders, name='user_orders'),
path('user/orders/<int:order_id>/', order_details, name='user_order_details'),

]