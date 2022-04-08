from django.db import models


# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    published = models.BooleanField(default=False)
    date = models.DateField(blank=True)
    content = models.TextField()
    description = models.TextField()


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
    price = models.DecimalField(blank=True, null=True)
    summary = models.TextField(blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True)
    category = models.CharField(max_length=30, blank=True, choices=GENRES)
    stock = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.title
