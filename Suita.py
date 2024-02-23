import unittest
import HtmlTestRunner

from Sesiunea11Login import TestLogin
from Sesiunea12_alerte import alerte


class Test_Suite(unittest.TestCase):
    def test_suite(self):
        suita=unittest.TestSuite()
        suita.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(TestLogin),
                        unittest.defaultTestLoader.loadTestsFromTestCase(alerte)])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title='TestReport',
            report_name='Smoke Test Result2'
        )
        runner.run(suita)
