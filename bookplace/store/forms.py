from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'title', 'author', 'image', 'pdf', 'editie', 'editura', 'limba', 'description',) 
        widgets = {
            'category': forms.Select(attrs={
                'class': 'w-100 p-3 rounded-4 border border-success'
            }),            
            'title': forms.TextInput(attrs={
                'class': 'w-100 p-3 rounded-4 border border-success'
            }),
            'author': forms.TextInput(attrs={
                'class': 'w-100 p-3 rounded-4 border border-success'
            }),
            'description': forms.TextInput(attrs={
                'class': 'w-100 p-3 rounded-4 border border-success'
            }),
            'pdf': forms.FileInput(attrs={
                'class': 'w-100 p-3 rounded-4 border border-success'
            }),              
            'image': forms.FileInput(attrs={
                'class': 'w-100 p-3 rounded-4 border border-success'
            }),  
            'editie': forms.TextInput(attrs={
                'class': 'w-100 p-3 rounded-4 border border-success'
            }),  
            'limba': forms.TextInput(attrs={
                'class': 'w-100 p-3 rounded-4 border border-success'
            }),
            'editura': forms.TextInput(attrs={
                'class': 'w-100 p-3 rounded-4 border border-success'
            }),                            
        }