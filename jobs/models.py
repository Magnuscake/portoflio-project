from django.db import models

class Job(models.Model):
    # upload to specifies where you would like your image to
    # be saved
    # Here, files uploaded will go to the images/ folder
    image = models.ImageField(upload_to = 'images/')
    summary = models.CharField(max_length = 200)
