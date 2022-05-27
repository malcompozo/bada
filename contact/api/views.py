from contact.models import Contact
from contact.api.serializers import ContactSerializer
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.views import APIView
from django.core.mail import EmailMessage
from badaRest.permissions import IsContactPermisions 


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
    permission_classes = [IsContactPermisions]
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
