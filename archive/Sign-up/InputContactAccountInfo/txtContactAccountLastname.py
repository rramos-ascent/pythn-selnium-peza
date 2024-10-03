from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def call(driver, TestData):
    try:
        ContactLastName = driver.find_element(By.XPATH, '//input[@id="lastname"]')
        ContactLastName.send_keys(TestData)
        #print("Contact Lastname INPUT")
        return 1
    except NoSuchElementException:
        #print("Element Not found! Test Fail")
        return 0