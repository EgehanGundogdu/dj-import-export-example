from django.db import models

class Driver(models.Model):
    name = models.CharField(max_length=80)
    plate_no = models.CharField(max_length=20)
    is_banned = models.BooleanField(default=False)
    email = models.EmailField(blank=False, null=False)
    started = models.DateField()
