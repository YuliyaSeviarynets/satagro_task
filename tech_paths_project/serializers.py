from rest_framework import serializers
from .models import ABLine


class ABLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ABLine
        fields = '__all__'
