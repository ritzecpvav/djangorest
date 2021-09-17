from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from rest_framework.reverse import reverse
from rest_framework import renderers

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

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })

class Snippet_Highlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)