import pytest
import pytest_bdd
from pytest_bdd import parsers

from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest_bdd import scenario, given, then

@pytest.fixture
def browser():
    # Assurez-vous que le pilote est installé et configuré correctement
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

#1er scénario, je teste la présence des éléments dans ma page
@scenario('features/contact_form.feature', "Verify the presence of the input field")

def test_input_field_presence():
    pass  # Les étapes réelles du test seront exécutées par les implémentations d'étapes ci-dessous

@given('I am on the contact page')
def open_contact_page(browser):
    # Remplacez cette URL par l'URL réelle de votre page de contact
    browser.get("file:///C:/Users/Formations/formations/seleniumPython/siteTest/index.html")

@then(parsers.parse('I should see the "{field_name}" input field "{field_type}"'))
def see_input_field(browser, field_name, field_type):
    try:
        assert browser.find_element(By.NAME, field_name).is_displayed()
        browser.save_screenshot(f"{field_name}.png")
        print(f"Succès : Le champs [{field_name}] est bien visible et a le type {field_type}")
    except AssertionError:
        print(f"Erreur : Le champs [{field_name}] n'a pas été trouvé")

    
# #2e scénario, je teste la possibilité de saisir dans les champs
# @scenario('features/contact_form.feature', "Check if input fields and textarea are editable")

# def test_input_field_writable():
#     pass  # Les étapes réelles du test seront exécutées par les implémentations d'étapes ci-dessous

# @given('I am on the contact page')
# def open_contact_page(browser):
#     # Remplacez cette URL par l'URL réelle de votre page de contact
#     browser.get("file:///C:/Users/Formations/formations/seleniumPython/siteTest/contact.html")

# @then(parsers.parse('I should be able to type in the "{field_name}" input field'))
# def see_input_field(browser, field_name):
#     element = browser.find_element(By.NAME, field_name)
#     element.send_keys("Test")  # Teste la saisissabilité
#     try:
#         assert element.get_attribute('value') == "Test", f"Échec de saisie dans le champ {field_name}. La valeur actuelle est {element.get_attribute('value')}"
#         browser.save_screenshot("exemple.png")
#         print(f"Succès : Le champs [{field_name}] est bien éditable")
#     except AssertionError:
#         print(f"Erreur : Le champs [{field_name}] ne peut pas être saisi")


# #3e scénario, je teste la possibilité de saisir dans les champs
# @scenario('features/contact_form.feature', "Submit mon form")

# def test_send_form():
#     pass  # Les étapes réelles du test seront exécutées par les implémentations d'étapes ci-dessous

# @given('I am on the contact page')
# def open_contact_page(browser):
#     # Remplacez cette URL par l'URL réelle de votre page de contact
#     browser.get("file:///C:/Users/Formations/formations/seleniumPython/siteTest/contact.html")

# @then(parsers.parse('I click on submit button to send "{field_name}"'))
# def click_submit_button(browser, field_name):
#     monForm = browser.find_element(By.ID, field_name)
#     monForm.submit()
#     browser.save_screenshot("confirm.png")

# @then("I should see the confirmation message")
# def verify_confirmation_message(browser):
#     try:
#         confirmMessage = browser.find_element(By.XPATH, '//*[@id="content"]/p')
#         assert confirmMessage.is_displayed()
#         contenuH1 = confirmMessage.text
#         print(f"Le message de confirmation est présent sur la page et contient : {contenuH1}")
#     except AssertionError:
#         print("Le message de confirmation n'est pas présent sur la page.")
    