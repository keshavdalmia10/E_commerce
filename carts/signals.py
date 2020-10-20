from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver

from .models import Cart
from orders.models import Order
from core.models import User
import uuid

   
