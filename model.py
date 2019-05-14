import random

#definiramo konstante
STEVILO_DOVOLJENIH_NAPAK = 10

PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = '-'
NAPACNA_CRKA = 'o'

ZMAGA = 'W'
PORAZ = 'X'


#if crka== model.PRAVILNA_CRKA:
    
#DEFINIRAMO LOGICNI MODEL IGRE

class Igra:

    def __init__(self, geslo, crke):
        self.geslo = geslo.upper()
        self.crke = crke
        return

    def napacne_crke(self):
        seznam_napacnih_crk = []
        for x in self.crke:
            if x not in self.geslo:
                seznam_napacnih_crk.append(x)
        return seznam_napacnih_crk
        
    def pravilne_crke(self):
        seznam_pravilnih_crk = []
        for x in self.crke:
            if x in self.geslo:
                seznam_pravilnih_crk.append(x)
        return seznam_pravilnih_crk
        
    def stevilo_napak(self):
        return len(self.napacne_crke())
    
    def zmaga(self):
        for x in self.geslo:
            if x in self.crke:
                return False
        return self.stevilo_napak() < STEVILO_DOVOLJENIH_NAPAK

    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK

    def pravilni_del_gesla(self):
        niz = ''
        for crka in self.geslo:
            if crka in self.crke:
                niz += ' ' + crka
            else:
                niz += ' _'
        niz = niz.strip() #pocistimo presledke
        return niz

    def nepravilni_ugibi(self):
        niz = ''
        for crka in self.napacne_crke():
           niz += crka + ' '
        #' '.join(self.napacne_crke())


    def ugibaj(self, crka):
        crka = crka.upper()
        if crka in self.crke:
            return PONOVLJENA_CRKA
        elif crka in self.geslo:
            self.crke.append(crka)
            if self.zmaga():
                return ZMAGA
            else:
                return PRAVILNA_CRKA
        else:
            self.crke.append(crka)
            if self.poraz():
                return PORAZ
            else:
                return NAPACNA_CRKA


#izluscimo vse slovenske besede
bazen_besed = []

with open("besede.txt",'r',encoding='utf-8') as datoteka:
    for vrstica in datoteka.readlines():
        beseda = vrstica.strip()
        bazen_besed.append(beseda)

# funkcija za generiranje iger

def nova_igra():
    geslo = random.choice(bazen_besed)
    return Igra(geslo, [])










    