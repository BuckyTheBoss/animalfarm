from django import forms
from .models import Family, Animal

class FamilyForm(forms.ModelForm):
    class Meta:
        model = Family
        fields = ['name']

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'