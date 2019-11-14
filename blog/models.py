from django.db import models
# from datetime import datetime

class Blog(models.Model):
    title = models.CharField(max_length = 100)
    publish_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = 'image/')

    def pretty_pub_date(self):
        return self.publish_date.strftime('%d %A %Y')
    
    # rename blog objects in admin page to their main title
    def __str__(self):
        return self.title

    def summary(self):
        # limit body to a certain limit; from index 0 - 100
        return self.body[:100] + "..."
