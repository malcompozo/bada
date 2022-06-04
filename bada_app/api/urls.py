from django.urls import include, path
from bada_app.api.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('event', EventAV, basename='pevent')

urlpatterns = [
    # path for events
    path('', include(router.urls)),

    # path for event
    path('event/<int:search_id>/', EventgetAV.as_view(), name='event' ),

    # path for costumers
    path('customer/<int:pk>/', CustomerAV.as_view(), name='customer' ),
    path('customers/', CustomerListAV.as_view(), name='customers' ),

]