from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import GenericView

urlpatterns = [
    # path('', index, name='home'),
    path('all/', GenericView.as_view(), name='all-list'),
]
