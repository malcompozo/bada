from rest_framework import serializers
from bada_app.models import *



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

#############################  CUSTOMER  #############################
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

#############################  SAVED EVENT  #############################
class EventSerializer(serializers.ModelSerializer):
    site = SiteSerializer(read_only=True)
    music = MusicSerializer(read_only=True)
    catering = CateringSerializer(read_only=True)
    drinks = DrinksSerializers(read_only=True)
    entertainment = EntertainmentSerializer(read_only=True)
    customer = CustomerSerializer(read_only=True)
    class Meta:
        model = EventBooking
        fields = "__all__"





