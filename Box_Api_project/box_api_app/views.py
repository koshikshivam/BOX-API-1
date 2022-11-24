from typing import List
from django.shortcuts import render
from .models import Box
#from django.contrib.auth.models import User
from .serializers import BoxSerializers
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import BasePermission,IsAdminUser,IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.authentication import BasicAuthentication,BaseAuthentication,SessionAuthentication
# from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics





class WriteByAdminOnlyPermission(BasePermission):
    def has_permission(self, request, view):
        User = request.user
        if request.method == 'GET':
            return True
        if request.method == 'POST' or request.method == 'PUT' or request.method == 'DELETE':
            if User.is_staff:
                return True
            
    def has_object_permission(self, request, view, obj):
        if request.method == 'PUT':
            if obj.creator != request.user:
                return False 
        return True
    
    
    
    
    
    # def has_object_permission(self, request, view, obj):
    #     if request.method == 'PATCH':
    #         if obj.length == request.user  and obj.width==request.user and obj.height== request.user :
    #             return False
    #     return True
            
            


# class Creater_of_box_FieldPermission(BasePermission):
#     def has_permission(self,request,view):
#         pass


            
            
# Create your views here.







class BoxModelViewSet(viewsets.ModelViewSet):
    queryset = Box.objects.all()
    serializer_class = BoxSerializers
    permission_classes=[IsAuthenticated,WriteByAdminOnlyPermission]
    authentication_classes = [SessionAuthentication]     
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['creator']
    
    
    
    
    
    
    
   