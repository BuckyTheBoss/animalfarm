from django.db import models
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormMixin
from .models import Animal
from .forms import *
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

# CRUD
# Create Read Update Delete

#READ
def index(request):
    families = Family.objects.all()
    return render(request, 'index.html', {'families': families})

#CREATE
@login_required
def add_family(request):
    families = Family.objects.all()
    
    if request.method == 'GET':
        form = FamilyForm()
        formset = InlineAnimalFormSet()
    elif request.method == 'POST':
        form = FamilyForm(request.POST)
        if form.is_valid():
            family = form.save(commit=False)
            family.created_by = request.user.profile
            family.save()
            formset = InlineAnimalFormSet(request.POST, instance=family)
            if formset.is_valid():
                for form in formset:
                    animal = form.save(commit=False)
                    animal.created_by = request.user.profile
                    animal.save()

            return redirect('home')

    return render(request, 'add_page.html', {'families': families, 'form':form, 'formset':formset,'title':'Add Family', 'obj_type':'Family'})


#UPDATE
@login_required
def update_family(request, id):
    fam = get_object_or_404(Family, id=id)
    if request.method == 'GET':
        form = FamilyForm(instance=fam)
    elif request.method == 'POST':
        form = FamilyForm(request.POST, instance=fam)
        if form.is_valid():
            form.save()
    return render(request, 'add_page.html', {'form':form,'title':'Update Family', 'obj_type':'Family', 'my_name': 'Avi'})



class AnimalListView(ListView):
    model = Animal
    ordering = '-name'
    


class AnimalDetailView(DetailView):
    model = Animal


class AnimalCreateView(LoginRequiredMixin, CreateView):
    model = Animal
    # fields = ['name', 'legs', 'color', 'speed', 'family']
    form_class = AnimalForm
    template_name = 'add_page.html'
    success_url = reverse_lazy('all_animals')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_name'] = 'hello'
        return context
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['family'].queryset = Family.objects.filter(name__istartswith='A')
        return form
    
    def form_valid(self, form):
        animal = form.save(commit=False)
        animal.created_by = self.request.user.profile
        animal.save()
        return super().form_valid(form)


class AnimalUpdateView(LoginRequiredMixin,UpdateView):
    model = Animal
    fields = '__all__'
    # form_class = AnimalForm
    template_name = 'add_page.html'
    success_url = reverse_lazy('all_animals')


class AnimalDeleteView(LoginRequiredMixin,DeleteView):
    model = Animal
    template_name = 'delete_page.html'
    success_url = reverse_lazy('all_animals')


class AnimalsCreateView(CreateView):
    model = Animal
    form_class = InlineAnimalFormSet
    template_name = 'add_multiple_page.html'
    success_url = reverse_lazy('all_animals')

def add_multiple_animals(request):
    
    formset = AnimalFormSet(queryset=Animal.objects.none())
    # request.user.profile.animal_set.all()
    # Animal.objects.filter(created_by = request.user.profile)
    if request.method == 'POST':
        formset = AnimalFormSet(request.POST, queryset=request.user.profile.animal_set.all())
        if formset.is_valid():
            for form in formset:
                
                if form.cleaned_data:
                    animal = form.save(commit=False)
                    animal.created_by = request.user.profile
                    animal.save()
            return redirect('all_animals')
    return render(request, 'add_multiple_page.html', {'formset':formset}) 


