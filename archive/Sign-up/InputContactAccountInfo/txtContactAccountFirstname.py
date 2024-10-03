from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def call(driver, TestData):
    try:
        ContactFirstName = driver.find_element(By.XPATH, '//input[@id="firstname"]')
        ContactFirstName.send_keys(TestData)
        #print("Contact Firstname INPUT")
        return 1
    except NoSuchElementException:
        #print("Element Not found! Test Fail")
        return 0