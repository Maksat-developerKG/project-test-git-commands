from .models import Product, Category, SubCategory
from rest_framework import serializers


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class SubCategoruSerializers(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = "__all__"
