from django.db import models


# Create your models here.
class UserModel(models.Model):
    class Meta:
        db_table = 'users'
        verbose_name = 'my_user'
    name = models.CharField(max_length=20)
    userName = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    age = models.IntegerField()

    def __str__(self):
        return self.name
