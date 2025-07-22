from django.db import models

class BookAuthor(models.Model):
    first_name = models.CharField(max_length=256, null=False)
    last_name = models.CharField(max_length=256, null=True)
    bio = models.TextField()

class Book(models.Model):
    title = models.CharField(max_length=512)
    authors = models.ManyToManyField(BookAuthor)
