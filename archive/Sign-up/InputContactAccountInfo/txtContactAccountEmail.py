from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def call(driver, TestData):
    try:
        ContactEMail = driver.find_element(By.XPATH, '//input[@id="email"]')
        ContactEMail.send_keys(TestData)
        #print("Contact EMail INPUT")
        return 1
    except NoSuchElementException:
        #print("Element Not found! Test Fail")
        return 0
