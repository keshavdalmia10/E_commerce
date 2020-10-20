from django.db import models
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.conf import settings
from core.models import User


class Product(models.Model):
    """"Product model"""
   
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=20)
    description = models.CharField(max_length=500)
   
    slug = models.SlugField(blank=True)
    
    def __str__(self):
        return self.name


class Category(models.Model):
    """Category model"""
    title = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    

    def __str__(self):
        return self.title

class Usersproducts(models.Model):  
     
    product=models.OneToOneField(Product, on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    code=models.CharField(max_length=10, blank=True)
     









	

    
