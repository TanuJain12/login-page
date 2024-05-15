from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

class MyLoginView(LoginView):
    template_name = 'registration/login.html'
