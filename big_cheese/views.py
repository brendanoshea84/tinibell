from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.admin.views.decorators import staff_member_required
from .models import Prices, PickupLocation
from products.models import Product, Control
from events.models import Events
from .forms import (
    ProductForm,
    EventsForm,
    ControlForm,
    PickupLocationForm,
)
from django.contrib import messages


@staff_member_required
def add_product(request):
    template = 'big_cheese/add_product.html'
    form = ProductForm
    context = {
        "form": form,
    }

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Damn, girl! That pasta smellin' good AF!")
        else:
            messages.error(request, "Invalid field data.")
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
def submit_product(request, item_id):

    product = Product.objects.get(pk=item_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Nothing beside remains. Round the decay Of that colossal Wreck, boundless and bare The lone and level sands stretch far away.”")
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


@staff_member_required
def add_event(request):
    template = 'big_cheese/add_event.html'
    form = EventsForm
    context = {
        "form": form,
    }

    if request.method == "POST":
        form = EventsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "History shall smile upon events such as these.")
        else:
            messages.error(request, "Invalid field data.")
    
    return render(request, template, context)


@staff_member_required
def update_event(request):

    events = Events.objects.all()
    template = 'big_cheese/update_event.html'

    context = {
        "events": events,
    }

    return render(request, template, context)


def submit_event(request, item_id):

    event = Events.objects.get(pk=item_id)
    template = "big_cheese/submit_event.html"

    if request.method == "POST":
        form = EventsForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, "Change is inevitible in these trying times.")
        else:
            messages.error(request, "Invalid field data.")

    form = EventsForm(initial={
        "name": event.name,
        "label": event.label,
        "description": event.description,
        "image_1": event.image_1,
        'date': event.date,
    })

    context = {
        "form": form,
        "event": event,
    }

    return render(request, template, context)

@staff_member_required
def site_ctrl(request):
    control = Control.objects.get(pk=1)
    form = ControlForm(initial={
        "no_orders": control.no_orders
    })
    if request.method=="POST":
        form = ControlForm(request.POST, instance=control)
        if form.is_valid():
            form.save()
            messages.success(request, "They do not deserve the bounty of your kitchen; let them starve.")
        else:
            messages.error(request, "If you're seeing this error, something crazy happened. Call Joel if it happens more than once.")
    context = {
        "form": form,
    }
    return render(request, 'big_cheese/site_ctrl.html', context)


@staff_member_required
def pickup_location(request):
    template= "big_cheese/pickup_location.html"
    locations = PickupLocation.objects.all()
    context = {
        "locations": locations,
    }

    return render(request, template, context)


@staff_member_required
def update_location(request, item_id):
    template= "big_cheese/update_location.html"
    location = PickupLocation.objects.get(pk=item_id)
    form = PickupLocationForm(initial={
        "name": location.name,
        "label": location.label,
        "postcode": location.postcode,
        "town_or_city": location.town_or_city,
        "street_address1": location.street_address1,
        "street_address2": location.street_address2,
        "active": location.active,
        "description": location.description,
    })
    if request.method=="POST":
        form = PickupLocationForm(request.POST, instance=location)
        if form.is_valid():
            form.save()
            messages.success(request, "Do not tarry, times are changing.")
        else:
            messages.error(request, "I think you filled something out wrong and the validator missed it. Try again.")

    context = {
        "location": location,
        "form": form
    }

    return render(request, template, context)


@staff_member_required
def add_location(request):
    template= "big_cheese/add_location.html"
    form = PickupLocationForm
    context = {
        "form": form,
    }
    if request.method == "POST":
        form = PickupLocationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "The quest is set, and the adventure underway.")
        else:
            messages.error(request, "I think you filled something out wrong and the validator missed it. Try again.")

    return render(request, template, context)


@staff_member_required
def user_mgmt(request):

    return render(request, 'big_cheese/user_mgmt.html')
