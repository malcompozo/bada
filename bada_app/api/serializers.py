from rest_framework import serializers
from bada_app.models import Contact,Estado_evento

#############################    #############################

#############################  CONTACT  #############################
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"

#############################  EVENT  #############################
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado_evento
        fields = "__all__"