from django.http import HttpRequest
from django.shortcuts import render, HttpResponse
from .models import Product, ProductImage

# Create your views here.
def products(request):
    template = 'products/products.html'
    product = Product.objects.all()
    image = ProductImage.objects.all()
    context = {
        "products": product,
        "images": image,
    }
    return render(request, template, context)

def product_detail(request):
    return HttpResponse("Product details")