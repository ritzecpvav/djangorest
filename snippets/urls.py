from django.urls import path, include

from snippets import views
from snippets.views import Snippet_View_Set, User_View_Set, api_root

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'snippets', views.Snippet_View_Set)
router.register(r'users', views.User_View_Set)

urlpatterns = [
    path('', include(router.urls)),
]
