from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Userprofile

class UserprofileLoginForm(AuthenticationForm):
    verificat = forms.BooleanField(required=True)
    class Meta:
        model = Userprofile
        fields = ('Nume utilizato', 'Parola', 'Confirma parola',)