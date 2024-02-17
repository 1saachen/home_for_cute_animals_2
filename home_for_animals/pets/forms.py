from django import forms
from .models import Pet

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'avatar', 'breed', 'distribution', 'weight', 'health_status']
