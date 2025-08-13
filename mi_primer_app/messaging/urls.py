# messaging/urls.py
from django.urls import path
from .views import InboxView, NewMessageView

app_name = 'messaging'
urlpatterns = [
    path('', InboxView.as_view(), name='inbox'),
    path('new/', NewMessageView.as_view(), name='new'),
]
