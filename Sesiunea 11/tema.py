import re

from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager import chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import unittest

class Test(unittest.TestCase):
    ACCEPT_BTN = (By.XPATH,'//*[@id="gdprCookieBar"]/div/div[2]/button[2]')
    CONNECT= (By.ID,'authorization-trigger')
    USER=(By.ID,'email')
    PAROLA=(By.NAME,'login[password]')
    CONNECT_BTN=(By.XPATH,'//*[@id="send2"]')
    SELECT=(By.XPATH,'//*[@id="menu-5-65a52e42cc63d"]/ul/li[1]/a')
    CATEG_ANTISTRES=(By.XPATH,'//*[@id="menu-5-65a52e42cc63d"]/ul/li[1]/ul/li[7]/a')
    SORT_PRET =(By.XPATH,'//*[@id="sorter"]/option[4]')
    ERR_MSG= (By.XPATH,"//div[@data-ui-id='message-error']")
    CAUTARE_PROD=(By.ID,'search')
    SEARCH_BTN=(By.XPATH,'//*[@id="search_mini_form"]/div[2]/button')
    NR_PROD= (By.XPATH,'//*[@id = "toolbar-amount"]')
    DECONECTARE = (By.ID, "authorization-trigger")
    DELOGARE = (By.XPATH, "//*[@id='cdz-login-form-dropdown']//*[@class = 'log-out link']")
    CATEG_ANTISTRES = (By.XPATH, '//*[@id="menu-5-65aae4e9932be"]/ul/li[1]/ul/li[7]/a')
    MENU_LINK = (By.XPATH, '//*[@id="menu-5-65aae4e9932be"]/ul/li[1]')
    SORT_PRET = (By.XPATH, '//*[@id="sorter"]/option[4]')
    LISTA_PRODUSE = (By.XPATH, '//*[@id="category-products-grid"]/ol')
    PRET_PRODUS = (By.XPATH, '//*[@id="product-price-2606"]/span')
    def setUp(self) -> None:
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://www.daciaplant.ro/')

    def tearDown(self) -> None:
        self.chrome.quit()

    def test_teste1(self):
        # verif ca se intra pe site si se accepta cookie
        self.chrome.implicitly_wait(10)
        self.chrome.find_element(*self.ACCEPT_BTN).click()
        sleep(2)
        # se verif ca se face logarea cu datele corecte
        self.chrome.find_element(*self.CONNECT).click()
        sleep(2)
        self.chrome.find_element(*self.USER).send_keys('irinavoinea@yahoo.com')
        sleep(2)
        self.chrome.find_element(*self.PAROLA).send_keys('irinairina')
        self.chrome.find_element(*self.CONNECT_BTN).click() #aici nu dadeai click pe connect si primeai un mesaj fals pozitiv
        #din cauza printului care il aveai aici imediat, el printa indiferent daca intrai in cont sau nu
        actual =self.chrome.current_url
        expected = 'https://www.daciaplant.ro/customer/account/'
        self.assertEqual(actual,expected, 'parola corecta.cont creat')
        sleep(2) # aici ti-am facut un assert care sa fie relevant pt ce incercai tu sa testezi, adica sa vezi ca s-a
        # facut conectarea corect

    def test_teste2(self):
            # se verif ca afiseaza mesaj de err daca se introd parola gresita
        self.chrome.implicitly_wait(10)
        self.chrome.find_element(*self.ACCEPT_BTN).click()
        # sleep(2)
        # self.chrome.find_element(*self.DECONECTARE).click()
        # sleep(2)
        # self.chrome.find_element(*self.DELOGARE).click()
        # actual = self.chrome.current_url
        # expected = 'https://www.daciaplant.ro/customer/account/logoutSuccess/'
        # self.assertEqual(actual, expected, 'ne-am delogat')
        sleep(2)
        self.chrome.find_element(*self.CONNECT).click()
        sleep(2)
        self.chrome.find_element(*self.USER).send_keys('irinavoinea@yahoo.com')
        sleep(2)
        self.chrome.find_element(*self.PAROLA).send_keys('parola_gresita')
        self.chrome.find_element(*self.CONNECT_BTN).click() # nici aici nu aveai simulare de click pe butonul de conectare
        # print('parola incorecta')
        sleep(2)
        # error_code_locator = self.chrome.find_element(*self.ERR_MSG)
        # print('Mesajul de eroare este afisat')
        asteptare_eroare = WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located(self.ERR_MSG))
        if 'The account sign-in' in asteptare_eroare.text:
            print('Mesajul de eroare este afisat')
        else:
            print('mesajul de err nu este afisat')

        #aici merge mai bine un bloc decizional de tip IF in loc de TRY

    def test_teste4(self):
        self.chrome.implicitly_wait(10)
        self.chrome.find_element(*self.ACCEPT_BTN).click()
        sleep(2)
                # se verif ca se poate naviga si alege categ Antistres
        self.chrome.find_element(*self.MENU_LINK).click()
        sleep(2)
        self.chrome.find_element(*self.CATEG_ANTISTRES).click()
        sleep(2)
                # se verif ca se face sortare dupa pret in categ Antistres
        self.chrome.find_element(*self.SORT_PRET).click()
        sleep(2)
        produs = self.chrome.find_elements(*self.LISTA_PRODUSE) #identific lista de produse
        pret = []   #creez o lista unde voi adauga fiecare pret
        for product in produs:
            pret_text = product.find_element(*self.PRET_PRODUS).text.strip(' Lei')  #extrag pretul si elimin cuvantul lei
            pret_numeric = float(re.sub(r'[^\d.]', '', pret_text.replace(',', '.'))) #am explicat mai jos
            pret.append(pret_numeric)   #adaug in lista preturile curatate de orice alt caracter care nu este numeric

        preturi_sortate = sorted(pret)      #sortez lista
        assert pret == preturi_sortate, 'Sortarea nu s-a facut corect'  #verific ca lista mea sortata este la fel cu ce s-a gasit pe site

    #1.pentru ca preturile din categoria antistres au preturi reduse, adica sunt afisate de doua ori, atunci cand incerci sa extragi
    #pretul, acesta are pe langa cifre si alte caractere gen litere sau caractere speciale, atunci trebuie sa ne folosim de expresia
    # regulata 're'. expresiile regulate sunt sabloane text care descriu un model de cautare intr-un sir de caractere (cu aceste sabloane
    #putem manipula textul. De exemplu re.sub inlocuieste toate potrivirile ale sablonului cu un sir de caractere dat. in codul meu
    # [^\d.] este sablonul (ce este trecut acolo indica sa fie scase toate caracterele care nu sunt cifre)

    #2. a trebuit sa iti modifica cativa selectori pt ca nu erau corecti, plus ca am adaugat si selectori care au fost necesari
    # sa identificam lista de produse si pretul lor

    #3. iar nu ai desfacut tupla utilizand *, ai scris iar self.MENU_LINK




