from django.db import models
from AIC.AIC_API.models import Api
from rest_framework import serializers

class ApiSerialize(serializers.Serializer):
    user_id = serializers.ForeignKey("AIC_APP.Yobotuser", on_delete=models.CASCADE)
    api_key = serializers.ForeignKey("rest_framework_api_key.APIKey", primary_key=True, on_delete=models.CASCADE)
    active = serializers.BooleanField(default=False)
    def create(self, validated_data):
        return Api(**validated_data)