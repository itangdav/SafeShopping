from django.db import models


class Post(models.Model):
    address = models.CharField(max_length=300)

