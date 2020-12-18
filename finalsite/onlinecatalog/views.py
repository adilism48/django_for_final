from django.shortcuts import render

from .models import Product, Category


def index(request):
    product = Product.objects.order_by('-pub_date')
    categories = Category.objects.order_by('id')
    context = {
        'product': product,
        'title': 'Canteen online',
        'categories': categories,
    }
    return render(request, 'onlinecatalog/index.html', context)


def get_category(request, category_id):
    product = Product.objects.filter(category_id=category_id)
    categories = Category.objects.order_by('id')
    category = Category.objects.get(pk=category_id)
    context = {
        'product': product,
        'categories': categories,
        'category': category
    }
    return render(request, 'onlinecatalog/category.html', context)


def about(request):
    return render(request, 'onlinecatalog/about.html')