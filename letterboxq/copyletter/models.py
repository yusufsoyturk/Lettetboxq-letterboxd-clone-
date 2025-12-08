from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Movies(models.Model):
    movie_name = models.CharField(max_length=100, unique=True)
    released_year = models.IntegerField(blank=True, null=True)
    tmdb_id = models.IntegerField(unique=True)

    summary = models.TextField(null=True, blank=True)
    poster_url = models.URLField(max_length=500, null=True, blank=True)
    rate_mean = models.FloatField(null=True, blank=True)
    
    def __str__(self):
        return self.movie_name

class WatchedMovies(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='watched_movies')
    movies = models.ForeignKey(Movies, on_delete=models.CASCADE, related_name='watcher')
    watching_date = models.DateField(auto_now_add=True)
    rate = models.IntegerField(blank=True, null=True)

    class Meta:
        unique_together = ('username', 'movies')
    
    def __str__(self):
        return f"{self.username} watched {self.movies.movie_name}"
    



