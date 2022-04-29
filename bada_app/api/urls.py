from django.urls import path
from bada_app.api.views import ContactAV,EventgetAV,EventAV


urlpatterns = [
    path('contact/', ContactAV.as_view(), name='contact' ),
    path('event/<int:pk>', EventgetAV.as_view(), name='event' ),
    path('event/', EventAV.as_view(), name='event' ),
]