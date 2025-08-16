from django.db import models
from django.contrib.auth.models import User
from django import forms

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'birthdate', 'link']

    avatar = forms.ImageField(required=False)  
    bio = forms.CharField(widget=forms.Textarea, required=False)
    birthdate = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2025)), required=False)
    link = forms.URLField(required=False)

