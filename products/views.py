from django.http import HttpRequest
from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Product
from django.contrib import messages

# Create your views here.
def products(request):
    template = 'products/products.html'
    product = Product.objects.all()
    
    context = {
        "products": product,
    }
    return render(request, template, context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    print(product.image_1)
    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)