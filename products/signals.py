from django.db.models.signals import pre_save
from django.dispatch import receiver
from core.models import User
import uuid
from .models import Category,Product, Usersproducts

@receiver(pre_save, sender=Usersproducts)
def pre_save_modify_user_and_create_code(sender, instance, **kwargs):
    if instance.code=="":
        instance.code=str(uuid.uuid4()).replace("-","").upper()[:10]

    

