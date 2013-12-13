# -*- coding: utf8 -*-
from llibres.models import Genere
from llibres.models import Titol
from llibres.models import Llibre
from django.contrib.auth.models import User
from usuaris.models import Perfil

def crea():
    pepe_usr = User.objects.create_user( 'pepe', 'pepe@bookshare.cat', 'pepe1' )
    jose_usr = User.objects.create_user( 'jose', 'jose@bookshare.cat', 'jose1' )
    pepa_usr = User.objects.create_user( 'pepa', 'pepa@bookshare.cat', 'pepa1' )
    
    pepe_usr.save()
    jose_usr.save()
    pepa_usr.save()
    
    pepe = Perfil()
    pepe.usuari = pepe_usr
    pepe.save()
    
    jose = Perfil()
    jose.usuari = jose_usr
    jose.save()
    
    pepa = Perfil()
    pepa.usuari = pepa_usr
    pepa.save()
    
    fantasia = Genere()
    fantasia.nom = "Fantasia"
    fantasia.save()

    terror = Genere()
    terror.nom = "Terror"
    terror.save()

    romantico = Genere()
    romantico.nom = "Romantico"
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
    
    amor = Titol("Amor Amor", "Llibre d'amor", romantico)
    amor.save()
    
    amor1 = Llibre("Català","0000000000002","Segona","La Catalana", amor, pepa)
    amor1.save()
    
    grito = Titol("Grito","Terror el grito",terror)
    grito.save()
    
    grito1 = Llibre("Català","0000000000003","Tercera","Maya", grito, jose)
    
    
    