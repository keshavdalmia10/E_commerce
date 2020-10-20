from django.db import models
from decimal import Decimal
from django.conf import settings

from django.db import models
from django.db.models.signals import pre_save, post_save, post_delete   

from products.models import Product, Usersproducts

# Create your models here.



class Cart(models.Model):
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    name=models.CharField(max_length=200, blank=True)
    products=models.ManyToManyField(Product)
    total=models.PositiveIntegerField(blank=True, null=True)
    total_price=models.DecimalField(blank=True, decimal_places=2,max_digits=20, null=True)
    active=models.BooleanField(default=True)


    def __unicode__(self):
	    return str(self.name)

