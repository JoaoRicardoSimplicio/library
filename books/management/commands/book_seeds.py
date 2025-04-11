from django.core.management.base import BaseCommand

from books.seeds import seeds_local_data, seeds_online_data


class Command(BaseCommand):
    help = 'Seeds book data into database'

    def add_arguments(self, parser):
        parser.add_argument('--include-online', action='store_true', help='Seeds book data using online service')

    def handle(self, *args, **kwargs):
        include_online = kwargs.get('include_online')

        seeds_local_data()

        if include_online:
            seeds_online_data()
