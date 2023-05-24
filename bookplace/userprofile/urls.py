from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('inregistrare/', views.signup, name='signup'),
    # path('conectare/', auth_views.LoginView.as_view(template_name='userprofile/login.html'), name='login'),
    path('conectare/', views.LogIn, name='login'),
    path('deconectare', auth_views.LogoutView.as_view(), name='logout'),
    path('contul-meu/', views.myaccount, name = 'myaccount'),
    path('magazinul-meu/',views.my_store, name='my_store'),
    path('magazinul-meu/adauga-carte/',views.add_product, name='add_product'),
    path('magazinul-meu/editeaza-carte/<int:pk>/',views.edit_product,name='edit_product'),
    path('magazinul-meu/sterge-carte/<int:pk>', views.delete_product, name='delete_product'),
    path('publishers/<int:pk>/', views.publisher_detail, name='publisher_detail'),
    
    # path('reset_parola/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    # path('reset_parola_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    # path('reset_parola_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

    # Wishlist
    path('favorite/adauga/<int:id>', views.add_to_wishlist, name='user_wishlist'),
    path('favorite/', views.wishlist, name='wishlist'),

]