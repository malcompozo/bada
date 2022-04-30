from rest_framework import serializers
from bada_app.models import Contact,EstadoEvento

#############################    #############################

#############################  CONTACT  #############################
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"

#############################  EVENT  #############################
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoEvento
        fields = "__all__"