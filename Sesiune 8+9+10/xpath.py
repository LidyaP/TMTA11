# Xpath
#Xpath- este de doua tip-uri :
#xpath absolut = o adresa completa incepand de la inceputul paginii si desfasurat din parinte in copil pa la elementul cautat.
# Atunci cand se face cautare dupa xpath absolut se folosesete caracterul '/'
#xpath relativ = o adresa partiala incepand cu primul element unic identificat pe pagina si defasurt din parinte in copil sau
# din copil in parinte, sau din frate in frate pana la identificarea elementului cautat. Atunci cand se face cautare de xpath
# relativ se foloseste caracterul '//'

# Modalitati prin care putem sa folosim xpath-ul relativ :

#Cautare dupa atribut-valoare pentru un tag specific
# EX. //button - sistemul va cauta toate elementele de pe site care au tag-ul button

# Cautare dupa atribut- valoare. atunci cand facem cautare dupa atribut-valoare, atributul trebuie precedat intodeauna de caracterul @.
# De asemenea se va plasa perechea cheie-valaore intre paranteze '[]'
# EX. //button[@class = 'navbar-toggler'] - sistemul va cauta toate elementele care au tagul button si perechea atribut-valoare ( in cazul nostru
# atributul este class iar valoarea este navbar-toggler)

# atunci cand nu stim sau nu ne intereseaza tag-ul, putem face cautare dupa atribut valoare prin intermediul caracterului '*'
# caracterul '*' este echivalentul lui all (tot)
#Ex. //*[@class = 'navbar-toggler'] -  sistemul cauta in tot codul HTML clasa precizata de noi

#!! atentie la XPATH daca avem clase care au valoare formata din elemente separate prin spatiu TREBUIE sa le punem pe toate
# ex //*[@class = 'navbar navbar-expand-lg bg-light']

# Cautare dupa copil prin navigare in jos -  ne folosim de operatorul '/'

# EX. sa presupunem ca avem un HTML de genul :
"""
<div id = 'parinte'>
    <p>Primul paragraf</p>
    <p>Al doilea paragraf</p>
</div>

daca vrem sa selectam al doilea paragraf construim Xpath-ul ca mai jos
//div[@id = 'parinte']/p[2]
"""


from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

chrome.maximize_window()

# chrome.get('https://formy-project.herokuapp.com/form')

# cautare cu Xpath folosindu-ne la constructia Xpath-ului de doua conditii (ambele sunt adevarate)
# chrome.find_element(By.XPATH, "//[@placeholder = 'Enter first name'] | //*[@placeholder = 'Enter last name']").send_keys("Cautare cu OR")


'''
sa zicem ca avem un cod html :
<div class = 'clasa1'>Element cu clasa 1</div>
<div class = 'clasa2'>element cu clasa 2</div>

Constuim Xpath ca sa ne aduca toate div-urile care sunt cu clasa1  si clasa2
//div[@class = 'clasa1'] | //div[@class = 'clasa2']
sau
//div[@class = 'clasa1' or @class = 'clasa2']

cautare cu OR doar a doua conditie adevarata

//div[contains(@class, 'clasa1') or contains(@class, 'clasa2')]

'''
# cautare Xpath dupa text

chrome.get('https://the-internet.herokuapp.com/javascript_alerts')
chrome.find_element(By.XPATH, "//button[text() = 'Click for JS Alert']").click()
sleep(3)


'''
navigarea pe axa x si y
1. Navigare din parinte in copil se face cu caracterul /
ex. //div/p
2. navigare catre un urmas care nu este urmasul direct. ne folosim de //. 
ex. //div/p//input
3. Navigare in sus catre parinte se facu cu '//parent::tag'
ex.//p/parent::div - specifica sa selectam parintele nodului curent care are eticheta div
4. Navigare la urmatorul frate cu "/following-sibling::tag'
ex. //div/following-sibling::p
5 navigare la fratele anterior cu "/preceding-sibling::tag"
ex. //p/preceding-sibling::p

xpath absolut = /html/body/div[2]/div/div/ul/li[1]/button
xpath relativ = //*[@id="content"]/div/ul/li[1]/button
'''