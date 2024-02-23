import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

try:
    chrome = webdriver.Chrome()
    URL = 'https://formy-project.herokuapp.com/form'
    # navigam spre URL-ul de mai sus
    chrome.get(URL)
    time.sleep(2)
    # maximizam fereastra driver-ului(chrome)
    chrome.maximize_window()
    # Gasiti si completati campul ''first name
    firstNameInput = chrome.find_element(By.ID, 'first-name')
    firstNameInput.send_keys('Matei')
    # Gasiti si completati campul ''last name: tag[atribut='value']
    lastNameInput=chrome.find_element(By.CSS_SELECTOR, 'input[placeholder=\'Enter last name\']')
    lastNameInput.send_keys('Nicolae')
    # Gasiti si completati campul ''job title folosind un selector XPath
    jobTitleInput=chrome.find_element(By.XPATH,'//div[3]/input[contains(@type,\'text\')]')
    jobTitleInput.send_keys('Tester')
    #Faceti click pe optiunea'Highschool'din HLOEducation
    #Cele doua linii de mai jos sunt echivalente
    chrome.find_element(By.XPATH,'//div[2]/input[contains(@type,\'radio\')]').click()
    HighSchool=chrome.find_element(By.XPATH,'//div[2]/input[contains(@type,\'radio\')]')
    HighSchool.click()
    #Alegeti genul: Click on male/female
    chrome.find_element(By.CSS_SELECTOR,'#checkbox-2').click()
    #Selectati '2-4'ani de experienta folosind obiectului select din Selenium
    yearsDropdown=Select(chrome.find_element(By.ID,'select-menu'))
    yearsDropdown.select_by_value('2')
    #Selectati ziua in curs
    #datepicker
    chrome.find_element(By.ID,'datepicker').click()
    time.sleep(3)
    chrome.find_element(By.CSS_SELECTOR,'[class=\'today day\']').click()
    #Folosind Linktext dati click pe Submit





finally:
    time.sleep(3)
    chrome.quit()
