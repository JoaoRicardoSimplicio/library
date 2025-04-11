from django.db import models


class Author(models.Model):

    name = models.CharField(unique=True, max_length=99, null=False)

    def __str__(self):
        return self.name


class Book(models.Model):

    title = models.CharField(max_length=99, null=False)
    description = models.TextField(blank=True, null=True)
    isbn = models.CharField(unique=True, max_length=50, null=False)
    authors = models.ManyToManyField(Author, related_name='books')
    published_at = models.DateField(null=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
