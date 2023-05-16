from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Product
from userprofile.models import Customer
from django.forms import TextInput, EmailInput, PasswordInput
from django.contrib.auth.models import User



class CrateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields= ['username', 'email', 'password1', 'password2',]
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'w-100 p-3 rounded-4 border border-success shadow',
                'placeholder': 'Exemplu1234',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-100 p-3 rounded-4 border border-success shadow',
                'placeholder': 'exemplu@email.com',
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'w-100 p-3 rounded-4 border border-success shadow',
            }), 
            'password2': forms.PasswordInput(attrs={
                'class': 'w-100 p-3 rounded-4 border border-success shadow',
            }), 
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'title', 'author', 'image', 'pdf', 'editie', 'editura', 'limba', 'description',) 
        widgets = {
            'category': forms.Select(attrs={
                'class': 'w-100 p-3 rounded-4 border shadow border-success',
            }),            
            'title': forms.TextInput(attrs={
                'class': 'w-100 p-3 rounded-4 border shadow border-success',
                'placeholder': 'Adauga titlul cartii',
            }),
            'author': forms.TextInput(attrs={
                'class': 'w-100 p-3 rounded-4 border shadow border-success',
                'placeholder': 'Adauga autorul cartii',
            }),
            'description': forms.TextInput(attrs={
                'class': 'w-100 p-3 rounded-4 border shadow border-success',
                'placeholder': 'Adauga cateva cuvinte despre carte',
            }),
            'pdf': forms.FileInput(attrs={
                'class': 'w-100 p-3 rounded-4 border shadow border-success',
            }),              
            'image': forms.FileInput(attrs={
                'class': 'w-100 p-3 rounded-4 border shadow border-success',
            }),  
            'editie': forms.TextInput(attrs={
                'class': 'w-100 p-3 rounded-4 border shadow border-success',
                'placeholder': 'Adauga editia cartii',
            }),  
            'limba': forms.TextInput(attrs={
                'class': 'w-100 p-3 rounded-4 border shadow border-success',
                'placeholder': 'Adauga limba cartii',
            }),
            'editura': forms.TextInput(attrs={
                'class': 'w-100 p-3 rounded-4 border shadow border-success',
                'placeholder': 'Adauga editura cartii',
            }),                            
        }