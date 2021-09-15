from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from djangorest.quickstart.serializers import User_Serializer, Group_Serializer


class User_View_Set(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = User_Serializer
    permission_classes = [permissions.IsAuthenticated]


class Group_View_Set(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = Group_Serializer
    permission_classes = [permissions.IsAuthenticated]