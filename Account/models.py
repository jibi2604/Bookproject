from django.db import models


# Create your models here.

class CreateUserProfile(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    cpassword = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.username)

