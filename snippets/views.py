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
from rest_framework import viewsets
from rest_framework.decorators import action

from snippets.models import Snippet
from snippets.serializers import Snippet_Serializer, User_Serializer
from snippets.permissions import IsOwnerOrReadOnly

class Snippet_View_Set(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = Snippet_Serializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
class User_View_Set(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = User_Serializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })
