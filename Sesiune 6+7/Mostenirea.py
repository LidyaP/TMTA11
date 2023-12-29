#MOSTENIREA - este un concept in POO care permite unei clase copil (numita clasa derivata sau subclasa) sa preia atribute si metode
#de la una sau mai multe clase parinte ( numita si clasa de baza sau superclasa).
#Clasa copil preia atributele di metodele clasei parinte si poate adauga sau modifica comportamentul acesteia
#Avantajul mostenitii este ca nu mai este nevoie sa scriem acelasi cod de mai multe ori
#O clasa copil poate sa mosteneasca un numar nelimitat de clase parinte.

#ex. de definire clasa parinte si copil

class Animal:
    def __init__(self, nume): # aceasta este clasa de baza (parinte) in ierarhia de mostenire
        self.nume = nume

    def sunet(self):           #metoda cu implementare implicita
        return "Sunet necunoscut"

class Caine(Animal):            # clasa copil care mosteneste clasa parinte "Animal"
    def sunet(self):            # aceasta metoda va suprascrie metoda din clasa parinte
        return "Ham, Ham"

class Pisica(Animal):
    def sunet(self):
        return "Miau, Miau"

rex = Caine(nume = "Rex")
tom = Pisica(nume= "TOM")

print(rex.nume)
print(tom.nume)
print(rex.sunet())
print(tom.sunet())

#Ex. mostenire multipla

class AnimalTerestru:
    def deplasare(self):
        return "Se deplaseaza pe uscat"

class AnimalAerian:
    def deplasare(self):
        return "Se deplaseaza in aer"

class Pasare(AnimalAerian, AnimalTerestru):
    pass

papagal = Pasare()
print(papagal.deplasare())


