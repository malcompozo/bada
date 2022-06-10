from rest_framework import serializers
from bada_app.models import *

#############################  CUSTOMER  #############################
class CustomerSerializers(serializers.ModelSerializer):
    event_booking = serializers.PrimaryKeyRelatedField(queryset=EventBooking.objects.all(), many=False)
    
    class Meta:
        model = Customer
        fields = "__all__"


#############################  SAVED EVENT  #############################
class EventSerializer(serializers.ModelSerializer):
    evento_reservado = CustomerSerializers(read_only=True)
    class Meta:
        model = EventBooking
        fields = "__all__"



class MailerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mailer
        fields = "__all__"





