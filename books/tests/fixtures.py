import factory

from books.models import Author, Book


class AuthorFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Author

    name = factory.Faker('name')


class BookFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Book

    title = factory.Faker('word')
    isbn = factory.Faker('numerify', text='##########')
    description = factory.Faker('sentence')
    published_at = factory.Faker('date')
    authors = factory.RelatedFactoryList(AuthorFactory, factory_related_name='authors', size=3)

    @factory.post_generation
    def authors(self, create, authors, **kwargs):
        if not create:
            return

        if authors:
            self.authors.add(*authors)
        else:
            authors = AuthorFactory.create_batch(1)
            self.authors.add(*authors)
