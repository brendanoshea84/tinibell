from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

@staff_member_required
def big_cheese(request):

    return render(request, 'big_cheese/big_cheese.html')