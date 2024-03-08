from django.shortcuts import render,redirect
from menu.models import *
from .forms import *


#Categories
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category/category_list.html', {'categories': categories})

def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'category/create_category.html', {'form': form})

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

def delete_category(request, pk):
    category = Category.objects.get(pk=pk)
    category.delete()
    return redirect('category_list')



def main_dashboard(request):
    products=Product.objects.all()
    return render(request,'main_dashboard.html',{'products':products})

#Products
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    
    return render(request, 'product/create_product.html', {'form': form})

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

def delete_product(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    return redirect('product_list')
    
    

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product/product_list.html', {'products': products})
