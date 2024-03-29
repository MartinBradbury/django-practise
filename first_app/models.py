from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Test(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.title
    
class Space(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    status = models.IntegerField()
    flagged = models.BooleanField()

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'