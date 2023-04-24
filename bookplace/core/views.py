from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
from django.core.mail import send_mail
from django.core.paginator import Paginator
from store.models import Product

def frontpage(request):
    products = Product.objects.filter(status=Product.ACTIVE)
    p= Paginator(Product.objects.filter(status=Product.ACTIVE), 8)
    page = request.GET.get('page')
    products_list = p.get_page(page)
    nums = "a" * products_list.paginator.num_pages

    return render(request, 'core/frontpage.html', {
        'products': products,
        'products_list':products_list,
        'nums':nums
    })

def viziune(request):
    return render(request, 'core/viziune.html')

def contact(request):
    return render(request, 'core/contact.html')