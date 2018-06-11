from django.db import models

# Create your models here.

# Models are like the colums
class Author(models.Model):
    name = models.CharField(max_length=254, blank=False)
    email = models.EmailField(max_length=100, blank=False)
#the below makes the titles of the above show in the admin area of the project   
    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    author = models.ForeignKey(Author, null=False, related_name="books")
#the below makes the titles of the books show in the admin area of the project   
    def __str__(self):
        return self.name
        
