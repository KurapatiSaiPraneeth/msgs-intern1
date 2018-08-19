from django.db import models

# Create your models here.
class Author(models.Model):
    author_name=models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.author_name)

class Book(models.Model):
    book_name=models.CharField(max_length=50)
    author=models.ManyToManyField(Author)

    def __str__(self):
        return "{}".format(self.book_name)        


