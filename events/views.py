from django.shortcuts import render
from .models import Events

# Create your views here.
def events(request):
    template = 'events/events.html'
    events = Events.objects.all()
    context = {
        "events": events,
    }
    return render(request, template, context)