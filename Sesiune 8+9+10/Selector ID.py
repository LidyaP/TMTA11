from time import sleep          #ca sa stea pagina deschisa cat ne dorim noi, pt asta se face importul

from selenium import webdriver  #Acest import aduce în Python modulul webdriver din biblioteca Selenium. Acest modul furnizează clase și metode
                                # pentru controlul browserelor web
from selenium.webdriver.chrome.service import Service #Importa clasa Service din modulul selenium.webdriver.chrome.service. Aceasta clasa este utilizata
                                            # pentru a controla serviciul WebDriver Chrome, care este necesar pentru a rula Selenium cu browser-ul Google Chrome.
from webdriver_manager.chrome import ChromeDriverManager # #Acest import aduce în Python clasa ChromeDriverManager din modulul webdriver_manager.chrome.
                                # Aceasta clasa este folosita pentru a gestiona descărcarea și gestionarea automata a driverului Chrome necesar pentru Selenium.
                                # In loc să descarcați manual un driver și să gestionați actualizarile, acest modul face acest lucru automat.
#pt mozila : from webdriver_manager.firefox import GeckoDriverManager
#pt Edge : from webdriver_manager.microsoft import EdgeChromiumDriverManager
#pt Safari : from webdriver_manager.safari import SafariDriverManager
#pt Opera : from webdriver_manager.opera import OperaDriverManager

from selenium.webdriver.common.by import By #Acest import aduce in Python clasa By din modulul selenium.webdriver.common.by. Clasa By conține metode utile pentru
                                            # a selecta elemente pe bază de diferite criterii, cum ar fi ID, clasa, tag etc.

# initializare chrome
s = Service(ChromeDriverManager().install())    #descarca și instaleaza versiunea potrivită a ChromeDriver în funcție de versiunea actuală a browserului Chrome instalat pe sistem.
chrome = webdriver.Chrome(service=s)    #Se creeaza o instanța a browserului Chrome (webdriver.Chrome) și se furnizeaza serviciul configurat. Astfel, Selenium va utiliza ChromeDriver
                                        # pentru a controla browserul Chrome.
#In cazul in care folositi o versiune mai veche de Pycharm va trebui sa va setati descarcarea driverului corect
# in mod dinamic si puteti face asta prin comanda de mai jos:
#chrome = webdriver.Chrome(executable_patch = ChrimeDriverManager().install())

#navigam catre un url
# chrome.get('https://formy-project.herokuapp.com/')
#maximizare fereastra
chrome.maximize_window()
sleep(3)                #Sleep introduce o pauză fixa, indiferent dacă actiunea a fost finalizata sau nu, in timp ce Implicit Wait și Explicit Wait
                        # așteapta ca o conditie specifica să fie indeplinita inainte de a continua executia.


#inchidera instantei de Chrome ! Se va folosi dupa ce am inserat toate testele dorite
# chrome.quit()
#inchiderea unui tab din Chrome
# chrome.close()

# Selector ID
# cautarea in web se poate face folosind : [id='valoareaID']
chrome.get('https://formy-project.herokuapp.com/form')

# first_name = chrome.find_element(By.ID,'first-name')
# sleep(1)
# first_name.send_keys("Lidia")
# sleep(2)
# last_name = chrome.find_element(By.ID, 'last-name')
# sleep(1)
# last_name.send_keys("Popa")
# sleep(2)

#metoda recomandata pt economisire de cod
# chrome.find_element(By.ID, 'last-name').send_keys("Popa")
# sleep(2)

# Modelul pe care il veti folosi in testare
try:
    first_name = chrome.find_element(By.ID,"first-name" )
    first_name.send_keys("Lidia")
except:
    print("Id-ul nu este corect")
print("Am reusit cu succes")

