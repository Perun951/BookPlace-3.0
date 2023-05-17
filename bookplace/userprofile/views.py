from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.text import slugify
from django.core.paginator import Paginator
from .decorators import allowed_user

from .models import Userprofile, Customer
from store.models import Product

from store.forms import ProductForm, CrateUserForm, LoginForm
from store.models import Product, Category

def publisher_detail(request, pk):
    user = User.objects.get(pk=pk)
    products = user.products.filter(status=Product.ACTIVE)
    p= Paginator(Product.objects.all(), 8)
    page = request.GET.get('page')
    products_list = p.get_page(page)
    nums = "a" * products_list.paginator.num_pages

    return render(request, 'userprofile/publisher_detail.html', {
        'user': user,
        'products':products,
        'products_list':products_list,
        'nums':nums
    })

@login_required(login_url='login')
def my_store(request):
    products = request.user.products.exclude(status=Product.DELETED)
    p= Paginator(request.user.products.exclude(status=Product.DELETED), 8)
    page = request.GET.get('page')
    products_list = p.get_page(page)
    nums = "a" * products_list.paginator.num_pages

    return render(request, 'userprofile/my_store.html',{
        'products': products,
        'products_list':products_list,
        'nums':nums
    })



@login_required(login_url='login')
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            title = request.POST.get('title')
            
            product = form.save(commit=False)
            product.user = request.user
            product.slug = slugify(title)
            product.save()
            messages.success(request, 'Cartea a fost adaugata!')

            return redirect('my_store')
    else:
        form = ProductForm()

    form = ProductForm()

    return render(request, 'userprofile/product_form.html', {
        'title': 'Adauga carte',
        'form': form
    })


@login_required(login_url='login')
def edit_product(request, pk):
    product = Product.objects.filter(user=request.user).get(pk=pk)

    if request.method == 'POST':
        form=ProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            form.save()

            messages.success(request, 'Cartea a fost modificata!')

            return redirect('my_store')
    else:
        form=ProductForm(instance=product)

    return render(request, 'userprofile/product_form.html', {
        'title': 'Editare carte',
        'product': product,
        'form': form
    })

    
@login_required(login_url='login')
def delete_product(request, pk):
    product = Product.objects.filter(user=request.user).get(pk=pk)
    product.status = Product.DELETED
    product.save()

    messages.success(request, 'Cartea a fost stearsa!')

    return redirect('my_store')

@login_required(login_url='login')
def myaccount(request):
    return render(request, 'userprofile/myaccount.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        User = authenticate(request, username=username, password=password)
        if User is not None:
            login(request,User)
            return redirect('frontpage')
        else: 
            messages.info(request, 'Numele de utilizator sau parola sunt incorecte')
        return render(request, 'userprofile/login.html', {
        })
    return render(request, 'userprofile/login.html', {
    })

def signup(request):
    form = CrateUserForm()
    if request.method=='POST':
        form = CrateUserForm(request.POST)
        if form.is_valid():
            User = form.save()
            login(request, User)
            return redirect('frontpage')
    return render(request, 'userprofile/signup.html',{
        'form': form
    })
    # if request.method == 'POST':

    #     if form.is_valid():
    #         user = form.save()

    #         login(request, user)

    #         Customer = Customer.objects.create(user=user)

    #         return redirect('frontpage')
    # else:
    #     form = CrateUserForm()

    return render(request, 'userprofile/signup.html',{
        'form': form
    })

