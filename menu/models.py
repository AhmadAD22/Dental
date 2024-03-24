from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import os

# Create your models here.
from autoslug import AutoSlugField

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='اسم التصنيف')
    slug = AutoSlugField(max_length=255, unique=True, populate_from='name', verbose_name='الاسم المختصر')
    image = models.ImageField(upload_to='category/', null=True, verbose_name='رفع الصورة')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء', blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث', blank=True, null=True)

    def __str__(self):
        return self.name
    
    def delete(self, *args, **kwargs):
        # Delete the associated image file
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super(Category, self).delete(*args, **kwargs)



class Product(models.Model):
    image = models.ImageField(upload_to='products/', verbose_name='رفع الصورة')
    name = models.CharField(max_length=255, verbose_name='اسم المنتج')
    description = models.TextField(blank=True, null=True, verbose_name='الوصف')
    category=models.ForeignKey(Category, verbose_name='التصنيف', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='السعر')
    offers = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0,blank=False, verbose_name='الخصم')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء',blank=True,null=True)
    updated_on = models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث',blank=True,null=True)


    def delete(self, *args, **kwargs):
        # Delete the associated image file
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        
        super(Product, self).delete(*args, **kwargs)
    def __str__(self):
        return self.name