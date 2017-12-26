from django.db import models


class Tutor(models.Model):
    mail_id = models.EmailField()
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    qualification = models.CharField(max_length=10)
    institute = models.CharField(max_length=60)
    mobile = models.CharField(max_length=15)
    location = models.CharField(max_length=30)
