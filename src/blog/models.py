from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=36)
    slug = models.SlugField()

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)


class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    published = models.BooleanField(default=False)
    date = models.DateField(blank=True, null=True)
    content = models.TextField()
    description = models.TextField()

    def number_of_words(self):
        return len(self.content.split())


class Author(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    wikipedia = models.URLField(blank=True)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"


class Book(models.Model):
    ADVENTURE = "AV"
    THRILLER = "TR"
    FANTASY = "FS"
    ROMANCE = "RM"
    HORROR = "HR"
    SCIENCE_FICTION = "SF"

    GENRES = [
        (ADVENTURE, "Aventure"),
        (THRILLER, "Thriller"),
        (FANTASY, "Fantastique"),
        (ROMANCE, "Romance"),
        (HORROR, "Horreur"),
        (SCIENCE_FICTION, "Science-fiction"),
    ]
    title = models.CharField(max_length=100)
    price = models.FloatField(blank=True, null=True)
    summary = models.TextField(blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True)
    category = models.CharField(max_length=30, blank=True, choices=GENRES)
    stock = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.title
