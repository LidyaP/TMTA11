'''
Encapsulare - este posibilitatea de a restrictiona accesul la anumite atribute si metode dintr-o clasa astfel incat sa protejam datele
sa aratam utilizatorului doar informatiile de care are nevoie. Motivul pentry care vrem sa facem asta este fie din motive de securitate fie
pentru a controla modificarea de catre utilizator
Exista trei tipuri :
a) public (fara restrictii) atributul sau metoda sunt accesibile oriunde in program
b) private - atributele si metodele sunt accesibile doar in interiorul claseri in care au fost definite. Vor fi precedate de caracterul "__"
c) protected - atributele sau metodele sunt vizibile oriunde dar nu sunt returnate ca sugestii. Vor fi precedate de caracterul "_"
'''

#ex. a)PUBLIC

class ExempluPublic:
    def __init__(self):
        self.public_var = 10

obiect = ExempluPublic()
print(obiect.public_var)

#ex. b)Privat

# class ExempluPrivat:
#     def __init__(self):
#         self.__privat_var = 30
#
# obiect1 = ExempluPrivat
# print(obiect1.__privat_var)         # acesta va genera o eroare

#ex. c) Protected

class ExempluProtejat:
    def __init__(self):
        self._protejat_var = 20

obiect2 = ExempluProtejat()
print(obiect2._protejat_var)

# Atunci cand avem dea face cu atribute private (mai ales) sau protected de regula se definesc ceea ce se numeste :
# getter - metoda pentru extragere valorii din atribut
# setter - metoda pentru actualizare valorii in atribut
# deleter - metoda pentru stergere valorii din atribut

class Cinema:
    def __init__(self, nume, adresa, capacitate):
        self.nume = nume
        self.adresa = adresa
        self.capacitate = capacitate
        self.filme = []
        self._bilete_vandute = 0    # am definit atributul ca fiind protected folosind caracterul "_"
        self.__total_incasari = 5000  # am definit atributul ca fiind privat
        self.faliment = False

    def add_film(self, film):
        self.filme.append(film)

    def remove_film(self, film):
        self.filme.remove(film)

    def rulare_film(self):
        print("Filmele ruleaza la", self.nume, "cinema:")
        for film in self.filme:
            print("-", film)

    def vinde_bilete(self,numar_bileta_vandute):
        self._bilete_vandute += numar_bileta_vandute

    @property
    def total_incasari(self):
        pass

    @total_incasari.getter
    def total_incasari(self):
        return self.__total_incasari

    @total_incasari.setter
    def total_incasari(self,valoare_modificare_total):
        self.__total_incasari += valoare_modificare_total

    @total_incasari.deleter
    def total_incasari(self):
        self.__total_incasari = 0

cinema_afi = Cinema('Hollyood', 'ParkLake', 150)
print(f"Filmele care ruleaza la cinema afi sunt : {cinema_afi.filme}")
print(f"La cinema afi s-au vandut : {cinema_afi._bilete_vandute}")
# print(cinema_afi.__total_incasari)
cinema_afi.floricele = 50           # creem un atribut nou specific doar opbiectului cinema_afi, acesta nu poate fi folosit de alte obiecte
print(cinema_afi.floricele)
cinema_plaza = Cinema('Bolyyood', "Plaza Romania", 250)
# print(cinema_plaza.floricele)
#Apelare getter :
print(f'Incasarile accesate prin getter : {cinema_afi.total_incasari}') #atentie! nu se mai pun cele doua paranteze rotunde

# Apelare setter :
cinema_afi.total_incasari = 60              #atentie! nu se mai pun cele doua paranteze rotunde
print(f'Incasarile accesate prin setter : {cinema_afi.total_incasari}')  #atentie! nu se mai pun cele doua paranteze rotunde

#apelare deleter
del cinema_afi.total_incasari
print(f'Incasarile accesate prin deleter : {cinema_afi.total_incasari}') #atentie! nu se mai pun cele doua paranteze rotunde
