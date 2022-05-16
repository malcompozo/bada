from bada_app.models import Contact, Customer, EventBooking, EventTipe
from bada_app.api.serializers import ContactSerializer, CustomerSerializer,EventSerializer, EventTipeSerializer
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.views import APIView
from django.core.mail import EmailMessage
from rest_framework.permissions import IsAuthenticated



#############################  EMAIL  #############################
def send_email(name, email, message):
    print (name, email, message)
    # envio de correo y redireccion
    correo = EmailMessage(
        "Bada Eventos: Nuevo mensaje de {}".format(email), # asunto
        "De {} \n \nCorreo <{}> \n \nEscribió: \n \n{} ".format(name, email, message), # cuerpo del mail
        "no_contestar@badaeventos.cl", # email que emite
        ["eventos@bada.cl"], # email de destino
        reply_to=[email] # responder al email de forma dinamica
    )
    correo.send()

#############################  CONTACT  #############################
class ContactAV(APIView):

    def get(self, request):
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)

    def post(self, request):
        de_serializer = ContactSerializer(data=request.data)
        if de_serializer.is_valid():

            name = de_serializer.validated_data['name']
            email = de_serializer.validated_data['email']
            message = de_serializer.validated_data['message']

            de_serializer.save()
            send_email(name, email, message)
            return Response(de_serializer.data, status=status.HTTP_201_CREATED)
        return Response(de_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#############################  CUSTOMER #############################

class CustomerAV(APIView):

    def get(self, request, pk):
        try:
            customer = Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def post(self, request):
        de_serializer = CustomerSerializer(data=request.data)
        if de_serializer.is_valid():
            de_serializer.save()
            return Response(de_serializer.data, status=status.HTTP_201_CREATED)
        return Response(de_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerListAV(APIView):

    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

#############################  EVENT SAVED ID #############################
class EventgetAV(APIView):

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

#############################  PREDEFINED EVENT #############################

class PredefinedEventAV(APIView):

    def get(self, request):
        predefinedEvent = EventTipe.objects.all()
        serializer = EventTipeSerializer(predefinedEvent, many=True)
        return Response(serializer.data)
