from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('snippets/', views.Snippet_List.as_view()),
    path('snippets/<int:pk>/', views.Snippet_Detail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)