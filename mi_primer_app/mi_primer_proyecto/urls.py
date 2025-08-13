from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('peliculas.urls')),   # ya lo tenés (home + about)
    path('pages/', include('pages.urls')), # listado/detalle/CRUD de pages
   # path('accounts/', include('accounts.urls')),  # login, signup, perfil
    #path('messages/', include('messaging.urls')), # mensajería
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)