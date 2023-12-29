from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

chrome.maximize_window()

chrome.get('https://formy-project.herokuapp.com/scroll')

#cautarea in bagina web pt CSS selector se poate face :
# Selectare dupa ID = #myID
#Selectarea dupa clasa = .myClass
#Seelectarea dupa tipul de element = input
#Cautarea primului copil a unui element se poate face cu caracterul '>' sau cu sintaxa first-of-type
# cautarea ultimului copil al unui element se face cu sintaxa last-of-type
# un copil care nu este nici primul nici ultimul se foloseste nth-of-type

chrome.find_element(By.CSS_SELECTOR, 'input#name').send_keys('Cristina')    #am cautat dupa ID
sleep(2)
chrome.find_element(By.CSS_SELECTOR, 'input.form-control').send_keys(' Dumitru')       #am cautat dupa clasa
sleep(2)
chrome.find_element(By.CSS_SELECTOR, 'input[placeholder = "MM/DD/YYYY"').send_keys('14/12/2023')    # am cautat dupa placeholder
sleep(2)
chrome.find_element(By.ID, 'logo').click()
sleep(2)
chrome.find_element(By.PARTIAL_LINK_TEXT, 'Web Form').click()
sleep(2)
chrome.find_element(By.CSS_SELECTOR, 'div input[placeholder*="first name"]').send_keys("Cristina")
# folosim *= petru a nu scrie tot continutul placeholderului
# *= inseamna contine
sleep(2)
chrome.find_element(By.CSS_SELECTOR, 'div input[placeholder*="last name"]').send_keys("Dumitru")
sleep(2)

#Ex. am facut navigare din parinte in copil combinata cu cautare dupa tip atribut -valoare
text_lable_name = chrome.find_element(By.CSS_SELECTOR, 'strong > label[for="last-name"]').text
text_afisat_pe_web = text_lable_name
textul_asteptat = 'Last name'

try:
    assert text_afisat_pe_web==textul_asteptat
    print("Titlul este corect :'{}'".format(text_afisat_pe_web))
except AssertionError:
    print("Mesajul este gresit. Asteptat {}. Actual {}".format(textul_asteptat, text_afisat_pe_web))