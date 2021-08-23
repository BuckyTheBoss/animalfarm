from django.shortcuts import redirect, render
from .forms import ProfileForm, SignupForm, MyUserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from .models import Profile
from django.contrib.auth import authenticate, login

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
    form_class = MyUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_form'] = ProfileForm()
        return context

    def form_valid(self, form):
        profile_form = ProfileForm(self.request.POST)
        if profile_form.is_valid():
            new_user = form.save()
            print(form.cleaned_data)
            profile = profile_form.save(commit=False)
            profile.user = new_user
            profile.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            print(user)
            if user:
                login(self.request, user)
                print('logged in')
            return redirect('home')
        else:
            return self.form_invalid(form)

class MyLoginView(LoginView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().get(request, *args, **kwargs)
