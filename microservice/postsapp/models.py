from django.db import models


class Post(models.Model):
    userId = models.IntegerField(default=1)
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=500)
