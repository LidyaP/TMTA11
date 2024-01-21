import unittest
from HTMLTestRunner.runner import HTMLTestRunner
# import HtmlTestRunner

from Sesiunea12.alerte import Alerts
from Sesiunea12.imitand_tastatura import Keyboard
from Sesiunea12.context_meniu import ContextMenu
from Sesiunea12.autentificare_baza import Autentification
from Sesiunea12.edge import Browser

class TestSuite(unittest.TestCase):

    def test_suite(self):
        teste_de_rulat = unittest.TestSuite()
        teste_de_rulat.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Alerts),
            unittest.defaultTestLoader.loadTestsFromTestCase(Keyboard),
            unittest.defaultTestLoader.loadTestsFromTestCase(ContextMenu),
            unittest.defaultTestLoader.loadTestsFromTestCase(Autentification),
            unittest.defaultTestLoader.loadTestsFromTestCase(Browser)
        ])
        runner = HTMLTestRunner(log=True, verbosity=2, output= 'report', title= 'Test report', report_name= 'report',
                                open_in_browser=True, description= 'HTMLTestreport', tested_by='Lidia')

        runner.run(teste_de_rulat)