from django import forms
from .models import Family, Animal
from django.forms import modelformset_factory, inlineformset_factory, widgets

class FamilyForm(forms.ModelForm):
    # age = forms.IntegerField(widget=forms.NumberInput(attrs={'onclick':'alert()'}))
    class Meta:
        model = Family
        fields = ['name']
        labels = {
            'name': 'Family Name'
        }
        

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        exclude = ['created_by']
        widgets = {
            'name': forms.TextInput(attrs={})
        }


AnimalFormSet = modelformset_factory(Animal, form=AnimalForm, extra=0)
InlineAnimalFormSet = inlineformset_factory(Family, Animal, form=AnimalForm, extra=0)
