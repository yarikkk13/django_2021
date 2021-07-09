from django.db import models


# Create your models here.
class UserModel(models.Model):
    name = models.CharField(max_length=20)
    userName = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
