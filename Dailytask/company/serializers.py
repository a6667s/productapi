from django.db.models import fields
from .models import *
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields =['id','category_name']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields =['id','product_name','product_image','category_type','product_colour','product_price']
    def to_representation(self, instance):
        self.fields['category_type'] =  CategorySerializer(read_only=True)
        return super(ProductSerializer, self).to_representation(instance)