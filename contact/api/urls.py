from django.urls import path
from contact.api.views import ContactAV


urlpatterns = [
    path('contact/', ContactAV.as_view(), name='contact' ),
]