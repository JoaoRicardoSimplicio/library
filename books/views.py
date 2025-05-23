from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from books.models import Author, Book
from books.serializers import AuthorSerializer, BookISBNSerializer, BookSerializer
from books.services import get_book_data_by_isbn


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @swagger_auto_schema(method='post', operation_description='Fetch book data based on ISBN ingestion', query_serializer=BookISBNSerializer)
    @action(detail=False, methods=['post'], url_path='ingest')
    def ingest(self, request):
        isbn = request.data.get('isbn')
        if not isbn:
            return Response(
                {'detail': 'ISBN must be provided.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        book_data = get_book_data_by_isbn(isbn=isbn)

        if not book_data:
            return Response(
                {'detail': 'Book data was not found.'},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = BookSerializer(data=book_data)
        serializer.is_valid(raise_exception=True)
        book = serializer.save()

        return Response(BookSerializer(book).data, status=status.HTTP_201_CREATED)


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
