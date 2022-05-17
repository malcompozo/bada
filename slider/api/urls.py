from django.urls import path
from slider.api.views import SliderList, SliderDetail

urlpatterns = [
    path('slider/', SliderList.as_view(), name='slider'),
    path('slider/<int:pk>', SliderDetail.as_view(), name='slider-detail'),
]