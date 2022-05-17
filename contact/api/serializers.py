from rest_framework import serializers
from contact.models import Contact

#############################  CONTACT  #############################
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"