import os
from functools import lru_cache
from typing import Any, Dict

from core.requester import requests
from core.helpers import parse_date


BASE_OPEN_LIBRARY_URL: str = os.environ.get('BASE_OPEN_LIBRARY_URL', 'http://openlibrary.org/')
RELATIVE_OPEN_LIBRARY_BOOKS_URL: str = os.environ.get('RELATIVE_OPEN_LIBRARY_BOOKS_URL', 'api/books')


def parse_book_data(isbn: str, book_data: Dict[str, Any]) -> Dict[str, Any]:
    return {
        'title': book_data.get('full_title') or book_data.get('title'),
        'authors_names': [author.get('name') for author in book_data.get('authors', []) if author],
        'isbn': isbn,
        'description': book_data.get('description') if isinstance(book_data.get('description'), str) else book_data.get('description', {}).get('value'),
        'published_at': parse_date(book_data.get('publish_date'))
    }


@lru_cache(maxsize=250)
def get_book_data_by_isbn(isbn: str) -> Dict[str, Any]:
    isbn_value = f'ISBN:{isbn}'
    params = {'bibkeys': isbn_value, 'jscmd': 'details', 'format': 'json'}

    response = requests.get(
        url= BASE_OPEN_LIBRARY_URL + RELATIVE_OPEN_LIBRARY_BOOKS_URL,
        params=params
    )

    try:
        book_data = response.json()[isbn_value]['details']
    except KeyError:
        return

    return parse_book_data(isbn=isbn, book_data=book_data)
