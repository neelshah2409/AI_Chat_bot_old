from django.db import models
from .models import Yobotuser
from rest_framework import serializers

class YobotuserSerialize(serializers.ModelSerializer):
    class Meta:
        model = Yobotuser
        fields= ["Name","Email","CompanyName","PhoneNum"]

    def create(self, validated_data):
        return Yobotuser(**validated_data)