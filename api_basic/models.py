from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.title 
