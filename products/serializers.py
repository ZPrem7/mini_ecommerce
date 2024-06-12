from rest_framework import serializers
from products.models import UserProfile,Product

from django.contrib.auth.models import User


      

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'    