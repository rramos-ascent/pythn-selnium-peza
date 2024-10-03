from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def call(driver, TestData):
    try:
        ContactCompPosition = driver.find_element(By.XPATH, '//input[@id="companyPosition"]')
        ContactCompPosition.send_keys(TestData)
        #print("Contact Position INPUT")
        return 1
    except NoSuchElementException:
        #print("Element Not found! Test Fail")
        return 0