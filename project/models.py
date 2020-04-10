from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='project/images/')
    live = models.URLField(blank=True)
    github = models.URLField(blank=True)