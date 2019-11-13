from django.db import models
# from datetime import datetime

class Blog(models.Model):
    title = models.CharField(max_length = 100)
    publish_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = 'image/')
