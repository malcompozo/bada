import datetime
from bada_app.models import Customer, EventBooking
from bada_app.api.serializers import *
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.views import APIView
from badaRest.permissions import IsAdminOrReadOnly 
from django.shortcuts import get_object_or_404
from django.core.mail import EmailMessage
from decouple import config
from django.template.loader import get_template


############################# CUSTOMER #############################
class CustomerAV(APIView):
    def get(self, request, pk):
        try:
            customer = Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CustomerSerializers(customer)
        return Response(serializer.data)


class CustomerListAV(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializers(customers, many=True)
        return Response(serializer.data)

    def post(self, request):
        de_serializer = CustomerSerializers(data=request.data)

        if de_serializer.is_valid():

            search_id = str(de_serializer.validated_data['event_booking'])
            name = de_serializer.validated_data['name']
            last_name = de_serializer.validated_data['last_name']
            complete_name = name + " " + last_name
            email = de_serializer.validated_data['email']
            phone = de_serializer.validated_data['phone']
            purchase_order = de_serializer.validated_data['purchase_order']
            create = datetime.date.today()

            de_serializer.save()

            event = EventBooking.objects.get(search_id=search_id)
            serializer = EventSerializer(event)
            data = serializer.data
            booking_date = data.get('booking_date')
            event_type = data.get('event_type')
            people = data.get('people')
            site = data.get('site')
            music = data.get('music')
            catering = data.get('catering')
            drinks = data.get('drinks')
            entertainment = data.get('entertainment')
            value = data.get('value')

            
            send_compra(email, 
                        complete_name, 
                        search_id, create, 
                        phone, 
                        booking_date, 
                        purchase_order,
                        event_type,
                        people,
                        site,
                        music,
                        catering,
                        drinks,
                        entertainment,
                        value)

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

            send_email(email, search_id)

            return Response(de_serializer.data, status=status.HTTP_201_CREATED)
        return Response(de_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



def send_email(email, search_id):
    html_tpl_path = 'mail/search_id.html'
    context_data = {'email': email, 
                    'search_id': search_id}

    email_html_template = get_template(html_tpl_path).render(context_data)
    correo = EmailMessage(
        "Bada Eventos: Seguimiento de evento", #ASUNTO
        email_html_template, #CUERPO
        config('EMAIL_HOST_USER'), #EMITE
        [email], #DESTINO
    )   
    correo.content_subtype = 'html' 
    correo.send()
    


# ,event_type,people,site,music,catering,drinks,entertainment,value
def send_compra(email, 
                complete_name, 
                search_id, 
                create, 
                phone, 
                booking_date, 
                purchase_order,
                event_type,
                people,
                site,
                music,
                catering,
                drinks,
                entertainment,
                value):
    html_tpl_path = 'mail/mail.html'
    context_data = {'name': complete_name, 
                    'search_id': search_id, 
                    'create': create, 
                    'booking_date': booking_date,
                    'phone': phone,
                    'purchase_order': purchase_order,
                    'event_type': event_type,
                    'people': people,
                    'site': site,
                    'music': music,
                    'catering': catering,
                    'drinks': drinks,
                    'entertainment': entertainment,
                    'value': value}

    email_html_template = get_template(html_tpl_path).render(context_data)
    correo = EmailMessage(
        "Bada Eventos: Reserva de evento", #ASUNTO
        email_html_template, #CUERPO
        config('EMAIL_HOST_USER'), #EMITE
        [email], #DESTINO
        [config('EMAIL_HOST_USER')], #EMITECOPIA
    )   
    correo.content_subtype = 'html' 
    correo.send()

