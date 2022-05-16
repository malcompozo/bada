from rest_framework import serializers
from bada_app.models import Contact,EventBooking,Customer, Banquetry, Site, Music, Toys, EventTipe

#############################  CONTACT  #############################
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"

#############################  SAVED EVENT  #############################
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventBooking
        fields = "__all__"

#############################  CUSTOMER  #############################
class CustomerSerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True)
    class Meta:
        model = Customer
        fields = "__all__"

#############################  EVENTOS PREDEFINIDOS  #############################
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
    banquetry = BanquetrySerializer(read_only=True)
    site = SiteSerializer(read_only=True)
    music = MusicSerializer(read_only=True)
    toys = ToysSerializer(read_only=True)

    class Meta:
        model = EventTipe
        fields = "__all__"
