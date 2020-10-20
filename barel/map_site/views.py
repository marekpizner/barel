from django.shortcuts import render
from django.http import HttpResponse
from .models import Advertise
from django.template import loader

# Create your views here.


def index(request):
    all_advertises = Advertise.objects.all()
    template = loader.get_template('map_site/index.html')
    context = {
        'all_advertises': all_advertises,
    }
    return HttpResponse(template.render(context, request))
