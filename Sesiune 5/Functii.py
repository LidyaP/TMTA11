# import math
#
# #FUNCTII
# #Functiile sunt blocuri de cod reutilizabile care efectueaza o anumita actiune. Ele sunt definite cu scopul de a limita
# # numarul de linii de cod pe care le scriem si a face programul sa fie mai modular si respectiv mai usor de citit
# #componentele unei functii :
# # inceputul functiei definit prin cuvantul "def"
# #numele functiei care nu trebuie sa fie un cuvant rezervat si se foloseste formatul snake_case
# #() care pot stoca parametri
# #separatorul intre lista de parametri si corpul fuctiei este ":"
# #corpul functiei - setul de instructiuni care se vor executa la apelarea functiei
# #(optional) instructiunea de return
#
# #ex.
# def salutare():
#     print("Salut!")
#
# salutare()#Apelul functiei
#
# #Ca sa folosim instructiunile salvate intr-o functie trebuie sa facem ceea ce se numeste apelarea functiei. Instructiunile
# # dintr-o functie se vor executa DOAR DACA APELAM FUNCTIA.
# # Apelarea se face prin scrierea numelui functiei urmat de doua paranteze rotunde in interiorul carora vom pune (daca este cazul)
# #unul sau mai multe argumentae.
#
# '''
# EXISTA PATRU TIPURI DE FUNCTII IN PYTHON
# 1. Functii simple
# 2. Functii cu parametri
# 3. Functii cu return
# 4. Functii cu parametri si return
#
# PARAMETRII: un parametru este o adresa de memorie temporara care se populeaza atunci cand functia este apelata. Parametri sunt
# reprezentati de un nume care este specificat intre parantezele rotunde la definirea functiei si care au rolul de a stoca informatii
# venite din exterior, aceste informatii vor fii utilizate in momentul executarii instructiunilor
#
# Parametrii sunt de doua feluri :
# parametri expliciti - sunt acei parametri specificati in mod direct in definitia functiei
# parametri impliciti - in cazul in care nu vor primi valoare la apelarea functiei se vor folosi impicit valoarea specifica la
# definirea functiei
# '''
# #ex. de parametri expliciti
# def salutare_cineva(nume):  #nume este parametru explicit
#     print(f"Salut, {nume}!")
#
# salutare_cineva("John") # La apelare, numele valorilor efective care sunt transmise functiilor se numesc argumente. "John" este un argument
#
# #ex. cu parametri impliciti
#
# def salutare_cineva(nume="Ioana"): # aceast functie are un singur parametru explicit, care are o valoare implicita setata ca "Ioana"
#     print(f'Salut, {nume}')
#
# salutare_cineva() # la apelarea acestei functii nu am furnizat argument
# salutare_cineva("Cristi") # la aceasta apelare am furnizat si argument, iar in acest caz valoarea implicita (Ioana) setata la definirea functie
#                             # va fi ignorata deoarece am furnizat un argument explicit
# '''
# RETURN
# este modalitatea prin care putem sa transmitem rezultatul functiei in exterior (adica sa o vizualizam)
# Spre exemplu daca vrem sa calculam suma a doua numere si sa o printam pe ecran in momentul apelarii functiei, va trebui sa avem
# instructiune de return, altfel adunarea se va executa dar noi nu vom putea valida acest lucru deoarece nu va fi afisat nicaieiri
# '''
# #Ex. Functii cu parametri si return
#
# def adunare(a,b):
#     rezultat = a+b # se realizeaza adunarea parametrilor a si b , iar rezultatul este stocat in variabila rezultat
#     return rezultat # aceasta este valoarea pe care o va primi orice cod care apeleaza aceasta functie
#
# suma = adunare(3,5) # se apeleaza functia adunare cu argumenetel a=3 si b=5.
#                         # Rezultatul returnat in functie (care este suma lui a si b) este asignat variabilei suma
# print(f"Suma este: {suma}") # printam valoarea variabilei suma
#
# # Functii cu numar indefinit de parametri
# # In Python poti defini functii care sa accepte un numar variabil de parametri folosindune de  functia Pyrthon "*args" si "**kwargs"
#
# # ex. Functii cu *args
#
# def functie_variabila(*args): # functia a fost definita cu un singur parametru *args, aratand ca functia accepta un numar variabil de argumente
#     rezultat = 0            # se initializeaza variabila rezultat la 0, care va fi utilizat pt a stoca suma argumentelor
#     for numar in args:      # bucla "for" itereaza prin toate argumentele furnizate si adauga fiecare la variabila "rezultat"
#         rezultat+= numar
#     return rezultat         # aceasta este valoarea pe care o va primi orice cod care apeleaza aceasta functie
# rezultat1 = functie_variabila(1,2,3) # se apeleaza functia cu 3 argumente iar rezultatele vor fi stocate in aceasta
#                                             # variabila (rezultat1)
# rezultat2 = functie_variabila(4,5,6,7,8,9,10) # se apeleaza functia inca o data dar i se dau mai multe argumente iar
#                                                     # rezultatele vor fi stocate in aceasta variabila (rezultat2)
#
# print(f"Rezultat 1 : {rezultat1}") # la rularea acestui cod se vor afisa rezultate sumelor pt cele 3 argumente
# print(f"Rezultat 2 : {rezultat2}")
#
# #functii cu **kwargs
#
# def informatii_student(**kwargs): # folosim parametrul **kwargs aratand ca functia accepta un numar variabil de argumente keyword
#     for cheie, valoare in kwargs.items(): # utilizam bucla "for" pentru a itera prin perechile cheie - valoare din kwargs
#         print(f"{cheie} {valoare}")        # fiecare pereche cheie-valoare va fi afisata in conosila folosindune de functia print
#
# informatii_student(nume ="John", varsta =20) # se apeleaza functia furnizand argumente de tip cheie-valoare (nume = John)
# informatii_student(nume = "Alice", varsta = 25, nota = 10, cursul = "Biologie")
#
# #ex. Sa calculam aria unui cerc
#
# def aria_cerc(raza):
#     return math.pi * raza **2
#
# rez = aria_cerc(3)
# print(rez)
#
# # TRATAREA EXCEPTIILOR:
# '''
# este o tehnica de gestionare a situatiilor exceptionare care pot aparea in timpul executiei unei bucati de cod sau a codului intreg
# . Exceptiile sunt evenimente neasteptate care pot provoca intreruperea rulai codului. Sunt utile atunci cand nu ne dorim oprirea codului
# Structura tratarii exceptiilor :
# try - inceputul blocului de exceptie
# caracterul ":" care marcheza inceputul blocului de cod care se incearca a se executa
# except - inceputul blocului de tratare exceptii
# caracterul ":" marcheaza inceputul blocului de cod de tratare a exceptiilor
# blocul de cod care se executa atunci cand se produce o exceptie
# '''
#
# # Ex. 1
# # print(10/0)
# try:
#     print(10/0)
# except:
#     print("impartirea la 0 nu este permisa")
#
# try:
#     rezultat = 10/0  # incerc sa impart 10 la 0
# except ZeroDivisionError: # ZeroDivisionError este denumirea erori care apare in caz ca vrem sa impartim 10/0
#     print("eroare : Impartirea la 0 nu este permisa") # Blocul care se executa daca apare exceptia specifica
#
# def impartire(a,b):
#     try:
#         rezultat3 = a/b
#         print(f"rezultatul impartirii este : {rezultat3}")
#     except ZeroDivisionError:
#         print("Nu se poate efectua impartirea")
#
# impartire(10,0)
#
# # Exceptii - poti ridica o exceptie manual folosind instructiunea "raise" (ridicarea unei exceptii). Ridicarea manuala a
# # unei exceptii este utila atunci cand vrei sa semnalezi ceva anormal in program si sa fortezi o executie alternativa
#
# # Ex.1
# nota_elev = int(input("va rugam sa intorduceti nota care trebuie sa fie procesata"))
# if nota_elev<5: # verifica conditia daca nota elevului este mai mica de 5
#     raise Exception("Nota cursantului este prea mica") # daca conditia de mai sus este adevarata (adica nota mai mica ca 5) atunci este
#                                                         # executata instructiunea de raise
# Prin folosirea raise programul semnaleaza explicit ca se afla intr-o situatie exceptionala, unde nota studentului
# este considerata prea mica. Functia raise este utilizata in general doar de programatori.from
#
# DEBUGGING  - reprezinta procesul de analiza a codului prin care putem sa observam cum circula datele prin intermediul caruia
# putem sa identificam potentialele probleme. Pentru a face debugging trebuie sa punem un break point in locul unde vrem sa vedem
# cum circula datele. Se pot pune multiple break-pointuri. Un break point este un loc unde codul se opreste inainte sa execute urmatoarea
# instructiune.
# Ca sa punem un break point dam click pe marginea din stanga a fisierului intre cifre si marginea fisierului
# Dupa ce am pus break point-ul de care avem nevoie dam click dreapta si "Debug"
#
# Ex.
lista_masini = ["Audi","Skoda", "Ferrai", "Trabant", "Dacia", "Mustang", "Mercedes", "Tesla"]
i = 0
while i <len(lista_masini):
    if lista_masini[i] == "Mercedes":
        print(f"Am gasit masina dvs")
        break
    i+=1