from rest_framework import serializers
from bada_app.models import *




#############################  SAVED EVENT  #############################
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventBooking
        fields = "__all__"

#############################  CUSTOMER  #############################
class CustomerSerializers(serializers.ModelSerializer):
    event = EventSerializer(many=True, read_only=True)
    class Meta:
        model = Customer
        fields = "__all__"

class MailerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mailer
        fields = "__all__"





