import pytest
import pytest_bdd
import time
from pytest_bdd import parsers

from selenium  import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pytest_bdd import scenario, given, when, then

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@scenario('./features/contact_form.feature', "Verify the presence of the input field")
def test_input_field_presence():
    pass

@given('I am on the contact page')
def open_contact_page(browser):
    browser.get("file:///C:/Users/Formations/formations/seleniumPython/siteTest/contact.html")


@then('I should see the "nom" input field "text"')
def see_input_field(browser):
    assert browser.find_element(By.NAME, "nom_user").is_displayed()


@then(parsers.parse('I should see the "{field_name}" input field "{field_type}"'))
def open_contact_page(browser,field_name,field_type):
     assert browser.find_element(By.NAME, field_name).is_displayed()
     assert browser.find_element(By.NAME, field_name).get_attribute('type') == field_type


@scenario('./features/contact_form.feature', "Verify input field is disabled")
def test_input_field_disabled():
    pass

@then('I should see the "nom" is disabled')
def check_input_field_disabled(browser):
    assert not browser.find_element(By.NAME, "nom_user").is_enabled()

@then('I should see the "prenom" is enabled')
def check_input_field_is_enabled(browser):
    assert browser.find_element(By.NAME, "prenom_user").is_enabled()

@scenario('./features/contact_form.feature', "Verify label text")
def test_label_text():
    pass

@then('I should see the "nom" label is equal to "Votre Nom"')
def check_label_text(browser):
    assert browser.find_element(By.CSS_SELECTOR, 'label[for=nom_user]').text == 'Votre nom :'

@scenario('./features/contact_form.feature', "Write in a field")
def test_write_in_field():
    pass

@then('I can write "toto" in the field "message"')
def write_in_field(browser):
    browser.find_element(By.ID,'message').send_keys("toto")
    # time.sleep(10)

@scenario('./features/contact_form.feature', "I can change page")
def test_change_page():
    pass

@given('I am on the index page')
def open_index_page(browser):
    browser.get("file:///C:/Users/Formations/formations/seleniumPython/siteTest/index.html")

@when('I click on the contact link')
def click_contact_link(browser):
    # browser.find_element(By.LINK_TEXT, "Cliquez ici pour nous contacter").click()
    footerLinks = browser.find_elements(By.CSS_SELECTOR, "body > footer > ul > li > a")
    assert len(footerLinks) == 2
    footerLinks[1].click()

@then('I am redirected on the contact page')
def contact_page_displayed(browser):
    assert browser.find_element(By.NAME, "nom_user").is_displayed()

@scenario('./features/contact_form.feature', "Compare values on two pages")
def test_compare_values():
    pass

global valueToCompare
valueToCompare = ''

@given('I am on the index page with a value to compare')
def store_value(browser):
    browser.get("file:///C:/Users/Formations/formations/seleniumPython/siteTest/index.html")
    valueToCompare = browser.find_element(By.TAG_NAME, 'h2').text

@then('the values to compare are equals')
def compare_values(browser):
    secondValue = browser.find_element(By.TAG_NAME, 'h2').text
    assert secondValue == valueToCompare

@scenario('./features/contact_form.feature', "I can select a fruit")
def test_select_fruit():
    pass

@then('I can select mango in the fruits dropdown')
def select_from_dropdown(browser):
    fruitsSelection = Select(browser.find_element(By.ID, 'fruits'))
    fruitsSelection.select_by_value('mango')
    time.sleep(10)