from django.db import models


# Create your models here.


class Logen (models.Model):
    usernam = models.CharField(max_length=50)
    email = models.CharField(max_length=1001)
    txte = models.TextField(blank=True , null=True)
    activ = models.BooleanField(default=True)

    def __str__(self):
        return self.usernam


class Show (models.Model):
    facebook = models.CharField(max_length=50 , blank=True , null=True)
    twitter = models.CharField(max_length=50 , blank=True , null=True)
    gmail = models.CharField(max_length=50 , blank=True , null=True)

    def __str__(self):
        return self.facebook
