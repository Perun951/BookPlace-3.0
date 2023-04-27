from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Count, Avg

from .models import Product, Category, Review

def recomandari(request):
    products = Product.objects.filter(status=Product.ACTIVE)

    return render(request, 'store/recom.html', {
        'products': products,
    })

def nr_rev(request):
    products = Product.objects.annotate(num_reviews=Count('reviews')).order_by('-num_reviews')
    return render(request, 'store/nr_rev.html', {
        'products': products,
        })

def nr_down(request):
    products = Product.objects.annotate(downs=Count('downloads')).order_by('-downs')

    return render(request, 'store/nr_down.html', {
        'products': products,
    })

def nota(request):
    products = Product.objects.annotate(avg_reviews=Avg('reviews__rating')).order_by('-avg_reviews')

    return render(request, 'store/nota.html', {
        'products': products,
    })

def validate_file_extension(value):
    if not value.name.endswith('.pdf'):
        raise ValidationError(u'Error message')
   
def search(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(status=Product.ACTIVE).filter(
        Q(title__icontains=query)
        | 
        Q(author__icontains=query)
        )

    return render(request, 'store/search.html',{
        'query': query,
        'products': products,
    })

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.filter(status=Product.ACTIVE)
    p = Paginator(Product.objects.all(), 8)
    page = request.GET.get('page')
    products_list = p.get_page(page)
    nums = "a" * products_list.paginator.num_pages

    return render(request, 'store/category_detail.html', {
        'category': category,
        'products': products,
        'products_list':products_list,
        'nums':nums
    })

def product_detail(request, category_slug, slug,):
    product = get_object_or_404(Product, slug=slug, status=Product.ACTIVE)

    if request.method == 'POST':
        rating = request.POST.get('rating',5)
        content = request.POST.get('content','')

        if content:
            reviews = Review.objects.filter(created_by=request.user, product=product)
            if reviews.count() > 0:
                reviews = reviews.first()
                reviews.rating = rating
                reviews.content = content
                reviews.save()
            else:
                review = Review.objects.create(
                    product= product,
                    rating = rating,
                    content = content,
                    created_by = request.user
                )

            return redirect('product_detail', category_slug=category_slug, slug=slug)

    return render(request, 'store/product_detail.html', {
        'product': product
    })
    
