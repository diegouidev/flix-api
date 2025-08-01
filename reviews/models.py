from django.db import models
from movies.models import Movies
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.PROTECT, related_name='reviews')
    stars = models.IntegerField(validators=[MinValueValidator(1, 'Avaliação mínima é 1'), MaxValueValidator(5, 'Avaliação máxima é 5')])
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.movie.title} - {self.stars} stars"
