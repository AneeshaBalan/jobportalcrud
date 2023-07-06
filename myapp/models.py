from django.db import models

# Create your models here.

class Jobportal(models.Model):
    username=models.CharField(max_length=260)
    qualification=models.CharField(max_length=260)
    age=models.PositiveIntegerField()
    experience=models.CharField(max_length=200)
    currenlty_working=models.BooleanField(default=False)


def _str_(self):
    return self.username