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
        return '''
        mail_id: %s
        first_name: %s
        last_name: %s
        qualification: %s
        institute: %s
        mobile: %s
        location: %s
        ''' % (self.mail_id,
               self.first_name,
               self.last_name,
               self.qualification,
               self.institute,
               self.mobile,
               self.location)
