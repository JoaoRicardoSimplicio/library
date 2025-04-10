from django.urls import include, path
from rest_framework.routers import DefaultRouter

from books.views import AuthorViewSet, BookViewSet


router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')
router.register(r'authors', AuthorViewSet, basename='author')

urlpatterns = [
    path('', include(router.urls)),
]
