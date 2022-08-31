from turtle import title
from django.db import models

class Post(models.Model):
    title=models.CharField(max_length=150)
    
    def __str__(self) :
        return self.title
    cover = models.ImageField(upload_to="media", null=True,blank=True)
    image1 = models.ImageField(upload_to="media", null=True,blank=True)
    image2 = models.ImageField(upload_to="media", null=True,blank=True)


