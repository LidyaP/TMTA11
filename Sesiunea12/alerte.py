from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
# import unittest
from selenium.webdriver.support import expected_conditions as EC
from unittest import TestCase

class Alerts(TestCase):

    ALERT = (By.XPATH, "//button[text() = 'Click for JS Alert']")
    CONFIRM = (By.XPATH, "//button[text() = 'Click for JS Confirm']")
    PROMPT = (By.XPATH, "//button[text() = 'Click for JS Prompt']")
    TEXT_TO_SEND = ('ala1235')

    def setUp(self) -> None:
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://the-internet.herokuapp.com/javascript_alerts')

    def tearDown(self) -> None:
        self.chrome.quit()

    def test_alert(self):
        self.chrome.find_element(*self.ALERT).click()
        sleep(2)
        # schimbam controlul pe pop up de alerta
        obiect = self.chrome.switch_to.alert
        #extragem textul din obiect cu funxtia .text si il printam
        print("Alert show following message " + obiect.text)
        sleep(2)
        obiect.accept() #metoda accept este echivalentul clickului pe butonul OK din alerta
        print("Clicked on the OK button in the Alert Window")
        sleep(2)

    def test_confirm_ok(self):
        self.chrome.find_element(*self.CONFIRM).click()
        sleep(1)
        obiect = self.chrome.switch_to.alert
        print(f"Alert show following message : {obiect.text} ")
        sleep(1)
        obiect.accept()
        print("Clicked on the OK button in the Alert Window")
        sleep(1)

    def test_confirm_cancel(self):
        self.chrome.find_element(*self.CONFIRM).click()
        sleep(1)
        obiect = self.chrome.switch_to.alert
        print(f"Alert show following message : {obiect.text} ")
        sleep(1)
        obiect.dismiss() #metoda dismiss este echivalentul butonului Cancel din alerta
        print("Clicked on the CANCEL button in the Alert Window")
        sleep(1)

    def test_promt(self):
        self.chrome.find_element(*self.PROMPT).click()
        sleep(1)
        obiect = self.chrome.switch_to.alert
        print(f"Alert show following message : {obiect.text} ")
        obiect.send_keys(self.TEXT_TO_SEND)
        sleep(2)
        obiect.accept()
        sleep(3)
        print("Clicked on the OK button in the Alert Window")
        sleep(1)


