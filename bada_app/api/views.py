from bada_app.models import Customer, EventBooking
from bada_app.api.serializers import CustomerSerializer,EventSerializer
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.views import APIView
from badaRest.permissions import IsAdminOrReadOnly 




#############################  CUSTOMER #############################
class CustomerAV(APIView):
    permission_classes = [IsAdminOrReadOnly]
    def get(self, request, pk):
        try:
            customer = Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CustomerSerializer(customer)
        return Response(serializer.data)


class CustomerListAV(APIView):
    permission_classes = [IsAdminOrReadOnly]
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request):
        de_serializer = CustomerSerializer(data=request.data)
        if de_serializer.is_valid():
            de_serializer.save()
            return Response(de_serializer.data, status=status.HTTP_201_CREATED)
        return Response(de_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#############################  EVENT SAVED ID #############################
class EventgetAV(APIView):
    permission_classes = [IsAdminOrReadOnly]
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
class EventAV(APIView):
    permission_classes = [IsAdminOrReadOnly]
    def get(self, request):
        events = EventBooking.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request):
        de_serializer = EventSerializer(data=request.data)
        if de_serializer.is_valid():
            de_serializer.save()
            return Response(de_serializer.data, status=status.HTTP_201_CREATED)
        return Response(de_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

