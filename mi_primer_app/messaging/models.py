from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')  # Remitente
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')  # Destinatario
    body = models.TextField()  # Cuerpo del mensaje
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación
    read = models.BooleanField(default=False)  # Estado de lectura

    class Meta:
        ordering = ['-created_at']  # Ordena los mensajes por fecha descendente

    def __str__(self):
        return f'{self.sender} → {self.recipient} ({self.created_at:%Y-%m-%d %H:%M})'  # Representación del mensaje
