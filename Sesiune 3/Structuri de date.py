#STRUCTURI DE DATE - structurile de date reprezinta adrese de memorie care pot stoca mai multe valori
# Exista patru structuri de date principale : Liste, Seturi, Tupluri si Dictionare
#Listele - suntr structuri care permit stocarea si manipularea unui numar variabil de elemente. Listele sunt ordonate
# si indexate (indexarea incepe de la 0). Listele sunt mutabile, ceea ce inseamna ca pot fi modificate (se pot adauga,
# sterge si modifica) dupa ce au fost create. Listele sunt definite prin incadrarea elementelor intre paranteze drepte "[]"
# lista permite elemente duplicate
#Adaugarea elementelor se poate face la finalul listei cu functia append(), dar se poate face adaugare si in interiorul
# liste cu functia insert(). Stergerea elementelor din lista se face atat prin metoda pop (prin metoda pop se sterge ultimul
# elemt din lista) cat si prin functia del (sterge un element de la un index precizat)

lista = [1, 2, 3, "patru", 5.1, True]
print(f"Aceasta este lista mea {lista}")
print(f"Tipul listei este {type(lista)}")
#Indexarea listelor
primul_element = lista[0]
print(primul_element)
al_doilea_element = lista[1]
print(al_doilea_element)
print(f"Aceasta este elemtul de la index 3 : '{lista[3]}'")# metoda recomandata pt economie de cod
#Slicing lista - permite extragere unei portiuni din lista
print(f"Portiunea din lista este {lista[1:3]}")
print(f"Portiunea din lista este {lista[3:5]}")
print(f"Portiunea din lista este {lista[:5]}")
#Adaugare de elemente intr-o lista
lista.append(3)
print(f"Am adaugat un nou element. Lista arata asa : {lista}")
lista.insert(1,9)
print(lista)
#Stergere de elemente
print(f'Am sters un element prin metoda pop cu argument, elementul sters este {lista.pop(1)}')
print(f"lista mea arata asa {lista} ")
lista.append(10)
print(lista)
print(f'Am sters un element prin metoda pop fara sa dau argument, elementul sters este {lista.pop()}')
# del lista[3]
print(f"Asa arata lista dupa ce am folosit functia del : {lista}")
# lista.remove(5.1)
print(f"Asa arata lista dupa ce am folosit functia remove : {lista}")
# Concatenare de doua liste - se foloseste operatorul +
lista1 = [1,2,3]
lista2 = [4,5,6]
lista_concatenata = lista1+lista2
print(f'Lista concatenata este : {lista_concatenata}')
# Extindere de lista - folosind extend()
lista1.extend(lista2)
print(f' Am extins lista1 cu elementele din lista2, lista arata asa {lista1}')
#Metode si functii pt liste :
print(f'Am folosit functia len, lista are lungimea de {len(lista)} elemente')
print(f'De cate ori apare cifra 3 in lista? {lista.count(3)}')
print(lista)
# print(f'Lista sortata este urmatoare {sorted(lista)}')#sortare ascendenta
# lista.sort(reverse= True)# sortare descendenta
# print(f'Lista sortata este urmatoare {lista}')
print(f'Idexul primei cifre 3 gasite in lista este {lista.index(3)}')
print(f'Idexul primei cifre 2 gasite in lista este {lista.index(2)}')

lista6 = [1, 2, 3, 5.1, 9, -1]
print(f'Cifra cea mai mare din lista este {max(lista6)}')
print(f'Cifra cea mai mica din lista este {min(lista6)}')

#SETURI - sunt colectii neeordonate de elemente unice. Seturile sunt asemanatoare cu listele, dar acestea nu permit
# elemente duplicate si nu au o ordine definita (adica nu sunt indexate). Faptul ca nu sunt ordonate, nu ne permite
# sa accesam elemente pe baza de index, nu putem adauga elemente la o anunita pozitie si nu ne lasa sa extragem un
# singur element din set. Acesta poate fi gestionat doar in intregime. Seturile sunt definite de  paranteze ondulate'{}'
# Pentru ca seturile nu pot contine duplicate , orice incercare de a adauga elemente duplicate va fi ignorat
# (nu va returna eroare dar nici nu va adauga elementul)

set1 = {1, "sapte", 2, 9, 3.23, True}
print(set1)

# existenta unui element in se
exista = 3 in set1
print(exista)
print(f'Exista elementul 3 in set? {3 in set1}')
#adaugare element in set
set1.add(47)
print(f'setul meu dupa adaugare element nou arata asa : {set1}')
#Stergere element
set1.remove(47)
print(f'setul meu dupa stergere element arata asa : {set1}')
#Unirea de seturi
set2 ={1,2,3}
set3 ={3,4,5}
unire = set2.union(set3)
print(f'Acesta este noul set {unire} dupa ce am unit set2 si set3')
#Intersecta seturilor
intersectie = set2.intersection(set3)
print(f' intersectia celor doua seturi este : {intersectie}')
#Diferenta seturilor
diferenta = set3.difference(set2)
print(f'diferenta celor doua seturi este: {diferenta}')

