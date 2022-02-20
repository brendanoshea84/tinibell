from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.admin.views.decorators import staff_member_required
from .models import Prices, PickupLocation
from products.models import Product
from events.models import Events
from .forms import ProductForm
from django.contrib import messages


# Create your views here.

@staff_member_required
def add_product(request):
    template = 'big_cheese/add_product.html'
    form = ProductForm
    context = {
        "form": form,
    }
    return render(request, template, context)

@staff_member_required
def update_product(request):
    template = 'big_cheese/update_product.html'
    products = Product.objects.all()
    products = products.order_by("discontinued")
    form = ProductForm
    context = {
        "form": form,
        "products": products,
    }
    return render(request, template, context)


@staff_member_required
def add_event(request):

    return render(request, 'big_cheese/add_event.html')


@staff_member_required
def update_event(request):

    return render(request, 'big_cheese/update_event.html')


@staff_member_required
def site_ctrl(request):

    return render(request, 'big_cheese/site_ctrl.html')


@staff_member_required
def user_mgmt(request):

    return render(request, 'big_cheese/user_mgmt.html')


@staff_member_required
def submit_product(request, item_id):

    product = Product.objects.get(pk=item_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Damn, girl! You killin it!")
        else:
            messages.error(request, "Invalid field data.")
    form = ProductForm(initial={
        "name": product.name,
        "price": product.price,
        "description": product.description,
        "featured": product.featured,
        "nmbr_remaining": product.nmbr_remaining,
        "discontinued": product.discontinued,
        "vegan": product.vegan,
        "gluten_free": product.gluten_free,
        "nut_free": product.nut_free,
        "image_1": product.image_1,
        "image_2": product.image_2,
        "image_3": product.image_3,
    })
    context = {
        "form": form,
        "product": product,
    }

    return render(request, "big_cheese/submit_product.html", context)