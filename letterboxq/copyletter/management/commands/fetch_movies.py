import requests
from django.core.management.base import BaseCommand
from django.conf import settings
from copyletter.models import Movies

class Command(BaseCommand):
    help = 'Fetches popular movies from the TMDB API and saves them to the database.'

    def handle(self, *args, **options):
        url = f"https://api.themoviedb.org/3/movie/popular?api_key={settings.TMDB_API_KEY}&language=en-US&page=1"
        
        response = requests.get(url)
        data = response.json()
        
        if response.status_code != 200:
            self.stdout.write(self.style.ERROR('API request failed!'))
            return

        movies_count = 0
        for film_data in data.get('results', []):
            try:
                title = film_data.get('title')
                tmdb_id = film_data.get('id')
                
                Movies.objects.update_or_create(
                    tmdb_id=tmdb_id,
                    defaults={
                        'movie_name': title,
                        'summary': film_data.get('overview'),
                        'released_year': int(film_data.get('release_date', '0000')[:4]) if film_data.get('release_date') else None,
                        'rate_mean': film_data.get('vote_average'),
                        'poster_url': f"https://image.tmdb.org/t/p/w500{film_data.get('poster_path')}" if film_data.get('poster_path') else None,
                    }
                )
                movies_count += 1

            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Movie save error ({title}): {e}'))
                continue

        self.stdout.write(self.style.SUCCESS(f'Successfully saved/updated {movies_count} movies.'))