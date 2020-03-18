from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from usermanage.models import user
from usermanage.forms import UserForm, LoginForm
from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, 'index.html')

class SignupView(CreateView):
    model=user
    redirect_field_name='index.html'
    form_class=UserForm

class LoginView(DetailView):
    model=user
    redirect_field_name='index.html'
    form_class=LoginForm
