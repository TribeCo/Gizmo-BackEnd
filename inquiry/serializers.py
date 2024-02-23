from rest_framework import serializers
from .models import *
#---------------------------
class ForeignOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForeignOrder
        fields = ['name','link','price','discounted','discounted_price','image','admin_checked','profit']
#---------------------------