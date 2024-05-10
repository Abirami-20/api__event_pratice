from rest_framework import serializers
from .models import CollegeEvent,Register
class CollegeEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model=CollegeEvent
        fields="__all__"

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Register
        fields="__all__"
