# # - cu '#' punem comentarii pe o singura linie
# """
# - intre aceste ghilimele se pot pune comentarii pe mai
# multe linii iar editorul de cod le va ignora.
# variabila = 10 # am declarat o variabila
# """
# # linia aceasta vreau sa fie comentata
# # - cu combinatia tastelor ctrl+? putem comenta o linie selectata
# #VARIABLA - sunt aderese de memorie care stocheaza diverse valori
# #valori care pot modifica pe percursul executiei codului
# # numar_intreg = 15
# # print(numar_intreg)
# #CamelCase - consta in a incepe un cuvant cu o litera mare, fara
# #sa folosim spatii sau caractere cu subliniere intre cuvinte
# # NumeVariabila = 15
# #SnakeCase - consta in folosirea de litere mici si adaugarea de
# #caractere de subliniere intre cuvinte
# # nume_variabila = 15
# # myvar = 15
# # myVar = 15
# numar_intreg = 15 #(int)
# numar_cu_virgula = 3.14 #(floot)
# text = "Salut, buna seara!" #(string)
# lista = [1,2,3,4] #(lista)
#
# # TIPURI DE DATE - propietati ale adreselor de memorie care definesc
# # ce fel de informatii pot fi stocate la acea adresa de memorie.
# # Tipul de date poate varia in functia de valoarea salvata la acea
# # adresa de memorie si se poate schimba pe parcaursul executiei codului
# # Tipuri de date cele mai cunoscute :
# # Numeric :
#     # int (integer)
#     # myvar = 42
#     # floot (numere cu virgula)
#     # myvar = 3.14
# # Sir de caractere :
#     # str (string)
#     # myvar = "Buna ziua!"
# # Valori logice :
#     #bool (boolean) = True or False
#     # myvar = True
# #Structuri de date secventiale :
#     #list (lista) = [1,2,3]
#     #tupla =(1,2,3)
# #Structuri de date mapping :
#     #dict (dictionar) = {cheie : valoare}
# #Structuri de date set :
#     #set (seturi) = {1,2,3}
#
# # ani = 5 #am initializat o variabila cu valoare 5 reprezentata de
# #         #tipul de date int
# # ani1 = "cinci" # am initializat o variabila cu valoare "cinci"
# #         #de tipul de date str
#
# #PRINT - o functie care ne ajuta sa afisam informatii in consola
# # print(text)
# # print(lista)
# #Printare cu formatare este modalitatea prin care putem integra
# #o variabila in interiorul unui string.
# # pentru tipurile de date de tip string '+' este folosit petru a
# #concatena doua siruri de caractere
# #pentru tipurile de date de tip int semnul '+' va face adunare
# # print("Ana are " + 12 + "ani") - aici am incercat sa concatenam
#                                 #date de tip str cu int si am primit
#                                 #eroare
# # print("Ana are " + str(12) + " ani") - aici am folosit type casting
#     # adica am fortat cifra 12 sa fie de tip string, nu am primit eroare
#     #dar cod-ul este incarcat si greu de citit
# # print(f"Ana are {12} ani")
# varsta = 12
# print(f"Ana are {varsta} ani")# aici am concatentat cu variabila
#                             # definita mai sus
# #CONSTANTELE - este o adresa de memorie care stocheaza o valoare.
# # de obicei constantele sunt denumite cu litere majuscule si cu
# # subliniere intre cuvinte
# PI = 3.14159
# MAX = 100
# print(PI)
# varsta = 15 # am modificat valoarea variabilei definite mai sus
# print(f"Ana are {varsta} ani")#am printat variabila cu noua valoare
# FUNCTIA TYPE ()
# Functia este o logica de cod predefinita ce are rolul de a face ceva
# Functia Type este o funtie care returneaza tipul de date a unei
# variabile si nu numai
# x = 5
# print(type(x))
# y = "Hello"
# print(type(y))
# z = [1,3,9]
# print(type(z))
# TYPE CASTING - transforma o valoare dintr-un tip de date in altul
# type castingul este adesea necesar cad se lucreaza cu diferite
# tipuri de date sau atunci cand se doreste sa ne asiguram ca o valoare
# este de un anumit tip de date.
# Castingul trebuie sa fie compatibil. Nu se poate face conversie
# din str in int pentru ca va returna eroare\
# Mai jos incercam sa facem type casting dintr-o valoare de tip
# str in tip int
# nume = 'cinci'
# int_nume = int(nume)
# print(int_nume)
# mai jos incercam sa facem type casting dintr-o valoare boolean
# in int. va fi transformt True in 1 si False in 0
# x = True
# y = int(x)
# print(f"am fortat variabila sa fie in {y}")
# d = 4.58978
# f = int(d)
# print(f"valoarea fara zecimale este {f}")
#
# nume1 = "Ioana"
# an = 1990
# salariu = 9999.99
# angajat = True
#
# print(f'Ma numesc {nume1} sunt nascuta in anul {an} sunt '
#       f'angajata {angajat} si am salriul {salariu}')
#
# numele_meu = "Cristina"
# print("Numele meu este:", numele_meu)
#
# nume10 = "Ana"
# ani = 25
# print("Nume", nume10, "Varsta", ani)

# Fuctia INPUT
# Functia input este folosita pentru a citit o linie de intrare de la un utilizator /tastatura si functia returneaza o valoare
# cititia sub forma de sir de caractere . O folosim pentru a interactiona cu utilizatori pentru a obtine date de intrare in
# timp timpul executari codului.
#
# nume_utilizator = input("Va rougam introduceti numele dvs : ")
# print(f"Salut {nume_utilizator}")

# prenume = input("Va rugam sa va introduceti prenumele dvs : \n")
# nume = input("Va rugam sa va introduceti numele dvs: \n")
# print(f"Buna numele tau complet este : {prenume} {nume}!")

# print(10/0)

# try:
# 	print(10/0)
# except:
# 	print("impartirea la 0 nu este permisa")
# try:
#     # Codul care poate genera o excepție
#     rezultat = 10 / 0  # Exemplu: împărțire la zero
# except ZeroDivisionError:
#     # Blocul care se execută dacă apare excepția specificată
#     print("Eroare: Împărțire la zero!")

def verifica_numar_pozitiv(numar):
    if numar < 0:
        raise ValueError("Numărul nu poate fi negativ.")

try:
    verifica_numar_pozitiv(5)
except ValueError as e:
    print(f"Eroare: {e}")


