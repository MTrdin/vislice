import model

def izpis_poraza(igra):
    return 'Porabili ste preveč poskusov. Pravilno geslo je {}.'.format(igra.geslo)

def izpis_zmage(igra):
    return 'Uspešno ste uganili geslo {}!'.format(igra.geslo)

def izpis_igre(igra):
    tekst = (
        '=================================\n\n'
        '    {trenutno_stanje}\n\n'
        'Neuspesni poskusi: {poskusi} \n\n'
        '=================================\n\n'
    ).format(trenutno_stanje= igra.pravilni_del_gesla(),poskusi=igra.nepravilni_ugibi())
    return tekst

def zahtevaj_vnos():
    vnos = input('Poskusi uganit crko.')
    return vnos

def preveri_vnos(vnos):
    '''Funkcija vrne true ce'''
    if len(vnos) != 1:
        print('Neveljaven vnos. Vnesi eno crko.')
        return False
    else:
        return True

#izvajanje vmesnika
    
    

def zazeni_vmesnik():
    igra = model.nova_igra()

    while True:
        #izpišimo stanje
        print(izpis_igre(igra))
        #igralec
        poskus= zahtevaj_vnos()
        if not preveri_vnos(poskus):
            continue # preskoči preostanek zanke
        igra.ugibaj(poskus)
        rezultat = igra.ugibaj(poskus)

        #preverimo ce je igre konec
        if igra.poraz(): #if rezultat== model.PORAZ
            print(izpis_poraza(igra))
            return
        elif igra.zmaga():
            print(izpis_zmage(igra))
            return
    return

zazeni_vmesnik()
