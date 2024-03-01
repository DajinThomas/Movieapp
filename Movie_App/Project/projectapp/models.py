from django.db import models


class Movie(models.Model):
    objects = None
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    release_date = models.DateField()
    synopsis = models.TextField()
    image_url = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.title