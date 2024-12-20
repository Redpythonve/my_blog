from django.db import models
from datetime import date

# Create your models here.
class Author(models.Model):
      name = models.CharField(max_length=15)
      email = models.EmailField(max_length=254)
      
      def __str__(self):
            return self.name

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    headline = models.CharField(max_length=100)
    content = models.TextField()
    public_date = models.DateField(default=date.today)
    rating = models.IntegerField(default=5)
    

    def __str__(self):
        return self.headline