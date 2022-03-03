from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    template = "profiles/profile.html"
    profile = UserProfile.objects.get(user = request.user)
    orders = Order.objects.filter(user_profile = profile)
    form = UserProfileForm

    context = {
        "profile": profile,
        "orders": orders,
    }

    return render(request, template, context)


@login_required
def order_history(request):
    print("happidei")