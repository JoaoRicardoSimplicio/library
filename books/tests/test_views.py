import pytest
from unittest.mock import ANY, patch

from django.urls import reverse
from rest_framework.test import APIClient

from books.models import Author, Book
from books.tests.fixtures import AuthorFactory, BookFactory
from books.seeds import OPEN_LIBRARY_BOOK_LOCAL_DATA


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
class TestBookViewSet:

    def test_list_books(self, api_client):
        BookFactory.create_batch(3)

        url = reverse('book-list')

        response = api_client.get(url)

        assert 200 == response.status_code
        assert 3 == response.json()['count']

    def test_create_book(self, api_client):
        payload = {
            'title': 'Clean Code: A Handbook of Agile Software Craftsmanship',
            'isbn': '9780132350884',
            'authors_names': [
                'Robert C. Martin',
                'Dean Wampler'
            ],
            'description': '',
            'published_at': '2008-08-11'
        }

        url = reverse('book-list')

        response = api_client.post(url, data=payload)

        assert 201 == response.status_code
        assert 1 == Book.objects.count()
        assert 2 == Author.objects.count()

    def test_try_create_book_without_isbn(self, api_client):
        payload = {
            'title': 'Clean Code: A Handbook of Agile Software Craftsmanship',
            'authors_names': [
                'Robert C. Martin',
                'Dean Wampler'
            ],
            'description': '',
            'published_at': '2008-08-11'
        }

        url = reverse('book-list')

        response = api_client.post(url, data=payload)

        assert 400 == response.status_code
        assert response.json() == {'isbn': ['This field is required.']}
        assert 0 == Book.objects.count()
        assert 0 == Author.objects.count()

    def test_try_create_book_with_existent_isbn(self, api_client):
        author = AuthorFactory(name='Robert C. Martin')
        book = BookFactory(
            title='Clean Code: A Handbook of Agile Software Craftsmanship',
            isbn='9780132350883',
            authors=[author],
            published_at='2008-08-10'
        )
        payload = {
            'title': 'Clean Code: A Handbook of Agile Software Craftsmanship (Edition 2)',
            'isbn': '9780132350883',
            'authors_names': [
                'Robert C. Martin',
                'Dean Wampler'
            ],
            'description': '',
            'published_at': '2020-08-10'
        }

        url = reverse('book-list')

        response = api_client.post(url, data=payload)

        assert 400 == response.status_code
        assert response.json() == {'isbn': ['book with this isbn already exists.']}
        assert 1 == Book.objects.count()
        assert 1 == Author.objects.count()

    def test_try_create_book_without_authors_names(self, api_client):
        payload = {
            'title': 'Clean Code: A Handbook of Agile Software Craftsmanship',
            'isbn': '9780132350884',
            'authors_names': [
            ],
            'description': '',
            'published_at': '2008-08-11'
        }

        url = reverse('book-list')

        response = api_client.post(url, data=payload)

        assert 400 == response.status_code
        assert response.json() == {'authors_names': ['This field is required.']}
        assert 0 == Book.objects.count()
        assert 0 == Author.objects.count()

    def test_update_book(self, api_client):
        author = AuthorFactory(name='Robert C. Martin')
        book = BookFactory(
            title='We, Programmers: A Chronicle of Coders from Ada to AI (Robert C. Martin Series)',
            isbn='0135344263',
            authors=[author],
            published_at='2025-12-24'
        )

        payload = {'isbn': '9780132350884'}
        url = reverse('book-detail', kwargs={'pk': book.id})

        response = api_client.patch(url, data=payload, format='json')

        book.refresh_from_db()

        assert response.status_code == 200
        assert response.json()['isbn'] == payload['isbn']
        assert book.isbn == payload['isbn']

    def test_get_book(self, api_client):
        author = AuthorFactory(name='Robert C. Martin')
        book = BookFactory(
            title='We, Programmers: A Chronicle of Coders from Ada to AI (Robert C. Martin Series)',
            isbn='0135344263',
            authors=[author],
            published_at='2025-12-24'
        )
        expected_data = {
            'id': book.id,
            'title': book.title,
            'isbn': book.isbn,
            'authors': [
                {'id': author.id, 'name': author.name}
            ],
            'description': book.description,
            'published_at': book.published_at
        }

        url = reverse('book-detail', kwargs={'pk': book.id})

        response = api_client.get(url)

        assert 200 == response.status_code
        assert expected_data == response.json()

    def test_delete_book(self, api_client):
        author = AuthorFactory(name='Robert C. Martin')
        book = BookFactory(
            title='We, Programmers: A Chronicle of Coders from Ada to AI (Robert C. Martin Series)',
            isbn='0135344263',
            authors=[author],
            published_at='2025-12-24'
        )

        url = reverse('book-detail', kwargs={'pk': book.id})

        assert 1 == Book.objects.count()
        assert 1 == Author.objects.count()

        response = api_client.delete(url)

        assert 204 == response.status_code
        assert 0 == Book.objects.count()
        assert 1 == Author.objects.count()

    @patch('books.services.requests.get')
    def test_ingest_book_data_by_isbn(self, mock_requests_get, api_client):
        isbn = '978-0132931755'
        _isbn = f'ISBN:{isbn}'

        mock_response = {_isbn: OPEN_LIBRARY_BOOK_LOCAL_DATA.get(f'ISBN:{isbn}')}
        mock_requests_get.return_value.status_code = 200
        mock_requests_get.return_value.json.return_value = mock_response

        expected_data = {
            'id': ANY,
            'title': 'Working Effectively with Legacy Code',
            'isbn': '978-0132931755',
            'authors': [
                {'id': ANY, 'name': 'Michael C. Feathers'}
            ],
            'published_at': '2004-01-01',
            'description': None
        }

        url = reverse('book-ingest')

        payload = {'isbn': isbn}

        response = api_client.post(url, data=payload)

        assert 201 == response.status_code
        assert expected_data == response.json()
        assert 1 == Book.objects.count()
        assert 1 == Author.objects.count()
        mock_requests_get.assert_called_once()

    @patch('books.services.requests.get')
    def test_ingest_book_data_by_isbn_error_when_isbn_not_provided(self, mock_requests_get, api_client):
        url = reverse('book-ingest')

        payload = {}

        response = api_client.post(url, data=payload)

        assert 400 == response.status_code
        assert {'detail': 'ISBN must be provided.'} == response.json()
        assert 0 == Book.objects.count()
        assert 0 == Author.objects.count()
        mock_requests_get.assert_not_called()

    @patch('books.services.requests.get')
    def test_ingest_book_data_was_not_found_by_isbn(self, mock_requests_get, api_client):
        url = reverse('book-ingest')

        mock_requests_get.return_value.status_code = 200
        mock_requests_get.return_value.json.return_value = {}

        payload = {'isbn': '978-00000001'}

        response = api_client.post(url, data=payload)

        assert 404 == response.status_code
        assert {'detail': 'Book data was not found.'} == response.json()
        assert 0 == Book.objects.count()
        assert 0 == Author.objects.count()
        mock_requests_get.assert_called_once()

