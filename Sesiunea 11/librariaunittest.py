'''
Libraria Unittest

1. pentru a putea folosi aceasta librarie va trebui sa creem clase de test care sa o mosteneasca

import unittest
# modulul unitteste face parte din biblioteca Python standard si furnizeaza un framework pentru testare unitara si automata

class MyTest(unittest.TestCase):
    #unittest.TestCase este clasa de baza pe care o vom extinde cu diferite teste.
    def testeaza_ceva(self)
        ....cod de testare...

Atunci cand ne folosim de libraria unittest, clasa de baza va trebui sa contina si urmatoarele componente
a) setup - contine instructiuni ce trebuie sa fie executate inainte de fiecare test (preconditii)
b) teardown - contine instructiuni ce trebuie sa fie executate dupa fiecare test

ex.
class MyTest(unittest.TestCase):
    def setUp(self):
        #pregatirea resurselor pentru teste
        pass

    def tearDown(self):
        #curatarea resurselor dupa test
        pass

    def testeaza_ceva(self):
        #cod de testare

Fiecare clasa de test trebuie sa inceapa OBLIGATORIU cu prefixul test_ ca sa poata fi recunoscut de pachetul pytest
Orice metoda va trebui sa se termine cu o instructiune de assert
Unittest furnizeaza o serie de metode de asert pe care le putem folosi, cum ar fi : assertEqual, assertTrue, assertIn, etc

EX.
class MyTest(unittest.TestCase):
    def testeaza_ceva(self):
        x=1
        self.assertEqual(x, 1, "x nu este 1")

Atunci cand vrem sa sarim unele teste la rulare ne putem folosi de decoratorul @unittest.skip plasat inaintea fiecarei metode de test
pe care ne dorim sa o sarim

class MyTest(unittest.TestCase):

    @unittest.skip                      #acest test va fi sarit
    def test_testeaza_ceva(self):
        x=1
        self.assertEqual(x, 1, "x nu este 1")

    def test_altceva(self):             # acest test va fi executat.
        pass

Executarea testelor :
click pe triunnghiul verde de langa numele clasei de test - va rula toate testela din  acea clasa
click pe triunnghiul verde de langa numele metodei de test - va rula doar metoda respectiva
rulare din terminal unui fisier de teste specific : python -m filename.py
rulare din teminal a tuturor fisierelor de test : python -m unittest
'''

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from selenium.webdriver.support import expected_conditions as EC

class Test(unittest.TestCase):
    #aici definim constantele care sa stocheze valoareea de cautare a selectorului pe care il cautam.Pentru a indica
    # ca o variabila trebuie tratata ca si constanta se folosestc majuscule in denumirea lor
    FIRST_NAME_INPUT = (By.ID, 'first-name')
    LAST_NAME_INPUT = (By.ID, 'last-name')
    JOB_TITLE_INPUT = (By.ID, 'job-title')
    HIGH_SCHOOL_BTN = (By.ID, 'radio-button-1')
    MALE_CHECK_BOX = (By.ID, 'checkbox-1')
    YRS_OF_EXP_0_1 = (By.XPATH, "//*[@id = 'select-menu']/option[2]")
    DATE_SELECT = (By.ID, 'datepicker')
    SUBMIT_BTN = (By.XPATH, "//a[@role = 'button']")

    def setUp(self) -> None:    #->None inseamna ca aceasta functie nu returneaza nimic explicit. Functiile de coonfigurare
# teste cum ar fi setUp si tearDown sunt adesea definite sa nu returneze nimic
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://formy-project.herokuapp.com/form')

    def tearDown(self) -> None:
        self.chrome.quit()

    @unittest.skip
    def test_check_url(self):
        actual = self.chrome.current_url
        expected = 'https://formy-project.herokuapp.com/form'
        self.assertEqual(actual, expected, 'The page is not correct')
        sleep(2)

    def test_form(self):
        input_fist_name = self.chrome.find_element(*self.FIRST_NAME_INPUT)
        input_fist_name.send_keys('Lidia')
        self.assertTrue(input_fist_name.is_displayed(), 'Mesajul afisat este corect')
        sleep(2)
        self.chrome.find_element(*self.LAST_NAME_INPUT).send_keys("Popa")
        sleep(2)
        self.chrome.find_element(*self.JOB_TITLE_INPUT).send_keys('Tester')
        sleep(2)
        self.chrome.find_element(*self.HIGH_SCHOOL_BTN).click()
        sleep(2)
        self.chrome.find_element(*self.MALE_CHECK_BOX).click()
        sleep(2)
        self.chrome.find_element(*self.YRS_OF_EXP_0_1).click()
        sleep(2)
        self.chrome.find_element(*self.DATE_SELECT).click()
        sleep(2)
        self.chrome.get_screenshot_as_file('ss_pagina.png')

    def test_submit_button(self):
        self.chrome.find_element(*self.SUBMIT_BTN).click()
        # actual = WebDriverWait(self.chrome, 5).until(EC.text_to_be_present_in_element((By.XPATH, '/html/body/div/div'),
        #                                              ""))
        # if actual:
        #     print("Message found is correct")
        # else:
        #     print("message found is incorrect")

        element = WebDriverWait(self.chrome, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div')))

        if 'The form was' == element.text:
            print("Message found is correct")
        else:
            print("Message found is incorrect")

