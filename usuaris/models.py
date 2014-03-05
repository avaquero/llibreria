from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Perfil(models.Model):
    usuari = models.OneToOneField(User)
    
    def __unicode__(self):
        return self.usuari.username
    
from django.db.models.signals import post_save

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuari=instance)
#Cada cop es faci un save a la taula Users, s'executa create_user_profile
post_save.connect(create_user_profile, sender=User)
