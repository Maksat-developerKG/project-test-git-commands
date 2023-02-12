from django.shortcuts import render
from rest_framework import viewsets

from .serializers import ProductSerializers, CategorySerializers, SubCategoruSerializers
from .models import Product, Category, SubCategory


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategoruSerializers
