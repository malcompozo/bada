from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.views import APIView

from default_event.models import EventTipe
from default_event.api.serializers import EventTipeSerializer

#############################  PREDEFINED EVENT #############################


class PredefinedEventAV(APIView):

    def get(self, request):
        predefinedEvent = EventTipe.objects.all()
        serializer = EventTipeSerializer(predefinedEvent, many=True)
        return Response(serializer.data)
