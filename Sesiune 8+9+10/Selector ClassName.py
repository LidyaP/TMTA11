from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# initializare chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

#maximizare fereastra
chrome.maximize_window()

# Selector ClassName - bazat pe clasa
chrome.get('https://formy-project.herokuapp.com/')
#EX.1
# clasa_mea = chrome.find_element(By.CLASS_NAME, 'nav-link')
# sleep(2)
# clasa_mea.click()
# sleep(2)

#EX.2
# chrome.find_element(By.CLASS_NAME, 'nav-link').click()
# sleep(2)

#Ex.3

element_web = chrome.find_element(By.CLASS_NAME, 'lead')
textul_de_pe_element = element_web.text
expected_text = "This is a simple site that has form components that can be used for testing purposes."

try:
    assert textul_de_pe_element == expected_text
    print("Mesajul este corect : '{}'".format(textul_de_pe_element))
except AssertionError:
    print("Mesajul este gresit. Asteptat {} . Actual {}".format(expected_text, textul_de_pe_element))


