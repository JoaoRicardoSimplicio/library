from django.db import models


class Book(models.Model):

    title = models.CharField(max_length=99, null=False)
    description = models.TextField(blank=True, null=True)
    isbn = models.CharField(unique=True, max_length=50, null=False)
    published_at = models.DateField()

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Author(models.Model):

    name = models.CharField(max_length=99, null=False)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name
