from django.urls import path

from . import views 

urlpatterns = [
    path('recomadari/', views.recomandari, name='recomandari'),
    path('nr-reviewuri/', views.nr_rev, name='nr_rev'),
    path('nota/', views.nota, name='nota'),
    path('search/', views.search, name='search'),
    path('<slug:slug>/', views.category_detail, name='category_detail'),
    path('<slug:category_slug>/<slug:slug>/', views.product_detail, name='product_detail'),
]