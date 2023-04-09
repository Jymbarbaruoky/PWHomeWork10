from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=25, null=False, unique=True, blank=False)

    def __str__(self):
        return f"{self.name}"


class Author(models.Model):
    fullname = models.CharField(max_length=100, null=False, unique=True)
    born_date = models.CharField(max_length=50)
    born_location = models.CharField(max_length=100)
    description = models.CharField(max_length=5000)

    def __str__(self):
        return f"{self.fullname}"


class Quote(models.Model):
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='quotes', blank=False)
    quote = models.CharField(max_length=5000, null=False)

    def __str__(self):
        return f"{self.quote}"
