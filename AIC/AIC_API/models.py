from django.db import models
from AIC_APP.models import Yobotuser
from rest_framework_api_key.models import APIKey

class Api(models.Model):
    user_id = models.ForeignKey("AIC_APP.Yobotuser", on_delete=models.CASCADE)
    api_key = models.ForeignKey("rest_framework_api_key.APIKey", on_delete=models.CASCADE)
    active = models.BooleanField(default=False)

    class Meta:
        db_table = "AIC_API"
