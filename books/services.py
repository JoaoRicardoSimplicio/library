import os
from functools import lru_cache
from typing import Any, Dict

from core.requester import requests
from core.helpers import parse_date


BASE_OPEN_LIBRARY_URL: str = os.environ.get('BASE_OPEN_LIBRARY_URL', 'https://openlibrary.org/')
RELATIVE_OPEN_LIBRARY_BOOKS_URL: str = os.environ.get('RELATIVE_OPEN_LIBRARY_BOOKS_URL', '/api/books')


@lru_cache(maxsize=250)
def get_book_data_by_isbn(isbn: str) -> Dict[str, Any]:
    isbn_value = f'ISBN:{isbn}'
    params = {'bibkeys': isbn_value, 'jscmd': 'details', 'format': 'json'}

    response = requests.get(
        url= BASE_OPEN_LIBRARY_URL + RELATIVE_OPEN_LIBRARY_BOOKS_URL,
        params=params
    )

    book_data = response.json()[isbn_value]['details']

    return {
        'title': book_data.get('full_title') or book_data.get('title'),
        'authors_names': [author.get('name') for author in book_data.get('authors', []) if author],
        'isbn': isbn,
        'description': book_data.get('description') if isinstance(book_data.get('description'), str) else book_data.get('description', {}).get('value'),
        'published_at': parse_date(book_data.get('publish_date'))
    }
