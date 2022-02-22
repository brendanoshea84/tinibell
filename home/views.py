from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from django.conf import settings
from products.models import Product

# Create your views here.
def index(request):
    products = Product.objects.filter(featured=True)
    context = {
        "products": products
    }
    return render(request, 'home/index.html', context)