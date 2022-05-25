from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import generics, status, viewsets
from rest_framework.views import APIView

from default_event.models import EventType, Catering, Drinks, Group, Site, Music, Entertainment
from default_event.api.serializers import (EventTypeSerializer, 
                                            GroupSerializer, 
                                            CateringSerializer, 
                                            DrinksSerializers,
                                            SiteSerializer, 
                                            MusicSerializer, 
                                            EntertainmentSerializer)

#############################  LIST AND DETAIL PREDEFINED EVENT #############################

class PredefinedEventVS(viewsets.ViewSet):
    def list(self, request):
        queryset = EventType.objects.all()
        serializer = EventTypeSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = EventType.objects.all()
        event_type = get_object_or_404(queryset, pk=pk)
        serializer = EventTypeSerializer(event_type)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = EventTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        try:
            event_type = EventType.objects.get(pk=pk)
        except EventType.DoesNotExist:
            return Response({'ERROR':'Empresa no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        serializer = EventTypeSerializer(event_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#############################  DETAIL ITEMS PREDEFINED EVENT #############################
class GroupAV(APIView):
    def get(self, request):
        group = Group.objects.all()
        serializer = GroupSerializer(group, many=True)
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

#############################  DETAIL PREDEFINED EVENT FOR MODEL #############################

class CateringAV(generics.ListCreateAPIView):
    serializer_class = CateringSerializer
    def get_queryset(self):
        return Catering.objects.filter(eventType=self.kwargs['pk'])
    
class CateringList(APIView):
    def get(self, request, pk):
        catering = Catering.objects.filter(pk=pk)
        serializer = CateringSerializer(catering, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        catering = Catering.objects.get(pk=pk)
        serializer = CateringSerializer(catering, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DrinksAV(generics.ListCreateAPIView):
    serializer_class = DrinksSerializers
    def get_queryset(self):
        return Drinks.objects.filter(eventType=self.kwargs['pk'])

class DrinksList(APIView):
    def get(self, request, pk):
        drinks = Drinks.objects.filter(pk=pk)
        serializer = DrinksSerializers(drinks, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        drinks = Drinks.objects.get(pk=pk)
        serializer = DrinksSerializers(drinks, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EntertainmentAV(generics.ListCreateAPIView):
    serializer_class = EntertainmentSerializer
    def get_queryset(self):
        return Entertainment.objects.filter(eventType=self.kwargs['pk'])

class EntertainmentList(APIView):
    def get(self, request, pk):
        entertainment = Entertainment.objects.filter(pk=pk)
        serializer = EntertainmentSerializer(entertainment, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        entertainment = Entertainment.objects.get(pk=pk)
        serializer = EntertainmentSerializer(entertainment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

