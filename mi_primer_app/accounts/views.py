from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import SignUpForm, ProfileForm

class UserRegisterView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("login")  
    def form_valid(self, form):
        user = form.save()  # guarda el usuario con contraseña 
        messages.success(self.request, "¡Tu cuenta fue creada con éxito! Ahora inicia sesión.")
        return super().form_valid(form)
    
# Vista de inicio de sesión
class UserLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'accounts/login.html'

    def get_success_url(self):
        return reverse_lazy('profile')  # Redirige al perfil después de iniciar sesión


# Vista de cierre de sesión
class UserLogoutView(LogoutView):
    template_name = 'accounts/login.html'

# Vista para ver el perfil
class ProfileDetailView(DetailView):
    template_name = 'accounts/profile_detail.html'
    context_object_name = 'profile'

    def get_object(self):
        return self.request.user.profile  # Devuelve el perfil del usuario autenticado


# Vista de perfil (solo para usuarios autenticados)
@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


@login_required
def profile_edit(request):
    user_profile = request.user.profile

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=user_profile)

        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, '¡Tu perfil ha sido actualizado correctamente!')
            return redirect('profile')  # Redirige al perfil después de editar

    else:
        profile_form = ProfileForm(instance=user_profile)

    return render(request, 'accounts/profile_edit.html', {
        'profile_form': profile_form,
    })


@login_required
def change_password(request):
    if request.method == 'POST':
        password_form = PasswordChangeForm(user=request.user, data=request.POST)

        if password_form.is_valid():
            password_form.save()
            update_session_auth_hash(request, password_form.user)  # Mantiene la sesión abierta
            messages.success(request, '¡Tu contraseña ha sido cambiada correctamente!')
            return redirect('profile')  # Redirige al perfil después de cambiar la contraseña

    else:
        password_form = PasswordChangeForm(user=request.user)

    return render(request, 'accounts/change_password.html', {
        'password_change_form': password_form,
    })


