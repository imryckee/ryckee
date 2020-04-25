from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=500)
    text = models.TextField()
    image = models.ImageField(upload_to='blog/images/')
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.title