import requests
import pprint 

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import render, redirect
from django.conf import settings

from .models import DepositOptions, DepositProducts

from .serializer import DepositProductsSerializer,DepositOptionsSerializer

API_KEY =settings.API_KEY

URL = f"http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1"

@api_view(['GET'])
def save_deposit_products(request):
    
    response = requests.get(URL)

    data = response.json()

    result = data['result']

    baselists = result['baseList']

    serializer = DepositProductsSerializer(data=baselists,many=True)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors,status=404)

@api_view(['GET','POST'])
def deposit_products(request):

    if request.method == "GET":
        deposit_products = DepositProducts.objects.all()
        serializer = DepositProductsSerializer(deposit_products,many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = DepositProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=400)

# 옵션 리스트 저장 
@api_view(['GET'])
def save_deposit_options(request):
    response = requests.get(URL)

    data = response.json()

    result = data['result']

    optionlists = result['optionList']

    serializer = DepositOptionsSerializer(data=optionlists,many=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors,status=400)


# # 특정 상품의 옵션 리스트 출력 
# @api_view(['GET'])
# def deposit_product_options(request,fin_prdt_cd):
    

# @api_view(['GET'])
# def top_rate(request):


# Create your views here.
