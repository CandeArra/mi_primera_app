from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .forms import SignUpForm, ProfileForm
from .models import Profile


# Vista de registro de usuario
class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login')  # Redirige al login después de un registro exitoso

    def form_valid(self, form):
        # Verificar si el nombre de usuario ya existe
        if User.objects.filter(username=form.cleaned_data['username']).exists():
            form.add_error('username', 'Este nombre de usuario ya está en uso.')
            return self.form_invalid(form)

        # Verificar si las contraseñas coinciden
        if form.cleaned_data['password1'] != form.cleaned_data['password2']:
            form.add_error('password2', 'Las contraseñas no coinciden.')
            return self.form_invalid(form)

        # Guardar el usuario
        user = form.save()

        # Iniciar sesión automáticamente
        login(self.request, user)

        # Mensaje de éxito
        messages.success(self.request, '¡Te has registrado correctamente!')

        # Redirigir al login
        return redirect(self.get_success_url())  # Redirige a la página de login

    def form_invalid(self, form):
        # Si el formulario no es válido, puedes ver los errores
        messages.error(self.request, 'Error en el registro. Verifica los datos e inténtalo de nuevo.')
        return super().form_invalid(form)


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
