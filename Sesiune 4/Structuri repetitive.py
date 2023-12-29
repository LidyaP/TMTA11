# STRUCTURI REPETITIVE
#structurile repetitive sunt : while, folr, for each (cele mai utilizate sunt While si For)
# Structurile repetitive sunt utilizate pentru a executa aceasi secventa de instructiuni de mai multe ori pana cand o anumita conditie nu
# mai este indeplinita

#1 WHILE.
# este o structura repetitiva care executa un set de instructiuni atata timp cat o conditie este adevarata. Se foloseste atunci cand nu
# stim exact momentul in care conditia nu mai este adevarata
# Comonentele unui while:
#a) o variabila de control al while-lui ( nu este obilgatoriu)
#b) inceputul while-lui marcat prin cuvantul WHILE
#c) conditia de evaluare (cea pe baza caruia se decide daca se mai trece o data prin while sau nu)
#d) separatorul intre conditia de evaluare si corpul while_lui  ":"
#e) corpul while-lui (adica o serie de instructiuni care se vor repeta)

# #Ex.1
# suma = 0
# i = 1 # aceasta este variabila de iteratie
#
# while i>=1 and i<=10:
#     suma = suma+i
#     print(f"Am adunat numarul {i}")
#     i+=1
#
# #EX.2
#
# numar = 1
# while numar<=7:
#     print(numar)
#     numar +=1
#
# #3. Vreau sa ii printez pe cei 101 dalmatieni
# numar_dalmatieni = 1
# while numar_dalmatieni <=101:
#     print(f"Dalmatianul curent are numarul {numar_dalmatieni}")
#     numar_dalmatieni += 1

# FOR
# este o structura repetitiva care executa un set de intructiuni pe baza unui range si care se foloseste atunci cand stim exact de cate ori
# vrem sa parcurgm un anumit set de instructiuni. Se bazeaza pe o variabila de iteratie care va stoca rand pe rand valoarea din range
# Componentele unui "for"
#a) inceputul forului marcat de cuvantul "FOR"
#b) variabila de iteratie care va stoca indexul in range
#c) range-ul sau structura repetitiva care este parcursa
#d) separatorul de range ":"
#E) corpul forului (adica o serie de instructiuni)

#ex. vreau sa calculez suma numerelor de la 1 la 10

# suma = 0
# for i in range(1,11):
#     suma+=i
# print(f" Valoarea curenta a sumei este : {suma}")
#
# #Iterare printr-o lista
#
# fructe = ["mar", "banana", "cirese"]
# for fruct in fructe:
#     print(fruct)
#
# #3. Vreau sa ii printez pe cei 101 dalmatieni
# numar_dalmatieni = 1
# for i in range(1,102):
#     print(f"Dalamatianul curent are numarul {i}")

# For Each
# Diferenta intre for si for each este aceea ca in cazul for-ului variabila de iteratie stocheazza indezul curent al elementului
# din lista in timp ce la for each variabila de iteratie stocheaza valoarea curenta a elementului aflat la un anumit index

#ex. 1
# lista = [1,2,3,4]
# for element in lista:
#     print(element)
# In concluzie for este mai util atunci cand vrem sa modificam o valoare in lista pentu ca se acceseaza pe baza de index. For each este mai util
# atunci cand vrem sa scoate un element din lista petru a nu se calcula lungimea listei.

# METODE DE CONTROL AL STRUCTURILOR REPETITIVE
# exista cateva metode de control al structurilor repetitive (bucle), cum ar fi "break", "continue" si "else" in buclele "for" si "while".

#a) BREAK = incheie executia tuturor iteratiilor curente si viitoare in bucla

#Ex.
for i in range(1,11):
    if i == 5:
        break
    print(i)

#b)CONTINUE - sare peste iteratia curenta, dar executa iteratia viitoare

#ex.
for i in range(1,11):
    if i == 5:
        continue
    print(i)

#c) ELSE in bucla for  = este executata atunci cand bucla se termina normar (fara a fi intrerupta de break)

#ex.
for i in range(1,6):
    print(i)
else:
    print("Bucla a fost parcursa complet")

#d) ELSE in bucla while = este executata atunci cand conditia din bucla devine falsa

#ex.
i = 1
while i <=5:
    print(i)
    i+=1
else:
    print("Conditia nu mai este adevarata")

#ex.  Vrem sa parcurgem o lista de masini si sa alegem din lista doara daca este mercedes

lista_masini = ["Audi","Skoda", "Ferrai", "Mercedes", "Trabant", "Dacia", "Mustang", "Tesla"]
i = 0
while i <len(lista_masini):
    if lista_masini[i] == "Mercedes":
        print(f"Am gasit masina dvs")
        break
    i+=1

