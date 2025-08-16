from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('profile/', views.ProfileDetailView.as_view(), name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),  # Vista de editar perfil
    path('profile/change-password/', views.change_password, name='change_password'),  # Vista de cambiar contraseña
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    