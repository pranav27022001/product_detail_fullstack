from dataclasses import field
from pyexpat import model
from .models import Products
from rest_framework import serializers

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'