import pytest
import pytest_bdd
import time
from pytest_bdd import parsers

import pages.contactPage as contactPage 

from selenium  import webdriver
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
    assert contactPage.findNameInput(browser).is_displayed()
