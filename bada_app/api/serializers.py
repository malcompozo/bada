from rest_framework import serializers
from bada_app.models import EventBooking,Customer


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


