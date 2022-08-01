from django.db import models
from AIC_API.models import Api
from rest_framework import serializers

class ApiSerialize(serializers.ModelSerializer):
    class Meta:
        model = Api
        fields= "__all__"

    def create(self, validated_data):
        return Api(**validated_data)