from rest_framework import serializers
from default_event.models import Group, Banquetry, Site, Music, Toys, EventTipe


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

class ToysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Toys
        fields = "__all__"
        
class EventTipeSerializer(serializers.ModelSerializer):
    group = GroupSerializer(read_only=True)
    banquetry = BanquetrySerializer(read_only=True)
    site = SiteSerializer(read_only=True)
    music = MusicSerializer(read_only=True)
    toys = ToysSerializer(read_only=True)

    class Meta:
        model = EventTipe
        fields = "__all__"