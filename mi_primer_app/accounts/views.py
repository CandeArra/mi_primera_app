
# accounts/views.py
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView
from django.shortcuts import redirect
from django.contrib import messages
from .forms import SignUpForm, ProfileForm
from .models import Profile
from django.shortcuts import render


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, 'Registro exitoso. ¡Bienvenida/o!')
        return redirect(self.get_success_url())

class UserLoginView(LoginView):
    template_name = 'accounts/login.html'

class UserLogoutView(LogoutView):
    pass

class ProfileDetailView(DetailView):
    template_name = 'accounts/profile_detail.html'
    context_object_name = 'profile'

    def get_object(self):
        return redirect('accounts/profile_detail')

class ProfileUpdateView(UpdateView):
    form_class = ProfileForm
    template_name = 'accounts/profile_form.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return redirect('accounts/profile_detail')

class UserPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/password_change_form.html'
    success_url = reverse_lazy('profile')

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')