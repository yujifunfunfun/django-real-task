from django.db import models

class UrlList(models.Model):
    url_list = models.CharField(max_length=100)
