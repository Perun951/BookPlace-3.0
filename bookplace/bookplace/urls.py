from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from core.views import frontpage, contact, viziune

urlpatterns = [

    path('contact/',contact,name='contact'),
    path('viziune/',viziune,name='viziune'),
    path('admin/', admin.site.urls),
    path('', include('userprofile.urls')),
    path('', include('store.urls')),
    path('',frontpage,name='frontpage'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

