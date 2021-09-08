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
from rest_framework.authtoken.models import Token 
from django.contrib.auth import  authenticate,login 
from django.db.models import Q 
from rest_framework.authentication import TokenAuthentication 
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class Categoryview(APIView):
    """
    GET or  POST Catagory...
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

class Productview(APIView):
    """
    GET or  POST Product...
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
    Retrieve, update or delete a Product instance.
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
        # try:

        snippet=Product.objects.get(id=pk)
        serializer=ProductSerializer(snippet,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"status":True,"message":"Product updated successfully","data":serializer.data},status=status.HTTP_200_OK)
        # except Exception:
        #     return Response({"status":False,"message":"OOPS,Something went wrong"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
       
    def delete(self, request, pk):
        try:
            product = self.get_object(pk)
            product.delete()
            return Response({"status":True,"message":"Product removed successfully"},status=status.HTTP_204_NO_CONTENT)
        except Exception:
            return Response({"status":False,"message":"OOPS,Something went wrong"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)