#TUPLE
# sunt structuri de date asemanatoare cu listele, diferenta dintre liste si tuple este ca tuplele sunt imutabile ceea ce inseamna ca nu pot
# fi modificate dupa ce au fost create. Asta inseamna ca putem face orice operatie de acesare a elementelor dar nu putem face operatii de adaugare
# de stergere sau modificari. Tuplele sunt definite utilizand paranteze rotunde (), sau daca contin un singur element trebuie sa punem virgula ','
# dupa acel element deoarece sistemul ar vedea tupla ca o variabila cu valoare de tip integer.

#tupla cu mai multe elemente
tupla1 =(1,2,3,"patru")
print(tupla1)
#tupla cu un singur element
tupla2 = (5,)
print(type(tupla2))
#Tupla fara paranteze (tupla packing)
tupla3 = 1,2,3
print(tupla3)
print(type(tupla3))
#Tupla goala
tupla_goala = ()
print(tupla_goala)

#Indexarea tuplelor
primul_element = tupla1[0]
print(primul_element)
print(f"Primul element din tupla este : '{tupla1[0]}'") # metoda recomandata pt economisire de cod

#Sliceing tupla
print(f"Aceasta este o portiune din tupla : '{tupla1[0:3]}")

#Iterare tuple - se refera la procesul de parcurgere a elementelor dintr-o lista/tupla/sir de caractere si prelucrarea fiecarui element intr-un
# mod specific. Iterarea este realizata cu ajutorul buclelor, de ex bucla "for"

for x in tupla1:
    print(x) # x este o variabila care ia valoarea fiecarui element din tupla in timpul iterari.

#Despachetare tuple (Tuple Unpacking) - este procesul de asignare a valorilor dintr-o tupla unor variabile individuale. Acest proces ajuta la la
# lucrul cu tuplele in diferite contexte. Pentru a despacheta se poate face prin a folosi o tupla pe partea dreapta a unei instructiuni de atribuire
# si de a asigna valorile la variabila individuale pe parte stanga

a,b,c,d = tupla1 # a = 1, b =2, c = 3, d= patru
print(f'Variabila "d" are urmatoarea valoare "{d}"')
print(f'Variabila "c" are urmatoarea valoare "{c}"')

#Dictionare
#dictionarele sunt structuri de date flexibile si ordonate care asociaza chei unice cu valorile corespunzatoare. Dictionarele sunt mutabile,
# adica putem adauga, sterge sau modifica valori din interiorul unui dictionar. Cheile unui dictionar trebuie sa fie unice dar valorile se pot repeta
# Dictionarele sunt definite utilizand acolade ondulate "{}" si au un format cheie:valoare

# Dictionar cheie:valoare
dictionar1 = {"cheie1": 10,
              "cheie2":"Cristina",
              "cheie3": 3.14}
print(dictionar1)
print(type(dictionar1))
#Dictionar gol
dictionar_gol = {}
print(dictionar_gol)

# adaugarea unui element in dictionar
dictionar1["cheie4"] = "John"
print(dictionar1)
# Acesare valori prin cheie
print(f'Acesta este valoare cheii 2 din dictionar : {dictionar1["cheie2"]}')
# Iterare prin dictionare
for cheie, valoare in dictionar1.items():
    print(f" Cheia este : {cheie}, Valoarea este : {valoare}")
# apeland metoda items() asupra dictionariului returneaza o secventa de tupluri de genul (("cheie1",10), ("cheie2","Cristina"....etc)

#Verificarea existentei unei chei
print(f"Exista 'cheia3' in dictionar? {'cheie3' in dictionar1}")

# Sterhere unui element prin intermediul cheii
# del dictionar1["cheie1"] # stergere prin metoda del
# print(dictionar1)
# dictionar1.pop("cheie4")
# print(dictionar1) #stergere prin metoda pop

#actualizarea valorilor unei chei
dictionar1["cheie2"] = "valoare_noua"   # actualizare folosind operatorul de atribuire
print(dictionar1)
dictionar1.update({"cheia3": "adaugare_elemen_prin_update"}) #se va face adaugare de cheie noua pt ca in dictionare nu exista nicio cheie cu numele "cheia3"
print(dictionar1)
dictionar1.update({"cheie3": "valoare_cu_update"}) #actualizare folosind metoda update
print(dictionar1)

# Dictionare imbricate (dictionar in dictionar), mai sunt cunoscute si ca dictionare embedde - 2D - nested

jucatori_de_fotbal = {
    "Ducadam" : {"varsta" : 70, "numar_tricou" : 10, "numar_meciuri" : 50},
    "Nicolita" : {"varsta" : 45, "numar_tricou" : 7,
                  "titluri_campion":{"balon_de_aur": 2016,
                                     "jucatorul_anului" :2010,
                                     "ani_castig":[2016,2020,2010]},
                  "numar_meciuri":30}
}
print(f"Nicolita a fost jucatorul anunului in : {jucatori_de_fotbal['Nicolita']['titluri_campion']['jucatorul_anului']}")
print(f"Al doilea an in carea a castigat Nicolita a fost in anul : {jucatori_de_fotbal['Nicolita']['titluri_campion']['ani_castig'][1]}")