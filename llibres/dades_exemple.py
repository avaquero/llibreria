# -*- coding: utf8 -*-
from llibres.models import Genere
from llibres.models import Titol
from llibres.models import Llibre
from django.contrib.auth.models import User
from usuaris.models import Perfil

def crea():
    #--------------------USUARIS---------------------------------
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
    #------------------------GENERES------------------------------------
    fantasia = Genere()
    fantasia.nom = "Fantasia"
    fantasia.save()
    
    aventura = Genere()
    aventura.nom = "Aventura"
    aventura.save()

    terror = Genere()
    terror.nom = "Terror"
    terror.save()

    romantico = Genere()
    romantico.nom = "Romantico"
    romantico.save()
    
    historica = Genere()
    historica.nom = "Historica"
    historica.save()
    
    manuals = Genere()
    manuals.nom = "Manuals"
    manuals.save()
    #---------------------Titols---------------------------
    harrypotter = Titol()
    harrypotter.titol = "Harry Potter i la pedra filosofal"
    harrypotter.sinopsis = "Primer de Harry Potter"
    harrypotter.genere = fantasia
    harrypotter.save()

    amor = Titol(titol = "Amor Amor", sinopsis = "Llibre d'amor", genere = romantico)
    amor.save()

    grito = Titol(titol ="Grito",sinopsis ="Terror el grito",genere =terror)
    grito.save()
    
    #-----------------------------Llibres-----------------
    harry1 = Llibre()
    harry1.idioma = "Català"
    harry1.isbn = "0000000000001"
    harry1.edicio = "Primera"
    harry1.editorial = "La Castellana"
    harry1.titol = harrypotter
    harry1.propietari = pepe
    harry1.save()
    
    amor1 = Llibre(idioma = "Català",isbn = "0000000000002",edicio = "Segona",editorial = "La Catalana", titol = amor, propietari = pepa)
    amor1.save()
    
    grito1 = Llibre(idioma = "Català", isbn = "0000000000003", edicio = "Tercera", editorial = "Maya", titol = grito, propietari = jose)
    grito1.save()
    
    