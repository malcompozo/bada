from django.urls import path
from bada_app.api.views import EventgetAV,EventAV,CustomerAV,CustomerListAV


urlpatterns = [
    # path para eventos
    path('event/<int:search_id>', EventgetAV.as_view(), name='event' ),
    path('event/', EventAV.as_view(), name='event' ),

    # path para clientes
    path('customer/<int:pk>', CustomerAV.as_view(), name='customer' ),
    path('customers/', CustomerListAV.as_view(), name='customers' ),
]