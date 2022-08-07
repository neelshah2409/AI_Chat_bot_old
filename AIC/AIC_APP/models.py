from django.db import models

# Create your models here.

class Yobotuser(models.Model):
    Userid = models.AutoField
    Name = models.CharField(max_length=100)
    Password = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    CompanyName = models.CharField(max_length=50)
    PhoneNum = models.IntegerField(default=0)
    ChatBotName = models.CharField(max_length=50, default="")
    APIKEY = models.SlugField(max_length=200, default="")
    improvedata = models.CharField(max_length=1000, default="")
    greetmsg = models.CharField(max_length=100, default="Welcome, How can i help you")
    errmsg = models.CharField(max_length=300, default="Sorry, for more details refer our site. ")

    class Meta:
        db_table = "userdata"