'''
POO/OOP - PROGRAMAREA ORIENTATA PE OBIECTE (OBJECT ORIENTED PROGRAMING)
POO este o modalitate prin care putem sa structuram propietatile si comportamentul unei entitati din viata reala intr-o structura
logica ce functioneaza ca un template. Acest template va servi drept model pentru crearea unei entitati care sa reprezinte un exemplu
din viata reala.
poo se bazeaza pe clase si obiecte.
o clasa este un sablon sau un model (ca o reteta) pentru a crea obiecte. Ea defineste atributele si modelele care vor fi prezente
in obiectele create din acea clasa
Obiectele sunt instante ale claselor, acestea contin date specifice (atribute) si pot apela metodele definite in clasa lor
Atributele sunt variabile definite intr-o clasa. Atributele unei clase descriu cum ar trebui sa arate entitatea (ce propietati sa aiba)
Metodele sunt functii definite intr-o clasa. Metodele unei clase descriu ce ar trebui sa faca entitatea (cum sa se comporte)
Diferenta intre functii si metode este aceea ca sunt independente, in timp ce metodele sunt create in interiorul unei clase
'''

#ex. 1

# class Masina:
#     def __init__(self,marca,model):
#         self.marca = marca
#         self.model = model
#
#     def afiseaza_informatii(self):
#         print(f'Masina : {self.marca} {self.model}')
#
# #ex. de obiect al clasei Masina
#
# masina_mea = Masina(marca = "Dacia", model = "Duster")
# print(masina_mea.marca, masina_mea.model)
# masina_mea.afiseaza_informatii()


#ex.2

class Caine:                                # definit clasa Caine
    def __init__(self,nume, varsta):        # am definit metoda speciala __init__ care actioneaza ca un constructor
        self.nume = nume                    # atributele nume si varsta ale obiectului sunt initializate cu valorile
                                            # primite la crearea obiectului
        self.varsta = varsta

    def latra(self):                        # am definit metoda latra care afiseaza un mesaj simplu in consola
        print("ham, ham")

rex = Caine(nume = "REX", varsta = 3)       # am creat un obiect "rex" si am transmis valorile atributelor nume si varsta
print(rex.nume)                             # se acceseaza si se afiseaza valorile atributului nume
print(rex.varsta)
rex.latra()                                 # am apelat metoda latra a obiectului rex. va afisa "ham ,ham" in consola

'''
Exista doua tipuri de constructori :
1. constructor implicit - care este incorporat in limbajul python si el este apelat automat atunci cand nu exista 
un constructor explicit
2. constructir explicit - este definit de catre un utilizator cu scopul de a controla felul in care acel obiect este instantiat
'''
#EX. de constructor implicit

class Masina:
    def __init__(self):
        self.moldel = "Nissan"
        self.an_fabricatie = 2020

    def afisare_informatii(self):
        print(f'Model : {self.moldel}, an fabricatie : {self.an_fabricatie}')

masina1 = Masina()
masina1.afisare_informatii()

#ex. constructor explicit

class Masina:
    def __init__(self, model = "Dacia", an_fabricatie = 2020):
        self.model = model
        self.an_fabricatie = an_fabricatie

    def afisare_informatii(self):
        print(f'Model : {self.model}, an fabricatie : {self.an_fabricatie}')

masina2=Masina(model='Tesla', an_fabricatie=2022)
masina2.afisare_informatii()

#ex. cu constructor explicit
class Scoala():
    #atribute pe care le poate avea scoala
    adresa =None                        #am pus none pentru ca fiecare obiect al clasei sa poata avea propria adresa
    ciclu_invatamant = "primar"
    capacitate_elevi = None
    numar_profesori = None
    profil = "Real"
    clase = {}                          # este un dictionar care va contine informatii despre clasele scolii

    #definim un constructor explicit
    def __init__(self, adresa, ciclu_invatamant, profil):
        self.adresa = adresa
        self.ciclu_invatamant = ciclu_invatamant
        while profil.lower() not in ("real","uman"):
            profil = input("profil invalid. Va rugam sa introduceti una din optiunile 'Real' sau 'Uman' ")

    #Activitati care se pot face intr-o scoala
    def adauga_clasa(self,nume_clasa,profil,ciclu,numar_elevi,numar_profesori):
        self.clase[nume_clasa] = {"profil":profil,
                                  "ciclu":ciclu,
                                  "numar_elevi":numar_elevi,
                                  "numar_profesori":numar_profesori}

    #definim o metoda pentru actualizarea adreselor
    def actualizare_adresa_scoala(self,adresa_noua):
        self.adresa = adresa_noua
        print(self.adresa)
        return self.adresa              # returneaza noua adresa astfel incat sa poapa fi utilizata sau afisata in alta parte a codului

    #definim o metoda care sa extraga numarul profesori
    def extrage_numar_de_profesori(self):
        return self.numar_profesori     #returneaza valoarea atributului numar_profesori al obiectului curent

# scoala1 = Scoala() #atuncti cand instantiem un obiect dintr-o clasa cu constructor explicit suntem obligati sa dam
# valori pentru parametri definiti in contructorul explicit. Aceasta instantiere o sa genereze eroare : TypeError: Scoala.__init__()
# missing 3 required positional arguments: 'adresa', 'ciclu_invatamant', and 'profil' pentru ca incercam sa instantiem un
# obiect fara sa ii dam valori petru parametri din constructor

scoala1 = Scoala("Strada Miahi Voda nr 23","primar","Uman")
print(f"Adresa scoli este : {scoala1.adresa}")
print(f"Ciclu invatamant este : {scoala1.ciclu_invatamant}")
print(f"Profilul este : {scoala1.profil}")

# scoala2 = Scoala("Strada Miahi Voda nr 23","primar","Teoretic")
# print(f"Profilul este : {scoala2.profil}")

scoala1.actualizare_adresa_scoala("Strada Mircea cel Batran nr 30")
print(scoala1)  # printeaza adresa de memorie care reprezinta obiectul
print(f"Noua adresa este : {scoala1.adresa}")

scoala1.numar_profesori = 45
print(scoala1.extrage_numar_de_profesori())

#sa printam atributele definite la nivel de obiecte
print(f"Atributele definite la nivel de clasa sunt :{scoala1.adresa} {scoala1.profil} {scoala1.numar_profesori}"
      f" {scoala1.ciclu_invatamant} {scoala1.clase}")
#sa printam atributele definite la nivel de clasa
print(f"Atributele definite la nivel de obiect sunt : {Scoala.adresa} {Scoala.profil} {Scoala.clase} "
      f" {Scoala.numar_profesori} {Scoala.ciclu_invatamant} {Scoala.capacitate_elevi}")
# Atentie!! ordinea argumentelor date la instantiere trebuie sa coincida cu ordinea parametrilor definiti in constructor
scoala3 =Scoala("Strada Margelelor nr 60","Gimnazial", "Real")
print(f"Atributele definite la nivel de obiect 'scoala3' sunt : {scoala3.adresa} {scoala3.ciclu_invatamant} {scoala3.profil}")

# In POO estisa patru princiipi principale :
#1.Mostenirea (Inheritance)
#2.Abstractizare (Abstracting)
#3.Polimorfism (Polymorhism)
#4.Incapsularea (Encapsulation)
