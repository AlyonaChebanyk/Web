from django.db import models
from django.conf import settings


class Article(models.Model):
    q = models.CharField(max_length=25)
    author = models.CharField(max_length=40, null=True)
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=500)
    url_to_image = models.URLField(null=True)
    published_at = models.DateField()
    content = models.CharField(max_length=5000)

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
