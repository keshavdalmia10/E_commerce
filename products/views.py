from rest_framework import viewsets, mixins
#from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _

from products.models import Product

from products import serializers



class ProductViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,  mixins.CreateModelMixin):
    """Manage tags in the database"""
   # authentication_classes = (TokenAuthentication,)
   # permission_classes = (IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
