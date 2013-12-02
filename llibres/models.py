from django.db import models

class Genere(models.Model):
    nom = models.CharField(max_length=200, unique =  True, help_text = "Nom del genere")
    
    def __unicode__(self):
        return self.nom
    
class Titol(models.Model):
    titol = models.CharField(max_length=200, unique = True, help_text = "Titol del llibre")
    sinopsis = models.CharField(max_length=500)
    genere = models.ForeignKey(Genere)
    
    def __unicode__(self):
        return self.titol
    
class Llibre(models.Model):
    idioma = models.CharField(max_length=200)
    isbn = models.BigIntegerField(max_length=13)
    edicio = models.CharField(max_length=50)
    editorial = models.CharField(max_length=200)
    titol = models.ForeignKey(Titol)
    
    def __unicode__(self):
        return self.titol