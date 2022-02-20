from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

@staff_member_required
def add_product(request):

    return render(request, 'big_cheese/add_product.html')

@staff_member_required
def update_product(request):

    return render(request, 'big_cheese/update_product.html')

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