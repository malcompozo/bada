from bada_app.models import Customer, EventBooking
from bada_app.api.serializers import *
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.views import APIView
from badaRest.permissions import IsAdminOrReadOnly 
from django.shortcuts import get_object_or_404



############################# CUSTOMER #############################
class CustomerAV(APIView):
    permission_classes = [IsAdminOrReadOnly]
    def get(self, request, pk):
        try:
            customer = Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CustomerSerializers(customer)
        return Response(serializer.data)


class CustomerListAV(APIView):
    #permission_classes = [IsAdminOrReadOnly]
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializers(customers, many=True)
        return Response(serializer.data)

    def post(self, request):
        de_serializer = CustomerSerializers(data=request.data)
        if de_serializer.is_valid():
            de_serializer.save()
            return Response(de_serializer.data, status=status.HTTP_201_CREATED)
        return Response(de_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#############################  EVENT SAVED ID #############################
class EventgetAV(APIView):
    #permission_classes = [IsAdminOrReadOnly]
    def get(self, request, search_id):
        try:
            event = EventBooking.objects.get(search_id=search_id)
        except EventBooking.DoesNotExist:
            return Response({'ERROR ':' Evento no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = EventSerializer(event)
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            event = EventBooking.objects.get(pk=pk)
        except EventBooking.DoesNotExist:
            return Response({'ERROR ':' Evento no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

############################# ALL EVENT SAVED  #############################

class EventAV(viewsets.ViewSet):
    #permission_classes = [IsAdminOrReadOnly]
    def list(self, request):
        queryset = EventBooking.objects.all()
        serializer = EventSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = EventBooking.objects.all()
        event_type = get_object_or_404(queryset, pk=pk)
        serializer = EventSerializer(event_type)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        try:
            event_type = EventBooking.objects.get(pk=pk)
        except EventBooking.DoesNotExist:
            return Response({'ERROR':'Empresa no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        serializer = EventSerializer(event_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


############################# WEBPAY #############################
