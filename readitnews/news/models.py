from django.db import models

from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    published_date = models.DateField()
    image_url = models.URLField()

    def __str__(self):
        return self.title

