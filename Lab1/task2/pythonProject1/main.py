
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

#Test function to make this task more automatic
def testFunction(login, password):
    login1 = driver.find_element(By.ID, 'user-name')
    password1 = driver.find_element(By.ID, 'password')
    if login != "":
        login1.send_keys(f"{login}")
    else:
        login1.send_keys("")
    if password != "":
        password1.send_keys(f"{password}")
    else:
        password1.send_keys("")
    driver.find_element(By.ID, 'login-button').click()
    error = driver.find_element(By.XPATH, "//h3")

    return error.text



service = Service('chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get('https://www.saucedemo.com/');

time.sleep(5)

assert testFunction("test@wp.pl", "tata") == "Epic sadface: Username and password do not match any user in this service"
time.sleep(5)
driver.refresh()

assert testFunction("dada","") =="Epic sadface: Password is required"

time.sleep(5) # Let the user actually see something!
driver.refresh()

assert testFunction("","dsada") == "Epic sadface: Username is required"
time.sleep(5) # Let the user actually see something!
driver.refresh()
assert testFunction("","") == "Epic sadface: Username is required"
time.sleep(5) # Let the user actually see something!
driver.refresh()
