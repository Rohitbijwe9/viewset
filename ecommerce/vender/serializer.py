from rest_framework import serializers
from .models import Product
from django.core import validators



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=Product
