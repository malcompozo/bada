from rest_framework import serializers
from bada_app.models import Contact,Event,Slider

#############################  SLIDER  #############################
class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = "__all__"

#############################  CONTACT  #############################
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"

#############################  EVENT  #############################
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"