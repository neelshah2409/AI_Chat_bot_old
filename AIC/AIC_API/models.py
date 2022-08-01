from django.db import models
from AIC_APP.models import Yobotuser
from rest_framework_api_key.models import APIKey

class Api(models.Model):
    user_id = models.ForeignKey("AIC_APP.Yobotuser", on_delete=models.CASCADE)
    api_key_id = models.ForeignKey("rest_framework_api_key.APIKey",unique=True, on_delete=models.CASCADE)
    api_key = models.SlugField(max_length=255,unique=True)
    active = models.BooleanField(default=False)
    name = models.TextField(max_length=255,default="Public Api")
    class Meta:
        db_table = "AIC_API"
