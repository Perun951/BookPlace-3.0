from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect

from .decorators import allowed_user
from .models import Customer

from store.models import Product
from store.forms import ProductForm, CrateUserForm, LoginForm, CustomerForm
from store.models import Product, Category


@login_required(login_url='login')
def add_to_wishlist(request, id):
    product = get_object_or_404(Product, id=id)
    if product.users_wishlist.filter(id=request.user.id).exists():
        product.users_wishlist.remove(request.user)
    else:
        product.users_wishlist.add(request.user)
    return HttpResponseRedirect(request.META["HTTP_REFERER"])


@login_required(login_url='login')
def wishlist(request):
    products = Product.objects.filter(users_wishlist=request.user)

    return render(request, 'userprofile/favorite.html',{
        'wishlist': products,
    })


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
    customer = request.user.customer
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
    return render(request, 'userprofile/myaccount.html',{
        'form': form
    })

def LogIn(request):
    if request.user.is_authenticated:
        return redirect('frontpage')
    else:
        if request.method == 'POST':
            form = LoginForm(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                User = authenticate(request, username=username, password=password)
                if User is not None:
                    login(request, User)
                    return redirect('frontpage')
                else:
                    messages.info(request, 'Nume sau parola sunt invalide')
        else:
            form = LoginForm()
        return render(request, 'userprofile/login.html',{'form': form})

def signup(request):
    if request.user.is_authenticated:
        return redirect('frontpage')
    else:
        form = CrateUserForm()
        if request.method=='POST':
            form = CrateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username=form.cleaned_data.get('username')
                Customer.objects.create(
                    user=user,
                    name=user.username,
                    email=user.email,
                    )
                messages.success(request, 'Contul '+username+' a fost creat')
                return redirect('login')
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

