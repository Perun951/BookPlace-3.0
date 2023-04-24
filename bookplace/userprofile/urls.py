from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('inregistrare/', views.signup, name='signup'),
    path('conectare/', auth_views.LoginView.as_view(template_name='userprofile/login.html'), name='login'),
    path('deconectare', auth_views.LogoutView.as_view(), name='logout'),
    path('contul-meu/', views.myaccount, name = 'myaccount'),
    path('magazinul-meu/',views.my_store, name='my_store'),
    path('magazinul-meu/adauga-carte/',views.add_product, name='add_product'),
    path('magazinul-meu/editeaza-carte/<int:pk>/',views.edit_product,name='edit_product'),
    path('magazinul-meu/sterge-carte/<int:pk>', views.delete_product, name='delete_product'),
    path('publishers/<int:pk>/', views.publisher_detail, name='publisher_detail'),
]