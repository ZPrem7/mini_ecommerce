from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from products.serializers import ProductSerializer
from products.models import User,Product
from rest_framework.response import Response
import jwt, datetime
from rest_framework import generics
from django.contrib.auth import authenticate
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework_simplejwt.tokens import RefreshToken




class RestrictedView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response(data={"message": "You have access to this restricted content."})
    

class ProductViewsets(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class=ProductSerializer
    queryset=Product.objects.all()

        

# class ProductAPI(APIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]
#     def get(self,request):
#         obj=Product.objects.all()
#         serializer=ProductSerializer(obj, many =True)
#         return Response(serializer.data)

#     def post(self,request):
#         data=request.data
#         serializer=ProductSerializer(data=data)
#         if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#         return Response(serializer.errors)     

#     def put(request,id):
#         data=request.data
#         obj=Product.objects.get(id=data["id"])
#         serializer=ProductSerializer(obj,data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
    
#     def delete(request,id):
#         data=request.data
#         obj=Product.objects.get(id=data["id"])
#         obj.delete()
#         return Response("Deleted successfully")



