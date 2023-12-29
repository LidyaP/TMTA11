'''
POLIMORFISMUL : este posibilitatea crearii a doua functii cu nume identic dar cu un comportament diferit. Polimorfism inseamna "a avea mai multe forme" si apare in momentul in care folosim mostenirea
.Polimorfismul e ofera posibilitatea sa folosim metodelele mostenite sub mai multe forme, in functie de rezultatul pe care il dorim
In python implementarea se realizeaza prin doua mecanisme principale: suprascriere si folosirea functiei len() si a operatorilor
a) suprascriere - doua sau mai multe clase pot avea metode cu acelasi nume, dar comportamentul acestor metode poate varia in functie de tipul obiectelor care le apeleaza
'''

#ex.

class Caine:
    def sunet(self):
        return "Ham,Ham"

class Pisica:
    def sunet(self):
        return "Miau,Miau"

def afiseaza_sunet(animal):         # functia primeste un parametru numit animal, animal este un obiect de orice tip. Apoi functia apeleaza metoda sunet
    print(animal.sunet())

rex = Caine()
tom = Pisica()

afiseaza_sunet(rex)
afiseaza_sunet(tom)

#Ex. polimorfism cu functe len()

lista = [1,2,3,4,5]
sir_de_caractere = "Python"

lungime_lista = len(lista)
print(lungime_lista)
lungime_sir = len(sir_de_caractere)
print(lungime_sir)

#ex. polimorfism cu operatorul +
rezultat1 = 5+7
rezultat2 = "hello" + " " +"World"

print(rezultat1)
print(rezultat2)

#ex. supraincarcare cu ajutorul unui numar variabil de argumente
# Python nu suporta overloading (supraincarcare) i sensul traditional al limbajelor de programare cum ar fi Java sau C++ dar putem avea o forma de supraincarcare prin
# intermediul valorilor implicite a argumentelor sau a unui numar variabil de argumente
def calculator(*args):
    if len(args) == 1:
        return args[0] * 2
    elif len(args) ==2:
        return args[0] + args[1]
    else:
        return sum(args)

print(calculator(3))
print(calculator(2,5))
print(calculator(1,2,3,4))

# In functia de mai sus functia calculator accepta un numar variavil de argumente si isi ajusteaza comortamentulo in functie de numarul acestora