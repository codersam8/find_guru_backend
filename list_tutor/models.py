import json

from django.db import models


class Tutor(models.Model):
    mail_id = models.EmailField()
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    qualification = models.CharField(max_length=10)
    institute = models.CharField(max_length=60)
    mobile = models.CharField(max_length=15)
    location = models.CharField(max_length=30)

    def __str__(self):
        object_dict = {
            'mail_id': self.mail_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'qualification': self.qualification,
            'institute': self.institute,
            'mobile': self.mobile,
            'location': self.location
        }
        return json.dumps(object_dict)
