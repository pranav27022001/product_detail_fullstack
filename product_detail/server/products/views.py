from django.shortcuts import render
from .models import Products
from .serializers import ProductsSerializer
from rest_framework import response
from rest_framework.decorators import api_view
from rest_framework import viewsets 
# Create your views here.

class ProductView(viewsets.ModelViewSet):
    queryset=Products.objects.all()
    serializer_class= ProductsSerializer