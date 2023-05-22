# from typing import Any
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _

class Userprofile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    verificat = models.BooleanField(default=False)
    image = models.ImageField(upload_to='uploads/profile_images/', blank=True, null=True)

    def __str__(self):
        return self.user.username

class Customer(models.Model):
    user = models.OneToOneField(User, related_name='customer', null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=20, null=True)
    email = models.EmailField(null=False,blank=False)
    date_created = models.DateTimeField(auto_now_add=True, null=False)
    profile_pic = models.ImageField(null=True,blank=True,upload_to='uploads/profile_images/')

    def __str__(self):
        return self.user.username




# class CustomAccountManager(BaseUserManager):

#     def create_superuser(self, email, user_name, password, **other_fields):

#         other_fields.setdefault('is_staff', True)
#         other_fields.setdefault('is_superuser', True)
#         other_fields.setdefault('is_active', True)

#         if other_fields.get('is_staff') is not True:
#             raise ValueError(
#                 'Superuser are nevoie de is_staff=True.')
#         if other_fields.get('is_superuser') is not True:
#             raise ValueError(
#                 'Superuser are nevoie de is_superuser=True.')
        
#         return self.create_user(email, user_name, password, **other_fields)
    
#     def create_user(self, email, user_name, password, **other_fields):

#         if not email:
#             raise ValueError(_('Adauga o adresa de email.'))
        
#         email = self.normalize_email(email)
#         user = self.model(email=email,user_name=user_name, 
#                           **other_fields)
#         user.set_password(password)
#         user.save()
#         return user
        

# class UserBase(AbstractBaseUser, PermissionsMixin):
#     #Date cont
#     email = models.EmailField(_('email address'), unique=True)
#     user_name = models.CharField(max_length=50, unique=True)
#     first_name = models.CharField(max_length=50, blank=False)
#     last_name = models.CharField(max_length=50, blank=False)
#     #status
#     is_active = models.BooleanField(default=False)
#     verificat = models.BooleanField(default=False)
#     created = models.DateTimeField(auto_now_add=True)

#     objects = CustomAccountManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['user_name']

#     class Meta: 
#         verbose_name = "Accounts"
#         verbose_name_plural = "Accounts"

#     def __str__(self):
#         return self.user_name

admin.site.unregister(User)
# admin.site.register(User, UserBase)