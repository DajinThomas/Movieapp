# movies/forms.py
from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie # Name of the database means model name going to edit.
        fields = ['title', 'genre', 'release_date', 'synopsis', 'image_url'] # fields need to edit in the database
