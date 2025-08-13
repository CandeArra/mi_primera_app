# pages/urls.py
from django.urls import path
from .views import (
    PageListView, PageDetailView, PageCreateView, PageUpdateView, PageDeleteView
)

app_name = 'pages'

urlpatterns = [
    path('', PageListView.as_view(), name='list'),
    path('<int:pk>/', PageDetailView.as_view(), name='detail'),
    path('create/', PageCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', PageUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', PageDeleteView.as_view(), name='delete'),
]