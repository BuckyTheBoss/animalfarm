from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import Animal
from .forms import *
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
# Create your views here.

# CRUD
# Create Read Update Delete

#READ
def index(request):
    families = Family.objects.all()
    return render(request, 'index.html', {'families': families})

#CREATE
def add_family(request):
    if request.method == 'GET':
        form = FamilyForm()
    elif request.method == 'POST':
        form = FamilyForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'add_page.html', {'form':form,'title':'Add Family', 'obj_type':'Family'})

#UPDATE
def update_family(request, id):
    fam = get_object_or_404(Family, id=id)
    if request.method == 'GET':
        form = FamilyForm(instance=fam)
    elif request.method == 'POST':
        form = FamilyForm(request.POST, instance=fam)
        if form.is_valid():
            form.save()

    return render(request, 'add_page.html', {'form':form,'title':'Update Family', 'obj_type':'Family'})



class AnimalListView(ListView):
    model = Animal
    ordering = '-name'

class AnimalDetailView(DetailView):
    model = Animal


class AnimalCreateView(CreateView):
    model = Animal
    fields = '__all__'
    # form_class = AnimalForm
    template_name = 'add_page.html'
    success_url = reverse_lazy('all_animals')


class AnimalUpdateView(UpdateView):
    model = Animal
    fields = '__all__'
    # form_class = AnimalForm
    template_name = 'add_page.html'
    success_url = reverse_lazy('all_animals')