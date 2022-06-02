from rest_framework import serializers
from default_event.models import *


#############################  EVENTOS PREDEFINIDOS  #############################

class CateringSerializer(serializers.ModelSerializer):
    # AQUI AGREGAR RELACION DE TABLA
    class Meta:
        model = Catering
        fields = "__all__"

class DrinksSerializers(serializers.ModelSerializer):
    # AQUI AGREGAR RELACION DE TABLA
    class Meta:
        model = Drinks
        fields = "__all__"

class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = "__all__"

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = "__all__"

class EntertainmentSerializer(serializers.ModelSerializer):
    # AQUI AGREGAR RELACION DE TABLA
    class Meta:
        model = Entertainment
        fields = "__all__"
        
class EventTypeSerializer(serializers.ModelSerializer):
    site = SiteSerializer(read_only=True)
    music = MusicSerializer(read_only=True)
    event_catering = CateringSerializer(many=True, read_only=True)
    event_drinks = DrinksSerializers(many=True, read_only=True)
    event_entertainment = EntertainmentSerializer(many=True, read_only=True)

    class Meta:
        model = EventType
        fields = "__all__"