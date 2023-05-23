from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Product
from userprofile.models import Customer
from django.forms import TextInput, EmailInput, PasswordInput, ModelForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'w-100 p-3 rounded-4 border border-success shadow',
                'placeholder': 'Exemplu1234',
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'w-100 p-3 rounded-4 border border-success shadow',
            }),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'w-100 p-3 rounded-4 border-0 shadow', 'placeholder': 'Introdu numele de utilizator',})
        self.fields['password'].widget.attrs.update({'class': 'w-100 p-3 rounded-4 border-0 shadow', 'placeholder': 'Introdu parola',})

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user','verificat']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-30 p-3 rounded-4 border border-success shadow',
                'placeholder': 'Exemplu1234',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'w-30 p-3 rounded-4 border border-success shadow',
                'placeholder': '0000 000 000'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-30 p-3 rounded-4 border border-success shadow',
                'placeholder': 'exemplu@email.com',
            }),
            'profile_pic': forms.FileInput(attrs={
                'class': 'w-30 p-3 rounded-4 border shadow border-success',
            }), 
        }

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
                'type': 'password',
                'class': 'w-100 p-3 rounded-4 border border-success shadow',
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'w-100 p-3 rounded-4 border border-success shadow',
            }), 
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'w-100 p-3 rounded-4 border-0 shadow', 'placeholder': 'Creaza o parola',})
        self.fields['password2'].widget.attrs.update({'class': 'w-100 p-3 rounded-4 border-0 shadow', 'placeholder': 'Reintrodu parola',})

# class CrateUserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields= ['username', 'email', 'password1', 'password2',]
#         widgets = {
#             'username': forms.TextInput(attrs={
#                 'class': 'w-100 p-3 rounded-4 border border-success shadow',
#                 'placeholder': 'Exemplu1234',
#             }),
#             'email': forms.EmailInput(attrs={
#                 'class': 'w-100 p-3 rounded-4 border border-success shadow',
#                 'placeholder': 'exemplu@email.com',
#             }),
#             'password1': forms.PasswordInput(attrs={
#                 'type': 'password',
#                 'class': 'w-100 p-3 rounded-4 border border-success shadow',
#             }),
#             'password2': forms.PasswordInput(attrs={
#                 'class': 'w-100 p-3 rounded-4 border border-success shadow',
#             }), 
#         }
    
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['password1'].widget.attrs.update({'class': 'w-100 p-3 rounded-4 border-0 shadow', 'placeholder': 'Creaza o parola',})
#         self.fields['password2'].widget.attrs.update({'class': 'w-100 p-3 rounded-4 border-0 shadow', 'placeholder': 'Reintrodu parola',})

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

