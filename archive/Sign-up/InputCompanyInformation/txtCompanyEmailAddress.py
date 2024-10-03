from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def call(driver,EmailAddress):
    try:
        InputCompanyEmail = driver.find_element(By.XPATH, '//input[@id="companyEmailAddress"]')
        InputCompanyEmail.send_keys(EmailAddress)
        #print("Company Email INPUT, " + EmailAddress)
        return 1
    except NoSuchElementException:
        #print("Element Not found! Test Fail")
        return 0
