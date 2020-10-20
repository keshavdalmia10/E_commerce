from rest_framework import serializers
from . models import Cart




class CartSerializer(serializers.ModelSerializer):
    """Serializer for an ingredient object"""

    class Meta:
        model = Cart
        fields ='__all__'
        read_only_fields = ('id',)
