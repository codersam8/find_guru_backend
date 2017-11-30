from django.db import models


class Guru(models.Model):
    mail_id = models.EmailField()
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    qualification = models.CharField(max_length=10)
    institute = models.CharField(max_length=60)
    mobile = models.CharField(max_length=15)
    location = models.CharField(max_length=30)
