from rest_framework import serializers
from default_event.models import Group, Banquetry, Site, Music, Entertainment, EventTipe


#############################  EVENTOS PREDEFINIDOS  #############################
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"

class BanquetrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Banquetry
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
        
class EventTipeSerializer(serializers.ModelSerializer):
    group = GroupSerializer(read_only=True)
    banquetry = BanquetrySerializer(read_only=True)
    site = SiteSerializer(read_only=True)
    music = MusicSerializer(read_only=True)
    toys = EntertainmentSerializer(read_only=True)

    class Meta:
        model = EventTipe
        fields = "__all__"