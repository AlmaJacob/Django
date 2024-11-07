from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_name=models.TextField()
    bg_image=models.FileField()
    fg_image=models.FileField()
    time_duration=models.TextField()
    category=models.TextField()
    date=models.DateField()
    def __str__(self):
     return self.movie_name

class Lang(models.Model):
    language=models.TextField()

class movie_lang(models.Model):
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    lang= models.ForeignKey(Lang,on_delete=models.CASCADE)       