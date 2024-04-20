from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from faker import Faker
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("file:///Users/gaetanduez/Documents/SSID/monsite/contact.html")

#input("Appuyez sur une touche pour quitter")
wait = WebDriverWait(driver, 5)
fake = Faker()

#ChampsName = wait.until(EC.element_to_be_clickable((By.NAME, "nom_user")))
#ChampsName.click()

mes_champs = ["nom_user", "prenom_user", "message", "email", "genre"]

for champs in mes_champs:
    try:
        champsAtester = driver.find_element(By.NAME, champs)
        typeChamps = champsAtester.get_attribute("type")

        assert champsAtester.is_displayed()

        if typeChamps == "email":
            valeurAsaisir = fake.email()
        elif typeChamps == "radio":
            champsAtester.click()
            valeurAsaisir = champsAtester.get_attribute("value")
        else:
            valeurAsaisir = "Test de saisie"

        champsAtester.send_keys(valeurAsaisir)

        valeurDuChamps = driver.find_element(By.NAME, champs).get_attribute("value")

        print(f"Le test du champs [{champs}] de type [{typeChamps}] est OK et sa valeur est : [{valeurDuChamps}]")
        time.sleep(1)

    except NoSuchElementException:
        print(f"Le test du champs [{champs}] est KO")

"""
liste_champs = [
    ("nom", "text"),
    ("prenom", "text"),
    ("message", "textarea"),
    ("email", "email")
]

for champs, type_champs in liste_champs:
    try:
        champsAtester = driver.find_element(By.NAME, champs)

        assert champsAtester.is_displayed()

        if type_champs == "email":
            valeurAsaisir = fake.email()
        else:
            valeurAsaisir = "Test de saisie"

        champsAtester.send_keys(valeurAsaisir)

        valeurDuChamps = driver.find_element(By.NAME, champs).get_attribute("value")
        print(f"Le test du champs [{champs}] est OK et sa valeur est : [{valeurDuChamps}]")

    except NoSuchElementException:
        print(f"Le test du champs [{champs}] est KO")


try:
    champs = driver.find_element(By.NAME, "nom_user")
    champs.send_keys("Test de saisie")
    print("C'est OK pour la saisie")
except NoSuchElementException:
    print("La saisie n'a pas fonctionné")
"""

#driver.quit()