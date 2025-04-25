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

    baselist = resl

    return Response(result)



# @api_view(['GET','POST'])
# def deposit_products(request):

# @api_view(['GET'])
# def deposit_product_options(request):

# @api_view(['GET'])
# def top_rate(request):


# Create your views here.
