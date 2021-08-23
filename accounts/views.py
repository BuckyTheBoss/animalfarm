from django.shortcuts import redirect, render
from .forms import SignupForm, MyUserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from .models import Profile

# Create your views here.

# def register(request):
#     if request.method == 'GET':
#         form = MyUserCreationForm()
#     elif request.method == 'POST':
#         form = MyUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             print(user)
            
#             return redirect('home')
           
#     return render(request, 'register.html', {'form':form})

class UserCreationView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        Profile.objects.create(user=user)
        return super().form_valid(form)

class MyLoginView(LoginView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().get(request, *args, **kwargs)
