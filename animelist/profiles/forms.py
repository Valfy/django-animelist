from django import forms
from .models import AnimeProfile


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = AnimeProfile
        fields = ('username', 'avatar')