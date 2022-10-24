from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Products
# Create your views here.
from .serializers import ProductsSerializer


class LatestProductsList(APIView):
    def get(self, request, format=None):
        products = Products.objects.all()[0:4]
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data)
