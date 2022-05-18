from django.urls import path
from default_event.api.views import PredefinedEventAV,PredefinedEventDetail,GroupAV,BanquetryAV,SiteAV,MusicAV,EntertainmentAV


urlpatterns = [

    # path eventos predefinidos
    path('pevent/', PredefinedEventAV.as_view(), name='predefinidos'),
    path('pevent/<int:pk>', PredefinedEventDetail.as_view(), name='predefenido-detalle'),

    # path subcampos
    path('pevent/public/', GroupAV.as_view(), name='tipo-publico'),
    path('pevent/banquetry/', BanquetryAV.as_view(), name='banqueteria'),
    path('pevent/site/', SiteAV.as_view(), name='lugar'),
    path('pevent/music/', MusicAV.as_view(), name='musica'),
    path('pevent/entertainment/', EntertainmentAV.as_view(), name='entretenimiento'),

]