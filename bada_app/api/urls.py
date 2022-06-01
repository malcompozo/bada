from django.urls import path
from bada_app.api.views import *


urlpatterns = [
    # path for events
    path('event/<int:search_id>/', EventgetAV.as_view(), name='event' ),
    path('event/', EventAV.as_view(), name='event' ),

    # path for costumers
    path('customer/<int:pk>/', CustomerAV.as_view(), name='customer' ),
    path('customers/', CustomerListAV.as_view(), name='customers' ),

]