from django.shortcuts import (
                        render,
                        get_object_or_404,
                        redirect,
                        reverse,
                        HttpResponse
                        )
from products.models import Product
from django.contrib import messages

from django.core.mail import send_mail



# Create your views here.
def view_bag(request):
    # send_mail(
    #     'Subject here',
    #     'Here is the message. Get that on your dicko, bucko.',
    #     'info@tinibell.com',
    #     ['jdygard@gmail.com'],
    #     fail_silently=False,
    # )
    bag = request.session.get('bag', {})
    template = "bag/bag.html"
    context = {
        "bag": bag
    }
    return render(request, template, context)

def add_to_bag(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, f'Added {product.name} to your bag')
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')
    
    request.session['bag'] = bag
    return redirect(redirect_url)

def adjust_bag(request, item_id):

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request,
                            (f'Updated {product.name} '
                            f'quantity to {bag[item_id]}'))
    else:
        bag.pop(item_id)
        messages.success(request,
                            (f'Removed {product.name} '
                            f'from your bag'))

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))

def remove_from_bag(request, item_id):
    
    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})

        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)