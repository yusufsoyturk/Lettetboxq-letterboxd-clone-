from django import forms
from .models import WatchedMovies

class WatchedMoviesForm(forms.ModelForm):
    class Meta:
        model = WatchedMovies
        fields = ['rate', 'my_review']
        
        widgets = {
            'rate': forms.NumberInput(attrs={
                'class': 'form-control', 
                'min': '1', 
                'max': '10', 
                'placeholder': 'Your rate (1-10)'
            }),
            'my_review': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 4, 
                'placeholder': 'What is your thoughts on this movie?'
            }),
        }
        
        labels = {
            'rate': 'rate',
            'my_review': 'my_review'
        }
