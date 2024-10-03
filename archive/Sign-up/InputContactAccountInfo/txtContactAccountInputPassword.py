from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def call(driver, TestData):
    try:
        ContactPassword = driver.find_element(By.XPATH, '//input[@id="password"]')
        ContactPassword.send_keys(TestData)
        #print("Contact Password INPUT")
        return 1
    except NoSuchElementException:
        #print("Element Not found! Test Fail")
        return 0
