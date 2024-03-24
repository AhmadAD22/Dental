from django import forms
from menu.models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserModel





class DashboardUserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    is_superuser = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check'}), required=False)
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'is_superuser','password1', 'password2']
        

class DashboardUserUpdateForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_superuser = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check'}), required=False)
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'is_superuser']
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="User Name ", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))


#Category
class CategoryForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}), label='رفع الصورة')
    class Meta:
        model = Category
        fields = ('name', 'image')
        labels = {
            'name': 'اسم التصنيف',
            'image': 'رفع الصورة',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
      
      
# Product  
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('image', 'name', 'description', 'category', 'price', 'offers')
        labels = {
            'image': 'رفع الصورة',
            'name': 'اسم المنتج',
            'description': 'الوصف',
            'category': 'التصنيف',
            'price': 'السعر',
            'offers': 'الخصم',
        }
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'offers': forms.NumberInput(attrs={'class': 'form-control'}),
        }