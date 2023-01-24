from django.db import models
from django.core.validators import MinValueValidator


class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    @property
    def count_movies(self):
        return self.director_movies.count()


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    duration = models.FloatField(default=0, validators=[MinValueValidator(0.0)])
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='director_movies', null=True)

    def __str__(self):
        return self.title

    @property
    def rating(self):
        count = self.movie_reviews.count()
        if count == 0:
            return 0
        total = 0
        for i in self.movie_reviews.all():
            total += i.stars
        return total/count


CHOICES = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5)
)


class Review(models.Model):
    text = models.TextField()
    stars = models.IntegerField(choices=CHOICES, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_reviews', null=True)
