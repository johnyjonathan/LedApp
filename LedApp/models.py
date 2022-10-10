from email.policy import default
from django.db import models

class settings(models.Model):
    name = models.CharField(max_length=100)
    led_num = models.IntegerField(default=24)
    bright = models.FloatField(default = 1.0)
    max_led_num = models.IntegerField(default = 100)

