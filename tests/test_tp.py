import pytest
import pytest_bdd
import time
from pytest_bdd import parsers

from selenium  import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pytest_bdd import scenario, given, when, then

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@scenario('./features/tp.feature','Exercise 1')
def test_login_logout(browser):
    pass

@given(parsers.parse('I am logged as "{user}"'))
def standard_user_login(browser,user):
    browser.get('https://www.saucedemo.com/')
    browser.find_element(By.ID, 'user-name').send_keys(user)
    browser.find_element(By.ID, 'password').send_keys('secret_sauce')
    browser.find_element(By.ID, 'login-button').click()
    assert browser.current_url == 'https://www.saucedemo.com/inventory.html'
    assert browser.find_element(By.ID, 'inventory_container').is_displayed()

@when('I logout')
def logout(browser):
    browser.find_element(By.ID, 'react-burger-menu-btn').click()
    logout_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'logout_sidebar_link')))
    logout_button.click()

@then('I am back on the login page')
def check_login_page_displayed(browser):
    assert browser.current_url == 'https://www.saucedemo.com/'
    assert not browser.current_url == 'https://www.saucedemo.com/inventory.html'
    assert browser.find_element(By.ID, 'login-button').is_displayed()
