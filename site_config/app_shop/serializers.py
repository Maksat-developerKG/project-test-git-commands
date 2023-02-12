from .models import Product, Category
from rest_framework import serializers

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name']


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

    