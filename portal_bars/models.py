from django.db import models
from django.contrib.auth.models import User




class Profile(models.Model):
    email = models.CharField('Почта', max_length=50)
    login = models.CharField('Логин', max_length=20)
    surname = models.CharField('Фамилия', max_length=50)
    name = models.CharField('Имя', max_length=50)
    password = models.CharField('Пароль', max_length=50, )


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portal/images/')
    url = models.URLField(blank=True)
