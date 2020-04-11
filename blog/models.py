from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    image = models.ImageField(upload_to='blog/images/',blank=True)

    def __str__(self):
        return self.title