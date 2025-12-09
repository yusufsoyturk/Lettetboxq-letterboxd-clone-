from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Movies, WatchedMovies
from .forms import WatchedMoviesForm
from django.contrib import messages

def showMain(request):
    return render(request, 'copyletter/home_v1.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  
    else:
        form = UserCreationForm()
        
    return render(request, 'registration/signup.html', {'form': form})

def movie_list(request):
    movies = Movies.objects.all().order_by('rate_mean')

    context = {
        'movies' : movies,
    }

    return render(request, 'copyletter/movies.html', context)

@login_required
def add_watched_movie(request, movie_id):
    movie = get_object_or_404(Movies, id=movie_id)
    
    if request.method == 'POST':
        form = WatchedMoviesForm(request.POST)

        if WatchedMovies.objects.filter(username=request.user, movies=movie).exists():
            messages.info(request, "You watched before!")
            return redirect('movie_list')
        
        if form.is_valid():
            instance = form.save(commit=False)
            instance.username = request.user
            instance.movies = movie
            
            instance.save()
            return redirect('movie_list')
    else:
        form = WatchedMoviesForm()

    return render(request, 'copyletter/add_review.html', {'form': form, 'movie': movie})

@login_required
def profile_view(request):
    user_reviews = WatchedMovies.objects.filter(username=request.user).select_related('movies').order_by('-id')
    
    return render(request, 'copyletter/profile.html', {'reviews': user_reviews})

def reviews_view(request):
    all_reviews = WatchedMovies.objects.select_related('username', 'movies').all().order_by('-id')
    
    return render(request, 'copyletter/reviews.html', {'reviews': all_reviews})

@login_required
def delete_review(request, review_id):
    review_entry = get_object_or_404(WatchedMovies, id=review_id)
    
    if review_entry.username == request.user:
        review_entry.delete()
        messages.success(request, "The movie entry has been successfully deleted from your profile and the database.")
    else:
        messages.error(request, "You are not authorized to delete this entry!")
    return redirect(request.META.get('HTTP_REFERER', 'profile'))