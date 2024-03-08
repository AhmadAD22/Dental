from django import forms
from menu.models import *


#Category
class CategoryForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}), label='رفع الصورة')
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
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'offers': forms.NumberInput(attrs={'class': 'form-control'}),
        }