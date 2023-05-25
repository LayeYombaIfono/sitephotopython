#portation des model

from django.contrib.auth.models import AbstractUser
from django.db import models

#réation des classes

class User(AbstractUser):

    CREATOR = 'CREATOR'
    SUBSCRIBER = 'SUBSCRIBER'

#creaton de role

ROLE_CHOICES = (
    (CREATOR, 'créateur'),
    (SUBSCRIBER, 'Abonné'),
)
profile_photo = models.ImageField(verbose_name='Photo de profil')
role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Rôle')