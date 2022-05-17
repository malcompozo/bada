from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.views import APIView

from default_event.models import EventTipe, Banquetry, Group, Site, Music, Entertainment
from default_event.api.serializers import (EventTipeSerializer, 
                                            GroupSerializer, 
                                            BanquetrySerializer, 
                                            SiteSerializer, 
                                            MusicSerializer, 
                                            EntertainmentSerializer)

#############################  ALL PREDEFINED EVENT #############################
class PredefinedEventAV(APIView):

    def get(self, request):
        predefinedEvent = EventTipe.objects.all()
        serializer = EventTipeSerializer(predefinedEvent, many=True)
        return Response(serializer.data)

#############################  DETAIL PREDEFINED EVENT #############################
class PredefinedEventDetail(APIView):
    def get(self, request, pk):
        predefinedEvent = self.get_object(pk)
        serializer = EventTipeSerializer(predefinedEvent)
        return Response(serializer.data)


#############################  DETAIL PREDEFINED EVENT #############################
class GroupAV(APIView):
    def get(self, request):
        group = Group.objects.all()
        serializer = GroupSerializer(group, many=True)
        return Response(serializer.data)

class BanquetryAV(APIView):
    def get(self, request):
        banquetry = Banquetry.objects.all()
        serializer = BanquetrySerializer(banquetry, many=True)
        return Response(serializer.data)

class SiteAV(APIView):
    def get(self, request):
        site = Site.objects.all()
        serializer = SiteSerializer(site, many=True)
        return Response(serializer.data)

class MusicAV(APIView):
    def get(self, request):
        music = Music.objects.all()
        serializer = MusicSerializer(music, many=True)
        return Response(serializer.data)

class EntertainmentAV(APIView):
    def get(self, request):
        entertainment = Entertainment.objects.all()
        serializer = EntertainmentSerializer(entertainment, many=True)
        return Response(serializer.data)

