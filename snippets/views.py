from django.shortcuts import render
from django.http import Http404

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics

from snippets.models import Snippet
from snippets.serializers import Snippet_Serializer


class Snippet_List(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = Snippet_Serializer

class Snippet_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = Snippet_Serializer