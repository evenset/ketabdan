from django.db import models
from django.conf import settings

class ShortStory(models.Model):
     PUBLICATION_STATUS =(
        ('dr', 'Draft'),
        ('p' , 'Published'),
        ('b' , 'Banned'),
        ('de', 'Deleted'),
    )

    author = models.Foreignkey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
    title = models.CharField(max_length = 500)
    body = models.CharField(min_length = 3500)
    status = models.CharField(max_length = 1, choices = PUBLICATION_STATUS)
    publication_date = models.DateField()
