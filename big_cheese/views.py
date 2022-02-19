from django.shortcuts import render
from django.contrib.auth import is_superuser

# Create your views here.
@is_superuser
def big_cheese(request):

    return render(request, 'big_cheese/big_cheese.html')