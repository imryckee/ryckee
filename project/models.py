from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=300)
    text = models.TextField()
    image = models.ImageField(upload_to='project/images/')
    date = models.DateField()
    live = models.URLField(blank=True)
    github = models.URLField(blank=True)

    def __str__(self):
        return self.title