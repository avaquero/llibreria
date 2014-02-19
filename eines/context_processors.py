#Context processor que comprova si hi ha solicitut de prestecs perdents de llibres que te l'usuari 
def alerta_peticions(request):
    alerta_peticions_flag = ( not request.user.is_anonymous() and 
                              hasattr(request.user, 'perfil')  and
                              request.user.perfil.llibre_set.filter(titol__solicitut_prestec__estat = 'pendent').exists()
                             )
    return {'alerta_peticions_flag':alerta_peticions_flag,
            }
    
