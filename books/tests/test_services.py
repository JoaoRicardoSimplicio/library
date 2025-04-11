import pytest
from unittest.mock import patch

from django.test import TestCase

from books.seeds import OPEN_LIBRARY_BOOK_LOCAL_DATA
from books.services import get_book_data_by_isbn


class TestBookServices:

    @patch('books.services.requests.get')
    def test_get_book_data_by_isbn(self, mock_requests_get):
        isbn = '978-0143130727'
        _isbn = f'ISBN:{isbn}'
        mock_response = {_isbn: OPEN_LIBRARY_BOOK_LOCAL_DATA.get(f'ISBN:{isbn}')}

        mock_requests_get.return_value.status_code = 200
        mock_requests_get.return_value.json.return_value = mock_response

        expcted_data = {
            'title': 'Ikigai the Japanese secret to a long and happy life',
            'authors_names': ['Héctor García'],
            'isbn': isbn,
            'description': (
                "Bring meaning and joy to all your days with this internationally bestselling "
                "guide to the Japanese concept of ikigai -- the happiness of always being "
                "busy -- as revealed by the daily habits of the world's longest-living people. "
                "-- From Amazon.com summary."
            ),
            'published_at': '2017-01-01'
        }

        book_data = get_book_data_by_isbn(isbn)

        assert expcted_data == book_data
        mock_requests_get.assert_called_once()

    @patch('books.services.requests.get')
    def test_get_book_data_by_isbn_cached(self, mock_requests_get):
        isbn = '1931498717'
        _isbn = f'ISBN:{isbn}'
        mock_response = {_isbn: OPEN_LIBRARY_BOOK_LOCAL_DATA.get(f'ISBN:{isbn}')}

        mock_requests_get.return_value.status_code = 200
        mock_requests_get.return_value.json.return_value = mock_response

        expcted_data = {
            'title': "Don't Think of an Elephant!",
            'authors_names': [],
            'isbn': isbn,
            'description': (
                "Don't Think of an Elephant! is the antidote to the last forty years of conservative strategizing "
                "and the right wing's stranglehold on political dialogue in the United States. "
                "Author George Lakoff explains how conservatives think, and how to counter their arguments. He outlines in detail "
                "the traditional American values that progressives hold, but are often unable to articulate. "
                "Lakoff also breaks down the ways conservatives have framed the issues, and provides examples of how "
                "progressives can reframe the debate. "
                "Lakoff's years of research and work with environmental and political leaders have been distilled into this essential guide, "
                "which shows progressives how to think in terms of values instead of programs, and why people vote their values and identities, "
                "often against their best interests.--BOOK JACKET."
            ),
            'published_at': '2004-09-01'
        }

        book_data = get_book_data_by_isbn(isbn)

        assert expcted_data == book_data

        book_data = get_book_data_by_isbn(isbn)

        assert expcted_data == book_data
        mock_requests_get.assert_called_once()

    @patch('books.services.requests.get')
    def test_book_data_was_not_found_by_isbn(self, mock_requests_get):
        isbn = '978-00000001'
        _isbn = f'ISBN:{isbn}'
        mock_response = {}

        mock_requests_get.return_value.status_code = 200
        mock_requests_get.return_value.json.return_value = mock_response

        book_data = get_book_data_by_isbn(isbn)

        assert book_data is None
        mock_requests_get.assert_called_once()
