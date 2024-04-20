import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest_bdd import scenario, given, then

# Define your Selenium WebDriver fixture
@pytest.fixture
def browser():
    driver = webdriver.Chrome()  # Assurez-vous que le pilote est installé et configuré correctement
    yield driver
    driver.quit()

# Link the scenario in your feature file to a test function
@scenario('features/contact_form.feature', "Verify the presence of the input field")

def test_input_field_presence():
    pass  # The actual test steps will be performed by the step implementations below

# Define the steps used in the scenario
@given('I am on the contact page')
def open_contact_page(browser):
    browser.get("https://gaetanduez.fr/test/contact.html")  # Changez cette URL par l'URL réelle de votre page de contact

"""
@then('I should see the "nom" input field')
def see_nom_input_field(browser):
    assert browser.find_element(By.NAME, 'nom').is_displayed()
"""

@then('I should see the "nom" input field')
def see_input_field(browser):
    assert browser.find_element(By.NAME, "nom").is_displayed()

@then('I should see the "prenom" input field')
def see_input_field(browser):
    assert browser.find_element(By.NAME, "prenom").is_displayed()

@then('I should see the "email" input field')
def see_input_field(browser):
    assert browser.find_element(By.NAME, "email").is_displayed()

@then('I should see the "message" textarea')
def see_input_field(browser):
    assert browser.find_element(By.NAME, "message").is_displayed()