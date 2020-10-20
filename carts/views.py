from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model, authenticate
from django.http import Http404
from django.utils.translation import ugettext_lazy as _
from carts.models import Cart
from products.models import Product, Usersproducts
from carts import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CartSerializer
from django.shortcuts import get_object_or_404



class CartView(APIView):
    cart=get_object_or_404(Cart,)
    def get_object(self,user):
        try:
            return Usersproducts.objects.get(user=user)
        except Usersproducts.DoesNotExist:
            raise Http404

    def get(self, request, user, format=None, *args, **kwargs):
        userproduct=self.get_object(user)
        serializer=CartSerializer(userproduct)
        return Response(serializer.data)
    
    def post(self, request, user, format=None, *args, **kwargs):
        userproduct=self.get_object(user=user)
        cart.user=user
        cart.products=userproduct.product
        cart.save()
        
        


        
        


