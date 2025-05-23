from rest_framework import serializers
from .models import DepositOptions, DepositProducts

class DepositProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProducts
        fields = '__all__'

class DepositOptionsSerializer(serializers.ModelSerializer):

    product = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = DepositOptions
        fields = '__all__'
