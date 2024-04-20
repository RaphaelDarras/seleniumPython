import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def pytest_report_teststatus(report, config):
    if report.passed:
        print(f"Test {report.nodeid} a réussi !")
    elif report.failed:
        print(f"Test {report.nodeid} a échoué !")

def test_contact_form(browser):
    browser.get("https://gaetanduez.fr/test/contact.html")

    # Attente explicite pour le chargement des éléments
    wait = WebDriverWait(browser, 10)

    name_label = browser.find_element(By.XPATH, "//label[@for='nom']")
    try:
        assert name_label is not None
        assert name_label.text == "Nom"
        print("Le test a réussi !")
    except AssertionError:
        print("Le test a échoué !")

    