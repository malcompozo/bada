from rest_framework import serializers
from default_event.models import Group, Catering, Drinks, Site, Music, Entertainment, EventType


#############################  EVENTOS PREDEFINIDOS  #############################
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"

class CateringSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catering
        fields = "__all__"

class DrinksSerializers(serializers.ModelSerializer):
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
    class Meta:
        model = Entertainment
        fields = "__all__"
        
class EventTypeSerializer(serializers.ModelSerializer):
    group = GroupSerializer(read_only=True)
    catering = CateringSerializer(read_only=True)
    drinks = DrinksSerializers(read_only=True)
    site = SiteSerializer(read_only=True)
    music = MusicSerializer(read_only=True)
    entertainment = EntertainmentSerializer(read_only=True)

    class Meta:
        model = EventType
        fields = "__all__"