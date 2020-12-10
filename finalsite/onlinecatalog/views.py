from django.shortcuts import render

from .models import Product


def index(request):
    product = Product.objects.order_by('-pub_date')
    context = {
        'product': product,
        'title': 'Canteen online'
    }
    return render(request, 'onlinecatalog/index.html', context)
