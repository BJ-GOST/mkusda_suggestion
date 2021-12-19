from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
class suggestion(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
	contact = models.IntegerField(default=+254734567890)
	transport = models.IntegerField(default=1500)
	site = models.CharField(default='propossed mission site', max_length=250)
	field = models.CharField(default='site conference', max_length=250)

