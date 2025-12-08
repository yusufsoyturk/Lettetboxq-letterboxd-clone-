from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Movies

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




