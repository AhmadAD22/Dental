from django.shortcuts import render,redirect,get_object_or_404
from menu.models import *
from .forms import *
from cart.models import *
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')  # Redirect to the login page if the user is not authenticated
def user_list(request):
    users = User.objects.all()
    return render(request, 'user/users_list.html', {'users': users})

@login_required(login_url='login')  # Redirect to the login page if the user is not authenticated
def create_user(request):
    if request.method == 'POST':
        form = DashboardUserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            return redirect('user_list')
    else:
        form = DashboardUserRegistrationForm()
    return render(request, 'user/create_user.html', {'form': form})


@login_required(login_url='login')  # Redirect to the login page if the user is not authenticated
def update_user(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == 'POST':
        form = DashboardUserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user = form.save()
            return redirect('user_list')
    else:
        form = DashboardUserUpdateForm(instance=user)
    return render(request, 'user/update_user.html', {'form': form})

@login_required(login_url='login')  # Redirect to the login page if the user is not authenticated
def delete_user(request, pk):
    user = User.objects.get(pk=pk)
    user.delete()
    return redirect('user_list')

#Categories
@login_required(login_url='login')  # Redirect to the login page if the user is not authenticated
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category/category_list.html', {'categories': categories})

@login_required(login_url='login')  # Redirect to the login page if the user is not authenticated
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'category/create_category.html', {'form': form})

@login_required(login_url='login')  # Redirect to the login page if the user is not authenticated
def edit_category(request, pk):
    category = Category.objects.get(pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            category = form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category/edit_category.html', {'form': form, 'category': category})

@login_required(login_url='login')  # Redirect to the login page if the user is not authenticated
def delete_category(request, pk):
    category = Category.objects.get(pk=pk)
    category.delete()
    return redirect('category_list')


@login_required(login_url='login')  # Redirect to the login page if the user is not authenticated
def main_dashboard(request):
    product_count=Product.objects.all().count()
    performe_order_count=Order.objects.filter(performed=True).count()
    unperforme_order_count=Order.objects.filter(performed=False).count()
    user_count=User.objects.all().count()
    context = {
        'product_count': product_count,
        'performe_order_count':performe_order_count,
        'unperforme_order_count':unperforme_order_count,
        'user_count':user_count,
        
        
    }
    return render(request,'main_dashboard.html',context)

#Products
@login_required(login_url='login')  # Redirect to the login page if the user is not authenticated
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    
    return render(request, 'product/create_product.html', {'form': form})

@login_required(login_url='login')  # Redirect to the login page if the user is not authenticated
def update_product(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    
    return render(request, 'product/update_product.html', {'form': form, 'product': product})


@login_required(login_url='login')  # Redirect to the login page if the user is not authenticated
def delete_product(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    return redirect('product_list')
    
    
@login_required(login_url='login')  # Redirect to the login page if the user is not authenticated
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product/product_list.html', {'products': products})


@login_required(login_url='login')  # Redirect to the login page if the user is not authenticated
def new_orders(request):
    # Retrieve orders for the logged-in user
    orders = Order.objects.filter(performed=False)

    context = {
        'orders': orders,
    }
    return render(request, 'order/new_orders.html', context)

@login_required(login_url='login')  # Redirect to the login page if the user is not authenticated
def performed_orders(request):
    # Retrieve orders for the logged-in user
    orders = Order.objects.filter(performed=True)

    context = {
        'orders': orders,
    }
    return render(request, 'order/performed_order.html', context)

@login_required(login_url='login')  # Redirect to the login page if the user is not authenticated
def order_details(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    context = {
        'order': order
    }
    return render(request, 'order/order.html', context)

@login_required(login_url='login')  # Redirect to the login page if the user is not authenticated
def performe_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.performed=True
    order.save()
    return redirect('new_orders')
    

    

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})



def logout_user(request):
    logout(request)
    return redirect('home')
