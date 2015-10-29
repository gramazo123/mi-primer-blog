from django import forms
from .models import Postear

class PostearFormulario(forms.ModelForm):
    class Meta:
        model = Postear
        fields = ('titulo', 'texto',)
