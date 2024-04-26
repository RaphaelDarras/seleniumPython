import pytest
import pytest_bdd
import time
from pytest_bdd import parsers

from selenium  import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pytest_bdd import scenario, given, when, then

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

itemsAmountCart = ''
itemsPricesCart = []

@scenario('./features/tp.feature','Exercise 1')
def test_login_logout(browser):
    pass

#Make this step reusable easily for other users with a variable
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
    #Problem specific to Chrome: if we don't wait a little the button is not clickable
    logout_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'logout_sidebar_link')))
    logout_button.click()

@then('I am back on the login page')
def check_login_page_displayed(browser):
    assert browser.current_url == 'https://www.saucedemo.com/'
    assert not browser.current_url == 'https://www.saucedemo.com/inventory.html'
    assert browser.find_element(By.ID, 'login-button').is_displayed()

@scenario('./features/tp.feature','Exercise 2')
def test_bad_credentials_error(browser):
    pass


@given('I am on the login page')
def access_login_page(browser):
    browser.get('https://www.saucedemo.com/')

#Make this step reusable easily for other users with a variable
@when(parsers.parse('I try to log with the "{user}" credentials'))
def locked_out_user_log(browser,user):
    browser.find_element(By.ID, 'user-name').send_keys(user)
    browser.find_element(By.ID, 'password').send_keys('secret_sauce')
    browser.find_element(By.ID, 'login-button').click()

@then('I see an error message')
def log_error_message(browser):
    error_message = browser.find_element(By.CSS_SELECTOR, 'h3[data-test=error]').text
    assert error_message == 'Epic sadface: Sorry, this user has been locked out.'

@scenario('./features/tp.feature','Exercise 3')
def test_command(browser):
    pass

#Make this step reusable easily for other sorting orders with a variable
@when(parsers.parse('I sort the list in "{sort_order}" order'))
def sort_items(browser,sort_order):
    #Step 2: sorting the list
    sort_orders = Select(browser.find_element(By.CSS_SELECTOR, 'select[data-test=product-sort-container]'))
    sort_orders.select_by_value(sort_order)

#Make this step reusable easily for other items amount with a variable
@when(parsers.parse('I add the first "{amount}" items in the cart'))
def add_two_items(browser, amount):
    global itemsAmountCart, itemsPricesCart
    #Saving the amount coming from the step definition in a global variable to easily reuse it later
    #And keep the reusability of the whole step
    itemsAmountCart = amount
    items=browser.find_elements(By.CLASS_NAME, "btn_inventory")
    itemsPrices=browser.find_elements(By.CSS_SELECTOR, "div[data-test=inventory-item-price]")
    #Step 3: adding the first 2 items to the cart
    #And saving the prices in a global variable to use them in the bonus step
    #This is pure Python, not Selenium. Go ask Google about range an for loops in Python :)
    for x in range(int(amount)):
        items[x].click()
        itemsPricesCart.append(itemsPrices[x].text)
    #Little bonus, making sure the little red bubble on the cart shows the correct number
    assert browser.find_element(By.CSS_SELECTOR, "span[data-test=shopping-cart-badge]").text == amount

@when('I go to the cart')
def go_cart(browser):
    #Step 4: Going to the cart
    browser.find_element(By.CSS_SELECTOR, 'a[data-test=shopping-cart-link]').click()
    assert browser.current_url == 'https://www.saucedemo.com/cart.html'
    assert browser.find_element(By.CSS_SELECTOR, 'div[data-test=cart-list]').is_displayed()
    cartItems = browser.find_elements(By.CLASS_NAME, 'cart_item')
    #Step 5: making sure we have 2 products in the cart
    assert len(cartItems) == int(itemsAmountCart)

@when(parsers.parse('I order as "{firstname}" "{lastname}" habitant au "{zipcode}"'))
def order(browser, firstname, lastname, zipcode):
    #Step 6: Add client informations
    browser.find_element(By.ID, 'checkout').click()
    assert browser.current_url == 'https://www.saucedemo.com/checkout-step-one.html'
    browser.find_element(By.ID, 'first-name').send_keys(firstname)
    browser.find_element(By.ID, 'last-name').send_keys(lastname)
    browser.find_element(By.ID, 'postal-code').send_keys(zipcode)
    browser.find_element(By.ID, 'continue').click()
    assert browser.current_url == 'https://www.saucedemo.com/checkout-step-two.html'


@when('order informations are correct')
def check_order_infos(browser):
    #Step 7: Bonus !
    #Lot of things to ask google here
    #string[1:]
    #float()
    #string.replace('','')
    #round()
    itemsPricesOrder = []
    for x in range(len(itemsPricesCart)):
        itemsPricesOrder.append(itemsPricesCart[x][1:])
        
    itemsTotal = 0
    for x in range(len(itemsPricesOrder)):
        itemsTotal = itemsTotal + float(itemsPricesOrder[x])
    assert itemsTotal == float(browser.find_element(By.CSS_SELECTOR, "div[data-test=subtotal-label]").text.replace('Item total: $', ''))

    roundedTotal = round(itemsTotal)
    #The tax rate was not explained anywhere, I had to discover it myself: it's 8% of the subtotal
    tax = roundedTotal*0.08
    assert tax == float(browser.find_element(By.CSS_SELECTOR, "div[data-test=tax-label]").text.replace('Tax: $', ''))

    total = itemsTotal+tax
    assert round(total, 2) == float(browser.find_element(By.CSS_SELECTOR, "div[data-test=total-label]").text.replace('Total: $', ''))

@when('I finalize the order')
def finalize_order(browser):
    #Step 8
    browser.find_element(By.ID, 'finish').click()
    assert browser.current_url == 'https://www.saucedemo.com/checkout-complete.html'

@then('the order is confirmed')
def confirmed_order(browser):
    #Step 9
    assert browser.find_element(By.CSS_SELECTOR, 'img[data-test=pony-express]').is_displayed()
    assert browser.find_element(By.CSS_SELECTOR, 'h2[data-test=complete-header]').text == 'Thank you for your order!'
    assert browser.find_element(By.CSS_SELECTOR, 'div[data-test=complete-text]').text == 'Your order has been dispatched, and will arrive just as fast as the pony can get there!'