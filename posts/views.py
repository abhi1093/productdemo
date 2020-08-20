from django.shortcuts import render
from rest_framework import generics
from posts.models import Company,Product,PurchaseOrder
from posts.serializers import CompanySerializer,ProductSerializer,PurchaseOrderSerializer

class API_objects(generics.ListCreateAPIView):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer

class API_objects(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class API_objects(generics.ListCreateAPIView):
    queryset=PurchaseOrder.objects.all()
    serializer_class=PurchaseOrderSerializer

class API_objects_details(generics.RetrieveUpdateDestroyAPIView):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer

class API_objects_details(generics.RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class API_objects_details(generics.RetrieveUpdateDestroyAPIView):
    queryset=PurchaseOrder.objects.all()
    serializer_class=PurchaseOrderSerializer

# Create your views here.
