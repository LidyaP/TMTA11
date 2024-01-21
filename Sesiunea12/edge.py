from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
# import unittest
from selenium.webdriver.support import expected_conditions as EC
from unittest import TestCase
from webdriver_manager.microsoft import EdgeChromiumDriverManager

class Browser(TestCase):

    def setUp(self) -> None:
        self.edge = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        self.edge.maximize_window()
        self.edge.get('https://formy-project.herokuapp.com/form')

    def tearDown(self) -> None:
        self.edge.quit()

    def test_edge(self):
        first_name = self.edge.find_element(By.ID, "first-name")
        first_name.send_keys("Lidia")