from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def call(driver, TestData):
    try:
        ContactPasswordConfirm = driver.find_element(By.XPATH, '//input[@id="confirmPassword"]')
        ContactPasswordConfirm.send_keys(TestData)
        #print("Contact Password Confirm INPUT")
        return 1
    except NoSuchElementException:
        #print("Element Not found! Test Fail")
        return 0
