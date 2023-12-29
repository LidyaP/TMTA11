# #String index = un sir caractere este ordonat in sensul in care orice caracter din acel sir are o pozitie specifica
# # numita index. In orice string indexul porneste de la pozitia 0
# list = [1, 2, 3, 4, "Maria"]
# #elementul cu valoarea 1 are index 0
# #elementul cu valoarea 2 are index 1
# #elementul cu valoarea 3 are index 2 etc.
# element = list[2] # accesarea elementului cu index 2 , o sa returneze cifra 3
# print(f" Elementul cu index 2 este : {element}")
# #Indexarea negativa se foloseste pentru a accesa elemente in sens invers. incepand -1 care resprezinta ultimul element din
# #sir, -2 pentru penultimul element etc.
# last_element = list[-1]# accesam ultimul element din lista, o sa returneze 4
# print(f"Ultimul element din lista este : {last_element}")
# #String lenght - il folosim daca vrem sa aflam cate caractere are string, ne folosim de functia length (len)
# my_text = "Hello, World!"
# # lungime = len(my_text)
# # print(f"Variabila mea are lungimea de {lungime} caractere")
# print(f"Variabila mea are {len(my_text)} caractere") #prin metoda folosiri functiilor direct in prin se face economie de cod
# print(f'Lista mea are o lungime de {len(list)} caractere')# la extragerea lungimi din liste sau dictionare, nu va numara
#                                                         #virgula si spatiile asa cum face la stringuri
# #String slicing - o modalitate prin care putem sa extragem doar o parte ,sau intreg, etc dintr-un string.
# #Putem sa extragem atat intregul sir de caractere, cat si portiuni ori de inceput pana la o anumita pozitie, de la
# #o anumita pozitie pana la sfarsit sau un set de caractere din interior
# # Structura unui slicing este [pozitie_de_start:pozitie_de_end:steps]
# #Atentie!! Pozitia_de_end nu se in considerare ca si limita finala.De exemplu daca ne intereseaza sa extragem caracterele
# #de la pozitia 3 la pozitia 8 fiecare caracter . o sa scriem slicing-ul [3:9:1]
# #pozitie_de_stat - pozitia de incput a slicing-ului (in mod implit se incepe de inedex 0)
# #pozitie_de_end - pozitia de final (nu e luat in considerare la calcul)
# #step - pasul de parcurs (fiecare al catalea caracter este luat in considerare)
# # ':' separator de elemente.
# # In mod implicit pozitia de inceput este 0, pozitia de final e ultimul caracter si pasul este 1
#
# str_exemplu = "Ana are mere"
# print(f'Primele 3 carcatere din variabila noastra sunt : "{str_exemplu[0:3]}"')
# print(f'Ultimul caracter din variabila noastra este : "{str_exemplu[-1]}"')
# print(f'Ultimele trei caractere din variabila sunt : {str_exemplu[-3:]}')# ca sa obtinem ultimele 3 caractere ne folosim
#                                                                 #de '-3:' ca sa inceapa sa citeasca de la final 3 caractere
# print(f'Al 4 caracter de la final este : {str_exemplu[-4]}')
#
# poezie = "Ana are mere si este fericita cu ele si vrea sa mearga acasa"
# #Ex. Extrageti toate caracterele de inceput pana la sfarsit cu mentionarea pasului
# print(poezie[0:len(poezie):1])# folosim  functia len(poezie) petru a determina lungimea sirului si apoi utilizam aceasta
#                         #lungime pentru a accesa toate cararactere din sir si sa facem sliceing
# #Ex 2. Extragem toate caracterele de inceput pana la sfarsit folosind pozitia de inceput si sfarsit implicita
# print((poezie[:]))# va returna acelasi lucru ca mai sus doar ca nu specificam nici pasul nici startul si nici end-ul
# #Ex 3 Extrage toate caracterele de la inceput pana la sfarsit dar sa imi afiseze caracterele din 2 in 2
# print(poezie[::2])
# # Extrage toate caracterele de la pozitia 5 pana la pozitia 10
# print(poezie[5:10])
# # Extrage ultimele 3 caractere din string
# print(poezie[-3:])
# # Printeaza stringul in ordine inversa
# print(poezie[::-1])
# #Metoda string = metoda care poate fi folosita pentru interactiunea cu stringurile
#
# print(poezie.lower())# va transforma toate caraterele in litere mici
# print(poezie.upper())# va transforma toate caraterele in litere mari
# print(poezie.count("si"))
# print(poezie.count("e"))
# print(poezie.islower())
#
# #Metoda split = este folosit pentru a desparti un string intr-o lista de subsiruri
# # Sintaxa este string_subsir = string.split(delimiter)
#     # string este stringul inital pe care ne dorim sa il impartim
#     #delimiter = este caracterul sau sirul de caractere pe baza caruia facem impartirea
#     #string_subsir = stringul care va rezulta
#         # In mod inplicit se va face split dupa spatii (in cazul in care nu dam niciun argument)
#
# text = "Ana are pere si mere"
# print(f"Asa impartim sirul de caractere dupa spatii  {text.split()}")
# data = "22-11-2023"
# print(f'Asa facem split cu argument {data.split("-")}')
#
# #metoda Replace = este folosit pentru a inlocui toate caracterele unui subsir cu alt subsir de caractere
# #sintaxa_nou = string_intial.replace(subsir_vechi, subsir_nou, numar_inlocuiri)
#     # string_initial = sirul initial de caractere in care o a facem inlocuirea
#     #sbusir_vechi = caracterele pe care dorim sa il inlocuim
#     #subsir_nou = caracterele cu care vom inlocui subsirul_vechi
#     #numar_inlocuiri (obtional) = specifica numarul maxim de inlocuiri
#
# original = "Ana are mere. Ana este fericita."
# nou = original.replace("Ana", "Maria")
# print(original)
# print(nou)
#
# #metodele isDecimal/isNumeric/isDigit = au rezultat de tip boolean (True,False)
# #a)isdecimal = verificam daca toate caracterele sunt cifre zecimale (0-9)
# numar ="123456"
# print(f"Este un numar decimal? '{numar.isdecimal()}'")
# #b)isnumeric = verifica daca toate caracterele si sir sunt caractere numerice , inclusiv cele care sunt cifre speciale
# numar1 = "1.23"
# print(f'Este de tip numeric? "{numar1.isnumeric()}"')
# #c)isdigit = verifica daca toate caracterele din sir sunt cifre (0-9) dar include si alte caractere numericice de tip
# # binar,octal etc
# numar2 = "123456"
# print(f"este de tip digit? {numar2.isdigit()}")
# # OPERATORI ARITMETICI
# #sunt utilizatir pentru a efectua operatii matematice
# #1 Operatorul de adunare '+' = adauga doua sau mai multe numere
# a = 5+3 # variabila a va primi valoarea 8
# #2. Operatorul de scadere '-' =scade un numar din altul
# b =7-2 # variabila va primi valoarea 5
# #3. Operatorul de inmultire '*'
# c = 4*6 # variabila va primi valoarea 24
# #4. Operator de impartire '/' = returneaza o valoare de tip float
# d = 10/3 #variabila va primii valoarea 3.3333 (un numar float)
# #5. Operatorul de impartire intreaga '//' - efectueaza impartirea si returneaza partea intreaga a rezultatului
# e =10//3 # variabila va primi valoare 3
# #6. Operatorul de rest '%' -
# f = 10%3 # variabila va primi valoarea 1, deoarece restrul impartiri lui 10 la 3 este 1
# # 7. Operatorul de putere "**" - ridica un nr la putere
# g = 2**3# variabila va primi valoare 8, deoarece 2 la puterea 3 este 8
# #Operatori de atribuire - este utilizat pentru a atribui o valoare unei variabile
# #1. Operatorul de atribuire simplu '=' - atribuie o valoare unei variabile
# x = 5 # variabilei x i se atribuie valoarea 5
# #2 Operatorul de atribuire cu adaugare '+=' = adauga o valoare la variabila existenta si actualizeaza variabila cu
# # noul rezultat
# a = 10
# a+= 5 # echivalentul a= a+5
# print(a)
# # 3. Operatorul de atribuire cu scadere '-=' = scade o valoare la variabila existenta si actualizeaza variabila cu
# #  noul rezultat
# b = 8
# b-= 3 #echivalent b = b-3
# print(b)
# #4. operatorul de atribuire cu inmultire '*='inmulteste o variabila existenta cu o anumita valoare si actualizeaza
# # variabila cu rezultatul
# c = 4
# c*=2 #echivalentul c = c*2
# print(c)
# #5. operatorul de atribuire cu inpartire '/=' inparte o variabila existenta cu o anumita valoare si actualizeaza
# # variabila cu rezultatul (vom avea un rezultat de tip float)
# d =20
# d/=4 #echivalent d = d/4
# d//=4 # vom avea rezultul fara zecimale
# print(d)
# #6. Operatorul de atribuire cu rest'%=' - calculeaza restul impartirii variabilei la o anumita valoare si actualizeaza
# # variabila cu rezultatul
# e = 17
# e %= 5
# print(e)
# # OPERATORII DE COMPARARE - sunt utilizati pentru a compara doua valori si a determina relaia dintre ele - rezultatele
# # sunt de tip boolean
# #1. Operatorul egal '==' verifica daca doua valori sunt egale
# a = 5
# b = 7
# rezultat = (a==b)
# print(rezultat)
# #2. Operatorul diferit '!=' verifica daca doua valori nu sunt egale
# x = 10
# y = 1
# rezultat = (x!=y)
# print(rezultat)
# #3. Operatorul de mai mic '<' verifica daca o valoare este mai mica decat alta
# p = 3
# q = 6
# rezultat =(p<q)
# print(rezultat)
# #4. Operator de mai mare '>'
# #5. Operatorul de mai mic sau egal '<='
# #6. Operatorul mai mare sau egal '>='
#
# # OPERATORI LOGICI
# #1. AND
# #2. OR
# #3. NOT
# #prioritatea operatoriilor logici este NOT, OR, AND
#
# #1 OPERATORUL and returneaza True daca ambele expresii sau valori sunt adevarate
# numar = 10
# if numar >15 and numar <=20:
#     print('Numar este mai mare decat 15 si mai mic sau egal cu 20')
# else:
#     print('Numarul nu satisface conditia')
#
# x = 1
# rezultat_and = x>3 and x<13
# print(rezultat_and)
# #2 OPERATORUL or - returneaza true daca cel putin una din valori este adevearata
# x = 1
# rezultat_and = x>3 or x<13
# print(rezultat_and)
# #3 Operatorul NOT - returneaza inversul valorii boolean a unei variabile
# x = True
# rezultat_and = not x
# print(rezultat_and)
# #ASSERT - este folosit pentru a verifica daca o anumita conditie este adevarata. Genereaza o exceptie de tip AssertionError
# # in cazul in care conditia nu este adevarata. Assertul este foarte des utilizat in testarea automata deoarece verfica daca
# # conditiile sunt indeplinite.
# # Assertul are urmatoarele componente : pe prima pozitie valoarea pe care o comparam
#                             # pe a doua pozitie valoarea cu care comparam, cele doua valori sunt separate de operatorul
#                             # de comparare '=='
#                             # optional * ultima pozitie un mesaj care sa fie returnat in cazul in care cele doua valori sunt egale
# x = 5
# assert x>1, "Valoarea lui x trebuie sa fie mai mare de 1"
# print("x este mai mare de 1!")
#
# z = 10
# rezultat_not = not(z>3 and z<13)
# print(f'Rezultat NOT: ', rezultat_not)
# # Structurile alternative IF, ELSE si ELIF
# # # sunt utilizate pentru a crea ramificatii in cod in functie de conditii. Aceste structuri sunt varianta automata a metrodei
# # # de testare manuala Decision coverage
# x = 1
# if x > 5:
#     print("x este mai mare decat 5")
# else:
#     print("x nu este mai mare decat 5")
#
# nota = 50
# if nota >=90:
#     print("Nota este A")
# elif 80<= nota <90:
#     print('Nota este B')
# elif 70<= nota <80:
#     print("Nota este C")
# else:
#     print("Nota este sub C")
#
# numar = int(input("Introduceti un nr: \n"))
#
# if numar >0:
#     rezultat = "Numarul este pozitiv"
# elif numar <0:
#     rezultat = "Numarul este negativ"
# else:
#     rezultat = "Numarul este 0"
# assert rezultat == "Numarul este pozitiv" or rezultat == "Numarul este negativ" or rezultat == "Numarul este 0"
# print(rezultat)

numar1 = int(input("Va rugam sa introduceti numarul: \n"))

if numar1 % 2==0:
    print("Numarul este par")
else:
    print("Numarul este impar")




