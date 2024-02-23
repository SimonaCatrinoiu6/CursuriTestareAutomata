import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class alerte(unittest.TestCase):
    JS_ALERT_LOCK=(By.CSS_SELECTOR,'[onclick=\'jsAlert()\']')
    RESULT_LOC=(By.CSS_SELECTOR,'[style="color:green"]')
    def setUp(self) -> None:
        self.chrome=webdriver.Chrome()
        self.chrome.maximize_window()
        self.URL='https://the-internet.herokuapp.com/javascript_alerts'
        self.chrome.get(self.URL)
        self.chrome.implicitly_wait(5)
    def tearDown(self) -> None:
        print('Eliberam driver-ul')
        self.chrome.quit()
    def testJsAlert(self):
        self.chrome.find_element(*self.JS_ALERT_LOCK).click()
        time.sleep(1)
        self.chrome.switch_to.alert.accept()
        time.sleep(1)
        msg=self.chrome.find_element(*self.RESULT_LOC).text
        assert 'You successfully clicked an alert' in msg


