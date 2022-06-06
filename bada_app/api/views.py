from bada_app.models import Customer, EventBooking
from bada_app.api.serializers import *
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.views import APIView
from badaRest.permissions import IsAdminOrReadOnly 
from django.shortcuts import get_object_or_404
from django.core.mail import EmailMessage
from decouple import config


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

        name = de_serializer.validated_data['name']
        email = de_serializer.validated_data['email']
        created = de_serializer.validated_data['created']
        event_booking = de_serializer.validated_data['event_booking']


        if de_serializer.is_valid():

            send_compra(email,name,created,event_booking)

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

class MailAV(APIView):
    def get(self, request):
        customers = Mailer.objects.all()
        serializer = MailerSerializers(customers, many=True)
        return Response(serializer.data)

    def post(self, request):
        de_serializer = MailerSerializers(data=request.data)
        if de_serializer.is_valid():

            email = de_serializer.validated_data['email']
            search_id = de_serializer.validated_data['search_id']

            de_serializer.save()
            #FUNCION DE CORREO AUTOMATICO

            send_email(email, search_id)

            return Response(de_serializer.data, status=status.HTTP_201_CREATED)
        return Response(de_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def send_email(email, search_id):
    # envio de correo y redireccion
    correo = EmailMessage(
        "Bada Eventos: Nuevo mensaje", # asunto
        "Estimado {}\n \n Su código de evento es: {}. \n \n Use este código para pagar o modificar el evento elegido. \n \n Atte. equipo Bada Eventos.-".format(email, search_id), # cuerpo del mail
        config('EMAIL_HOST_USER'), # email que emite
        [email], # email de destino
    )
    correo.send()    

def send_compra(email,name,created,event_booking):
    correo = EmailMessage(
        "Bada Eventos: Reserva de evento", # asunto
        "Estimado {}\n \n Su código de evento es: {}. \n \n Creado el día {} \n \n Atte. equipo Bada Eventos. \n \n Para mas información contacte al 999-999-99 .-".format(name, event_booking, created), # cuerpo del mail
        config('EMAIL_HOST_USER'), # email que emite
        [email], # email de destino
    )    
    correo.send()

