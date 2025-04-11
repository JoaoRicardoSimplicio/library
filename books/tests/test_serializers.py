from unittest import mock

import pytest

from django.test import TestCase

from books.models import Author, Book
from books.serializers import AuthorSerializer, BookSerializer


@pytest.mark.django_db
class TestAuthSerializer(TestCase):

    def test_creates_author(self):
        authors_test_data = {
            'authors_data': [
                {'name': 'Robert C. Martin'},
                {'name': 'Dean Wampler'},
                {'name': 'George Orwell'}
            ],
            'results': {
                'authors_count': 3
            }
        }
        for author_data in authors_test_data['authors_data']:
            author_serializer = AuthorSerializer(data=author_data)

            assert author_serializer.is_valid()

            author_serializer.save()

        assert authors_test_data['results']['authors_count'] == Author.objects.count()

    def test_does_not_creates_author_with_blank_name(self):
        author_data = {'name': ''}
        author_serializer = AuthorSerializer(data=author_data)

        assert not author_serializer.is_valid()
        assert "name" in author_serializer.errors
        assert author_serializer.errors["name"][0] == str("This field may not be blank.")

    def test_updates_author(self):
        author = Author.objects.create(name='Robert')

        updated_data = {'name': 'Robert C. Martin'}

        author_serializer = AuthorSerializer(instance=author, data=updated_data)

        assert author_serializer.is_valid()
        assert 1 == Author.objects.count()

        author_serializer.save()
        author.refresh_from_db()

        assert updated_data['name'] == author.name
        assert 1 == Author.objects.count()


@pytest.mark.django_db
class TestBookSerializer(TestCase):

    def test_creates_book(self):
        books_test_data = {
            'books_data': [
                {
                    'title': 'Clean Code: A Handbook of Agile Software Craftsmanship',
                    'isbn': '9780132350884',
                    'authors_names': [
                        'Robert C. Martin',
                        'Dean Wampler'
                    ],
                    'description': '',
                    'published_at': '2008-08-11'
                },
                {
                    'title': "Clean Architecture: A Craftsman's Guide to Software Structure and Design (Robert C. Martin Series)",
                    'isbn': '9780132350885',
                    'authors_names': [
                        'Robert C. Martin',
                        'Kevlin Henney'
                    ],
                    'description': '',
                    'published_at': '2012-09-12'
                },
                {
                    'title': 'We, Programmers: A Chronicle of Coders from Ada to AI (Robert C. Martin Series)',
                    'isbn': '0135344263',
                    'authors_names': [
                        'Robert C. Martin',
                    ],
                    'description': '',
                    'published_at': None
                }
            ],
            'results': {
                'book_count': 3,
                'authors_count': 3
            }
        }

        for book_data in books_test_data['books_data']:
            book_serializer = BookSerializer(data=book_data)

            assert book_serializer.is_valid()

            book_serializer.save()

        assert books_test_data['results']['book_count'] == Book.objects.count()
        assert books_test_data['results']['authors_count'] == Author.objects.count()

    def test_does_not_creates_book_without_isbn(self):
        book_data = {
            'title': 'Clean Code: A Handbook of Agile Software Craftsmanship',
            'authors_names': [
                'Robert C. Martin',
                'Dean Wampler'
            ],
            'description': '',
            'published_at': '2008-08-11'
        }
        book_serializer = BookSerializer(data=book_data)

        assert not book_serializer.is_valid()
        assert "isbn" in book_serializer.errors
        assert book_serializer.errors["isbn"][0] == str("This field is required.")

    def test_does_not_creates_book_without_title(self):
        book_data = {
            'isbn': '9780132350884',
            'authors_names': [
                'Robert C. Martin',
                'Dean Wampler'
            ],
            'description': '',
            'published_at': '2008-08-11'
        }
        book_serializer = BookSerializer(data=book_data)

        assert not book_serializer.is_valid()
        assert "title" in book_serializer.errors
        assert book_serializer.errors["title"][0] == str("This field is required.")

    def test_updates_book(self):
        author = Author.objects.create(name='Robert C. Martin')
        book = Book.objects.create(
            title='Clean Code',
            isbn='9780132350884',
            published_at='2008-08-11'
        )
        book.authors.set([author])

        updated_data = {'title': 'Clean Code: A Handbook of Agile Software Craftsmanship'}

        book_serializer = BookSerializer(instance=book, data=updated_data, partial=True)

        assert book_serializer.is_valid()
        book_serializer.save()

        book.refresh_from_db()

        assert updated_data['title'] == book.title
        assert author.name == book.authors.first().name
        assert 1 == Author.objects.count()
        assert 1 == Book.objects.count()

    def test_updates_book_authors(self):
        author = Author.objects.create(name='Robert C. Martin')
        book = Book.objects.create(
            title='Clean Code: A Handbook of Agile Software Craftsmanship',
            isbn='9780132350884',
            published_at='2008-08-11'
        )
        book.authors.set([author])

        updated_data = {
            'authors_names': ['Robert C. Martin', 'Dean Wampler']
        }

        book_serializer = BookSerializer(instance=book, data=updated_data, partial=True)

        assert book_serializer.is_valid()
        book_serializer.save()

        book.refresh_from_db()

        assert ['Robert C. Martin', 'Dean Wampler'] == [author.name for author in book.authors.all()]
        assert 2 == Author.objects.count()
        assert 1 == Book.objects.count()
