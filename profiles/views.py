from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from checkout.models import Order

# Create your views here.
def profile(request):
    template = "profiles/profiles.html"
    profile = UserProfile.objects.get(user = request.user)
    orders = Order.objects.all(user = request.user)
    
    context = {
        "profile": profile,
        "orders": orders,
    }

    return render(template, context)


def order_history(request):
    print("happidei")