from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def call(driver, TestData):
    try:
        ContactUserName = driver.find_element(By.XPATH, '//input[@id="username"]')
        ContactUserName.send_keys(TestData)
        #print("Contact Username INPUT")
        return 1
    except NoSuchElementException:
        #print("Element Not found! Test Fail")
        return 0
