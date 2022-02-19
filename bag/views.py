from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from django.contrib import messages

# Create your views here.
def view_bag(request):
    return render(request, "bag/bag.html")

def add_to_bag(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, f'Added {product.name} to your bag')
        print("seven")
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')
        print("seven")
    
    request.session['bag'] = bag
    return redirect(redirect_url)

def adjust_bag(request):
    print(request)

def remove_from_bag(request):
    print(request)