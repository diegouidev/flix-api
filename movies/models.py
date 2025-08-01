from django.db import models
from genres.models import Genre
from actors.models import Actor

# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=500)
    release_date = models.DateField(null=True, blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name='movies')
    actors = models.ManyToManyField(Actor, related_name='movies')
    sinopsis = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['release_date']