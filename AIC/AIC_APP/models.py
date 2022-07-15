from django.db import models

# Create your models here.
class Question_ans(models.Model):
    id = models.AutoField
    questions = models.TextField(max_length=255, unique=True, null=True)

class Yobotuser(models.Model):
    Userid = models.AutoField
    Name = models.CharField(max_length=100)
    Password = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    CompanyName = models.CharField(max_length=50)
    PhoneNum = models.IntegerField(default=0)
    ChatBotName = models.CharField(max_length=50, default="")
    class Meta:
        db_table = "userdata"