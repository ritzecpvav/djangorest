from django.urls import path, include
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    path('snippets/', views.Snippet_List.as_view(), name='snippet-list'),
    path('snippets/<int:pk>/', views.Snippet_Detail.as_view(), name='snippet-detail'),
    path('users/', views.User_List.as_view(), name='user-list'),
    path('users/<int:pk>/', views.User_Detail.as_view(), name='user-detail'),
    path('', views.api_root),
    path('snippets/<int:pk>/highlight/', views.Snippet_Highlight.as_view(), name='snippet-highlight'),
])