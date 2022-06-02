from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from default_event.api.views import (PredefinedEventVS,
                                    CateringAV,
                                    CateringList,
                                    DrinksAV, 
                                    DrinksList,
                                    SiteAV,
                                    MusicAV,
                                    EntertainmentAV,
                                    EntertainmentList)

router = DefaultRouter()
router.register('p-event', PredefinedEventVS, basename='pevent')

urlpatterns = [

    # path eventos predefinidos
    path('', include(router.urls)),

    # path subcampos
    path('pevent/site/', SiteAV.as_view(), name='lugar'),
    path('pevent/music/', MusicAV.as_view(), name='musica'),


    path('pevent/<int:pk>/catering/', CateringAV.as_view(), name='banqueteria'), #GET ALL DETAIL PEVENT
    path('pevent/catering/<int:pk>', CateringList.as_view(), name='banqueteria'), # GET, PUT CATERING

    path('pevent/<int:pk>/drinks/', DrinksAV.as_view(), name='bebidas'), #GET ALL DETAIL PEVENT
    path('pevent/drinks/<int:pk>', DrinksList.as_view(), name='bebidas'), #GET, PUT DRINKS

    path('pevent/<int:pk>/entertainment/', EntertainmentAV.as_view(), name='entretenimiento'), #GET ALL DETAIL PEVENT
    path('pevent/entertainment/<int:pk>', EntertainmentList.as_view(), name='entretenimiento'), #GET, PUT ENTERTAINMENT

]