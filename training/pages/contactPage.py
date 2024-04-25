from selenium.webdriver.common.by import By

def findNameInput(browser):
    return browser.find_element(By.NAME, "nom_user")