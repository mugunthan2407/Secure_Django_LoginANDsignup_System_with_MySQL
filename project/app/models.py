from django.db import models

# Create your models here.
class User(models.Model):
    uid = models.CharField(max_length=20)
    uname = models.CharField(max_length=100)
    ucontact = models.CharField(max_length=20)
    uemail = models.EmailField()
    class meta:
        db_table = "user1"

