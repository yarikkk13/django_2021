from django.db import models


# Create your models here.
class UserModel(models.Model):
    class Meta:
        db_table = 'users'
    name = models.CharField(max_length=20)
    userName = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    age = models.IntegerField()
