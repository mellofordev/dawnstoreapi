from django.shortcuts import render,HttpResponse
from .models import Product
from rest_framework.decorators import api_view
from .serializers import ProductSerializer
from rest_framework.response import Response
# Create your views here.
@api_view(['GET'])
def home(request):
    if request.method=='GET':
        get_product = Product.objects.all()
        serializer = ProductSerializer(get_product,many=True)
        return Response({"products":serializer.data})