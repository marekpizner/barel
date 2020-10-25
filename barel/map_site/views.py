from django.shortcuts import render
from django.http import HttpResponse
from .models import Advertise
from django.template import loader
from django.views.generic import ListView

# Create your views here.


class GenericView(ListView):
    model = Advertise
    paginate_by = 2
    # Default: <app_label>/<model_name>_list.html
    template_name = 'map_site/index.html'
    context_object_name = 'advertises'  # Default: object_list
    queryset = Advertise.objects.all()


# def index(request):
#     all_advertises = Advertise.objects.all()
#     template = loader.get_template('map_site/index.html')
#     context = {
#         'all_advertises': all_advertises,
#     }
#     return HttpResponse(template.render(context, request))
