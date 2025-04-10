from typing import Any, Dict, List

from rest_framework import serializers

from books.models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)
    authors_names = serializers.ListField(
        child=serializers.CharField(),
        write_only=True
    )

    class Meta:
        model = Book
        fields = ['id', 'title', 'isbn', 'authors', 'authors_names', 'published_at', 'description']

    def create(self, validated_data: Dict[str, Any]) -> Book:
        authors_names: List[str] = validated_data.pop('authors_names', None)
        book: Book = Book.objects.create(**validated_data)
        if authors_names:
            authors: List[Book] = [Author.objects.get_or_create(name=name)[0] for name in authors_names]
            book.authors.set(authors)
        return book

    def update(self, instance: Book, validated_data: Dict[str, Any]) -> Book:
        authors_names: List[str] = validated_data.pop('authors_names', [])
        if authors_names:
            authors: List[Book] = [Author.objects.get_or_create(name=name)[0] for name in authors_names]
            instance.authors.set(authors)
        return super().update(instance, validated_data)
