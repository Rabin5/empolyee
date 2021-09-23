from rest_framework import serializers
from .models import Empolyee


class EmpolyeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empolyee
        fields = '__all__'
