from django.contrib import admin

# from .models import CustomAccountManager
# from .models import UserBase

# admin.site.register(UserBase)
# admin.site.register(CustomAccountManager)


from .models import Customer
from .models import Userprofile
# from .models import CustomUserManager

admin.site.register(Userprofile)
admin.site.register(Customer)
# admin.site.register(CustomUserManager)