@pytest.mark.django_db
class TestAuthorViewSet:

    def test_list_authors(self, api_client):
        AuthorFactory.create_batch(3)

        url = reverse('author-list')

        response = api_client.get(url)

        assert 200 == response.status_code
        assert 3 == response.json()['count']

    def test_create_author(self, api_client):
        payload = {'name': 'Robert C. Martin'}

        url = reverse('author-list')

        response = api_client.post(url, data=payload)

        assert 201 == response.status_code
        assert 1 == Author.objects.count()

    def test_try_create_author_with_blank_name(self, api_client):
        payload = {'name': ''}

        url = reverse('author-list')

        response = api_client.post(url, data=payload)

        assert 400 == response.status_code
        assert response.json() == {'name': ['This field may not be blank.']}
        assert 0 == Author.objects.count()

    def test_update_author(self, api_client):
        author = AuthorFactory(name='Robert')

        payload = {'name': 'Robert C. Martin'}
        url = reverse('author-detail', kwargs={'pk': author.id})

        response = api_client.patch(url, data=payload, format='json')

        author.refresh_from_db()

        assert response.status_code == 200
        assert response.json()['name'] == payload['name']
        assert author.name == payload['name']

    def test_get_author(self, api_client):
        author = AuthorFactory(name='Robert C. Martin')
        expected_data = {'id': author.id, 'name': 'Robert C. Martin'}

        url = reverse('author-detail', kwargs={'pk': author.id})

        response = api_client.get(url)

        assert response.status_code == 200
        assert expected_data == response.json()

    def test_delete_author(self, api_client):
        author = AuthorFactory(name='Robert C. Martin')

        url = reverse('author-detail', kwargs={'pk': author.id})

        assert 1 == Author.objects.count()

        response = api_client.delete(url)

        assert 204 == response.status_code
        assert 0 == Author.objects.count()
