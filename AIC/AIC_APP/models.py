from django.db import models

# Create your models here.
class Question_ans(models.Model):
    id = models.AutoField
    questions = models.TextField(max_length=500, unique=True, null=True)

