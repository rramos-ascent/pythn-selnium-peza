from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def call(driver, TestData):
    try:
        ContactMiddleName = driver.find_element(By.XPATH, '//input[@id="middlename"]')
        ContactMiddleName.send_keys(TestData)
        #print("Contact Middlename INPUT")
        return 1
    except NoSuchElementException:
        #print("Element Not found! Test Fail")
        return 0
