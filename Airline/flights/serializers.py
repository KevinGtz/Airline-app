from rest_framework import serializers
from .models import Flight


class FlihgtSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flight
        fields = '__all__'
