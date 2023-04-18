from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Tinder(models.Model):
    name = models.CharField("Название", max_length=150)
    description = models.CharField("Ваши дела", max_length=99999999)
    author = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)

class Contact(models.Model):
    mail = models.CharField("Почта", max_length=100, blank=True)
    telephone = models.CharField("Номер телефона", max_length=100)

#class Homepage(models.Model):
    