from django.db import models
from decimal import Decimal
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save
from core.models import User
from carts.models import Cart
import uuid


# Create your models here.

ADDRESS_TYPE = (
	('billing', 'Billing'),
	('shipping', 'Shipping'),
)

class UserAddress(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	type = models.CharField(max_length=120, choices=ADDRESS_TYPE)
	street = models.CharField(max_length=120)
	city = models.CharField(max_length=120)
	state = models.CharField(max_length=120)
	zipcode = models.CharField(max_length=120)

	def __unicode__(self):
		return self.street

	


ORDER_STATUS_CHOICES = (
	('created', 'Created'),
	('paid', 'Paid'),
	('shipped', 'Shipped'),
	('refunded', 'Refunded'),
)


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=120, choices=ORDER_STATUS_CHOICES, default='created')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    billing_address = models.ForeignKey(UserAddress, related_name='billing_address', null=True, on_delete=models.CASCADE)
    shipping_address = models.ForeignKey(UserAddress, related_name='shipping_address', null=True, on_delete=models.CASCADE)
   
    order_total = models.DecimalField(max_digits=50, decimal_places=2,null=True )
    order_id = models.CharField(max_length=20, null=True, blank=True)

    def __unicode__(self):
	    return self.id 

		