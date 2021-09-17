from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions

from snippets.models import Snippet
from snippets.serializers import Snippet_Serializer, User_Serializer
from snippets.permissions import IsOwnerOrReadOnly

class Snippet_List(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = Snippet_Serializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class Snippet_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = Snippet_Serializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    IsOwnerOrReadOnly]
class User_List(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = User_Serializer


class User_Detail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = User_Serializer