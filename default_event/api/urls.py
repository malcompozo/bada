from django.urls import path
from default_event.api.views import PredefinedEventAV


urlpatterns = [

    # path eventos predefinidos
    path('pevent/', PredefinedEventAV.as_view(), name='predefined'),

]