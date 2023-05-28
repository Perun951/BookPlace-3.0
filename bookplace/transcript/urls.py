from django.urls import path

from . import views

urlpatterns = [
    path('ai/voce/', views.index, name='index')
]