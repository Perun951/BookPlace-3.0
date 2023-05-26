from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _


class Customer(models.Model):
    user = models.OneToOneField(User, related_name='customer', null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=20, null=True)
    email = models.EmailField(null=False,blank=False)
    date_created = models.DateTimeField(auto_now_add=True, null=False)
    profile_pic = models.ImageField(default="Sample_User_Icon.png", null=True,blank=True,upload_to='uploads/profile_images/')

    def __str__(self):
        return self.user.username

admin.site.unregister(User)