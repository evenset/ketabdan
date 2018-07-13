from django.db import models
from django.contrib.auth.models import User 

class ShortStory(models.Model):
    PUBLICATION_STATUS =(
        ('dr', 'Draft'),
        ('p' , 'Published'),
        ('b' , 'Banned'),
        ('de', 'Deleted'),
    )
    author = models.ForeignKey(User,on_delete = models.CASCADE) 
    title = models.CharField(max_length = 500)
    status = models.CharField(max_length = 1, choices = PUBLICATION_STATUS)
    publication_date = models.DateField()