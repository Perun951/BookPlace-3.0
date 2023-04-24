from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Userprofile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    verificat = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

# class CustomUserManager(UserManager):
#     def _create_user(self,email,password,**extra):
#         if not email:
#             raise ValueError("Adresa email nu este valida.")
        
#         email=self.normalize_email(email)
#         user=self.model(email=email,**extra)
#         user.set_password(password)
#         user.save(using=self._db)

#         return user

#     def create_user(self, email=None,password=None, **extra):
#         extra.setdefault('is_staff',False)
#         extra.setdefault('is_superuser',False)
#         return self._create_user(email, password, **extra)

#     def create_superuser(self, email=None,password=None, **extra):
#         extra.setdefault('is_staff',True)
#         extra.setdefault('is_superuser',True)
#         return self._create_user(email, password, **extra)

# class User(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(blank=False,null=False, default='',unique=True)
#     name = models.CharField(max_length=50, blank=True, default='')

#     is_active = models.BooleanField(default=True)
#     is_superuser = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)

#     date_joined = models.DateTimeField(default=timezone.now)
#     last_login = models.DateTimeField(blank=True, null=True)

#     objects = CustomUserManager()

#     USERNAME_FIELD = 'email'
#     EMAIL_FIELS = 'email'
#     REQUIRED_FIELDS= []

#     class Meta:
#         verbose_name='User'
#         verbose_name_plural='Users'

#     def get_full_name(self):
#         return self.name

#     def get_short_name(self):
#         return self.name or self.email.split('@')[0]