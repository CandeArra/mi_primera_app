from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Message
from .forms import MessageForm

# Vista para mostrar la bandeja de entrada (todos los mensajes del usuario como remitente o destinatario)
class InboxView(LoginRequiredMixin, ListView):
    model = Message  # Modelo de mensaje
    template_name = 'messaging/inbox.html' 
    context_object_name = 'messages_list' 

    def get_queryset(self):
        u = self.request.user  # Obtener el usuario logueado
        return Message.objects.filter(recipient=u) | Message.objects.filter(sender=u)

# Vista para enviar un nuevo mensaje
class NewMessageView(LoginRequiredMixin, CreateView):
    form_class = MessageForm  
    template_name = 'messaging/new_message.html'  
    success_url = reverse_lazy('messaging:inbox')  # Redirige a la bandeja de entrada al enviar el mensaje

    def form_valid(self, form):
        obj = form.save(commit=False)  
        obj.sender = self.request.user  
        obj.save() 
        messages.success(self.request, 'Mensaje enviado.')  
        return super().form_valid(form)  