from django.contrib.auth.models import User
from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cart, CartItem, Product
from menu.models import *
from .models import *
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required



class CartItemQuantityUpdateAPIView(APIView):
    def post(self, request):
        itemId = request.data.get('itemId')
        quantityChange = int(request.data.get('quantityChange'))

        cart_item = get_object_or_404(CartItem, id=itemId)
        cart_item.quantity += quantityChange

        if cart_item.quantity > 0:
            cart_item.save()
            return Response({'message': 'Item updated'}, status=status.HTTP_200_OK)
        else:
            cart_item.delete()
            return Response({'message': 'deleted.'}, status=status.HTTP_200_OK)

class AddToCartAPIView(APIView):
    def post(self, request):
        user_id = request.data.get('user_id')
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)

        try:
            user = User.objects.get(id=user_id)
            product = Product.objects.get(id=product_id)
        except (User.DoesNotExist, Product.DoesNotExist):
            return Response(
                {'error': 'Invalid user or product.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        cart, _ = Cart.objects.get_or_create(user=user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

        if not created:
            cart_item.quantity += int(quantity)
            cart_item.save()

        return Response({'success': 'Item added to cart.'}, status=status.HTTP_200_OK)


class CartItemsAPIView(APIView):
    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            cart = Cart.objects.get(user=user)
        except User.DoesNotExist:
            return Response(
                {'error': 'User does not exist.'},
                status=status.HTTP_404_NOT_FOUND
            )
        except Cart.DoesNotExist:
            return Response(
                {'error': 'Cart does not exist.'},
                status=status.HTTP_404_NOT_FOUND
            )

        cart_items = CartItem.objects.filter(cart=cart)
        data = []
        total_price = 0  # Variable to store the total price
        for cart_item in cart_items:
            item_data = {
                'id': cart_item.id,
                'product': cart_item.product.name,
                'quantity': cart_item.quantity,
                'price': cart_item.product.price,
            }
            data.append(item_data)
            total_item_price = cart_item.quantity * cart_item.product.price
            item_data['total_price'] = total_item_price
            total_price += total_item_price

        # Add the total price to the response data
        data.append({'total_price': total_price})

        return Response(data, status=status.HTTP_200_OK)


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Cart, Order, OrderItem
@login_required
def confirm_order(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        cart = Cart.objects.get(user=request.user)
        
        # Create a new order
        if cart.cartitem_set.all():
            order = Order.objects.create(user=request.user, address=address)

        # Add items from the cart to the order
        for cart_item in cart.cartitem_set.all():
            OrderItem.objects.create(
                order=order,
                product=cart_item.product,
                quantity=cart_item.quantity,
                price=cart_item.product.price
            )

        # Clear the cart after creating the order
        cart.products.clear()

        # Redirect to a success page or do any other necessary actions
        return redirect('home')  # Assuming you have a URL name 'menu' for the menu page
    else:
        # Handle GET request for displaying the confirmation form
        try:
            cart = Cart.objects.get(user=request.user)
        except Cart.DoesNotExist:
            return Response(
                {'error': 'Cart does not exist.'},
                status=status.HTTP_404_NOT_FOUND
            )

        cart_items = CartItem.objects.filter(cart=cart)
        data = []
        total_price = 0
        for cart_item in cart_items:
            item_data = {
                'id': cart_item.id,
                'product': cart_item.product.name,
                'quantity': cart_item.quantity,
                'price': cart_item.product.price,
            }
            total_item_price = cart_item.quantity * cart_item.product.price
            item_data['total_price'] = total_item_price
            total_price += total_item_price
            data.append(item_data)

        context = {
            'data': data,
            'total_price': total_price,
            'user':request.user
        }
        return render(request, 'confirm_order.html', context)
    
    

@login_required(login_url='login')  # Redirect to the login page if the user is not authenticated
def user_orders(request):
    # Retrieve orders for the logged-in user
    orders = Order.objects.filter(user=request.user)

    context = {
        'orders': orders,
        'user':request.user
    }
    return render(request, 'user_orders.html', context)

@login_required(login_url='login')  # Redirect to the login page if the user is not authenticated
def order_details(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    context = {
        'order': order
    }
    return render(request, 'order_details.html', context)