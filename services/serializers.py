from rest_framework.serializers import ModelSerializer
from .models import *

class BookingSerializer(ModelSerializer):
    class Meta:
        model= Booking
        fields= ["customer","extra_kms","extra_hours","rate_days","rate_km","rate_hours","running_days"]
     
class BookingInternalSerializer(ModelSerializer):
    class Meta:
        model= Booking
        fields= "__all__"  
        