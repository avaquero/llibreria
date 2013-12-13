# -*- coding: utf8 -*-
from models.llibres import Genere
from models.llibres import Titol
from models.llibres import Llibre
from django.contrib.auth.models import User
from usuaris.models import Perfil

def crea():
    pepe_usr = User.objects.create( XXXXX )
    jose_usr = User.objects.create( XXXXX )
    pepa_usr = User.objects.create( XXXXX )
    
    pepe = Perfil()
    pepe.usuari = pepe_usr
    
    
    
    fantasia = Genere()
    fantasia.nom = "Fantasia"
    fantasia.save()

    terror = Genere()
    terror.nom = "terror"
    terror.save()

    romantico = Genere()
    romantico.nom = "romantico"
    romantico.save()

    harrypotter = Titol()
    harrypotter.titol = "Harry Potter i la pedra filosofal"
    harrypotter.sinopsis = "Primer de Harry Potter"
    harrypotter.genere = fantasia
    harrypotter.save()

    harry1 = LLibre()
    harry1.idioma = "Català"
    harry1.isbn = "0000000000001"
    harry1.edicio = "Primera"
    harry1.editorial = "La Castellana"
    harry1.titol = harrypotter
    harry1.propietari = pepe
    harry1.save()
    
    
    