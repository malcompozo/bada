from django.urls import path
from bada_app.api.views import ContactAV,EventgetAV,EventAV,CustomerAV,CustomerListAV,PredefinedEventAV


urlpatterns = [
    path('contact/', ContactAV.as_view(), name='contact' ),

    # path para eventos
    path('event/<int:search_id>', EventgetAV.as_view(), name='event' ),
    path('event/', EventAV.as_view(), name='event' ),

    # path eventos predefinidos
    path('pevent/', PredefinedEventAV.as_view(), name='predefined'),

    # path para clientes
    path('customer/<int:pk>', CustomerAV.as_view(), name='customer' ),
    path('customers/', CustomerListAV.as_view(), name='customers' ),
]