import pytest

# from tests.modules.mesTestsAutos import test_contact_form

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#test_contact_form()

driver.get("file:///C:/Users/Formations/formations/seleniumPython/siteTest/index.html")

# Attente explicite pour le chargement des éléments
wait = WebDriverWait(driver, 10)

name_label = driver.find_element(By.ID, 'nom_user')

try:
    assert name_label is not None
    assert name_label.text == "Votre nom :"
    print("Le test a réussi !")
except AssertionError:
    print("Le test a échoué !")