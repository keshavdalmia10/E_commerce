from rest_framework import serializers
from . models import Product, Category




class ProductSerializer(serializers.ModelSerializer):
    """Serializer for an ingredient object"""

    class Meta:
        model = Product
        fields ='__all__'
        read_only_fields = ('id',)

