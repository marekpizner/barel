from django.shortcuts import render
from django.http import HttpResponse
from .models import Advertise
from django.template import loader
from django.views.generic import ListView
import os
# Create your views here.


class GenericView(ListView):
    model = Advertise
    paginate_by = 2
    # Default: <app_label>/<model_name>_list.html
    template_name = 'map_site/index.html'
    context_object_name = 'advertises'  # Default: object_list
    queryset = Advertise.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mapbox_key'] = os.environ['MAPBOX_KEY']
        return context
