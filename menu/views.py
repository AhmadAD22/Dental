from django.shortcuts import render,redirect
from django.conf import settings
from .models import *
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from .forms import*
from django.contrib.auth import authenticate, login

def create_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'user_create.html', {'form': form})

def products(request):
    user = request.user
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {
        'products': products,
        'user': user,
        'categories': categories,
    }
    return render(request, 'menu.html', context)

def product_details(request,product_id):
    user = request.user
    products = Product.objects.get(id=product_id)
    context = {
        'product': products,
        'user': user,
    }
    return render(request, 'product.html', context)



from datetime import datetime, timedelta

def Home(request):
    user = request.user
    
    # Filter products based on release date
    today = datetime.now().date()
    products = Product.objects.order_by('-id')[:3]
    
    context = {
        'products': products,
        'user': user,
    }
    return render(request, 'home.html', context)