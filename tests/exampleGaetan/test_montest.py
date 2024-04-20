from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("file:///C:/Users/Formations/formations/seleniumPython/siteTest/index.html")
input("Appuyez sur une touche pour quitter")

# wait = WebDriverWait(driver,5)




# driver.quit()