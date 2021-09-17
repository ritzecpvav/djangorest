from django.urls import path, include

from snippets import views
from snippets.views import Snippet_View_Set, User_View_Set, api_root

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers


snippet_list = Snippet_View_Set.as_view({
    'get': 'list',
    'post': 'create'
})
snippet_detail = Snippet_View_Set.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
snippet_highlight = Snippet_View_Set.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = User_View_Set.as_view({
    'get': 'list'
})
user_detail = User_View_Set.as_view({
    'get': 'retrieve'
})

urlpatterns = format_suffix_patterns([
    path('', api_root),
    path('snippets/', snippet_list, name='snippet-list'),
    path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
    path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
    path('users/', user_list, name='user-list'),
])