from django import forms
from .models import TVShow, Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'stars']

class Movie(forms.ModelForm):
    class Meta:
        model = TVShow
        fields = ['title', 'description', 'release_date', 'rating']
