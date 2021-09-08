from django.shortcuts import render

# Create your views here.
from .models import *
from .serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import status
from django.db.models import Q 
from rest_framework.viewsets import ModelViewSet

# Create your views here.

############################################################### API FOR CATEGORY ###################################################
class Categoryview(APIView):
    """
    GET or  POST CATEGORY API 
    """

    def get(self, request, format=None):
        try:
            cat = Category.objects.all()
            serializer = CategorySerializer(cat, many=True)
            return Response({"status":True,"message":"All Category data fetched successfully",
            "data":serializer.data},status=status.HTTP_200_OK)
        except Exception:
                return Response({"status":False,"message":"Something went wrong"},status=status.HTTP_400_BAD_REQUEST) 

    def post(self, request, format=None):
        try:
            serializer = CategorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status":True,"message":"Category created successfully",
                "data":serializer.data},status=status.HTTP_201_CREATED)
        except Exception:
            return Response({"status":False,"message":"Something went wrong"},status=status.HTTP_400_BAD_REQUEST) 


class CategoryDetail(APIView):
    """
    GET, PUT or DELETE a Category instance.
    """
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        try:
            cat = self.get_object(pk)
            serializer = CategorySerializer(cat)
            return Response({"status":True,"message":"Category data fetched successfully",
            "data":serializer.data},status=status.HTTP_200_OK)
        except Exception:
            return Response({"status":False,"message":"Something went wrong"},status=status.HTTP_400_BAD_REQUEST) 

    def put(self,request,pk=None):
        try:
            cat=Category.objects.get(id=pk)
            serializer=CategorySerializer(cat,data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({"status":True,"message":"Category updated successfully","data":serializer.data},status=status.HTTP_200_OK)
        except Exception:
            return Response({"status":False,"message":"OOPS,Something went wrong"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
       
    def delete(self, request, pk):
        try:
            cat = self.get_object(pk)
            cat.delete()
            return Response({"status":True,"message":"Category removed successfully"},status=status.HTTP_204_NO_CONTENT)
        except Exception:
            return Response({"status":False,"message":"OOPS,Something went wrong"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


########################################################## API FOR  POST PRODUCT ##############################################
class Productview(APIView):
    """
    GET or POST PRODUCT API
    """

    def get(self, request, format=None):
        try:
            product = Product.objects.all()
            serializer = ProductSerializer(product, many=True)
            return Response({"status":True,"message":"All Product data fetched successfully",
            "data":serializer.data},status=status.HTTP_200_OK)
        except Exception:
                return Response({"status":False,"message":"Something went wrong"},status=status.HTTP_400_BAD_REQUEST) 

    def post(self, request, format=None):
        try:
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status":True,"message":"Product created successfully",
                "data":serializer.data},status=status.HTTP_201_CREATED)
        except Exception:
            return Response({"status":False,"message":"Something went wrong"},status=status.HTTP_400_BAD_REQUEST) 




class ProductDetail(APIView):
    """
    GET, PUT or DELETE a Product instance.
    """
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        try:
            product = self.get_object(pk)
            serializer = ProductSerializer(product)
            return Response({"status":True,"message":"Product data fetched successfully",
            "data":serializer.data},status=status.HTTP_200_OK)
        except Exception:
            return Response({"status":False,"message":"Something went wrong"},status=status.HTTP_400_BAD_REQUEST) 

    def put(self,request,pk=None):
        try:
            snippet=Product.objects.get(id=pk)
            serializer=ProductSerializer(snippet,data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({"status":True,"message":"Product updated successfully","data":serializer.data},status=status.HTTP_200_OK)
        except Exception:
            return Response({"status":False,"message":"OOPS,Something went wrong"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
       
    def delete(self, request, pk):
        try:
            product = self.get_object(pk)
            product.delete()
            return Response({"status":True,"message":"Product removed successfully"},status=status.HTTP_204_NO_CONTENT)
        except Exception:
            return Response({"status":False,"message":"OOPS,Something went wrong"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

###################################################### API FOR SEARCH OF PRODUCT #######################################################

class ProductSearch(APIView):
    '''
    API FOR SEARCH OF PRODUCT
    
    '''
    def post(self,request):
        try:
            params=request.data 
            if 'product_name' in params:
                obj=Product.objects.filter(Q(is_deleted=False)) & Product.objects.filter(Q(product_name__icontains=params['product_name']))
            if 'category_type' in params:
                obj=Product.objects.filter(Q(is_deleted=False)) & Product.objects.filter(Q(category_type__category_name__icontains=params['category_type']))
            if 'product_colour'  in params:
                obj=Product.objects.filter(Q(is_deleted=False)) & Product.objects.filter(product_colour__icontains=params['product_colour'])
            if not obj:
                return Response({"status":False,"message":"Requested Product not found"},status=status.HTTP_404_NOT_FOUND)
            serializer=ProductSerializer(obj,many=True)
            return Response({"status":True,"message":"Data fethced successfully","data":serializer.data},status=status.HTTP_200_OK)
        except Exception:
            return Response({"status":False,"message":"OOPS,Something went wrong"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


