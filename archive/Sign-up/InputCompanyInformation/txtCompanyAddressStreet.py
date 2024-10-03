from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def call(driver,AddressStreet):
    try:
        InputCompanyStreet = driver.find_element(By.XPATH, '//input[@id="companyAddressLine1"]')
        InputCompanyStreet.send_keys(AddressStreet)
        #print("Company Street INPUT, " + AddressStreet)
        return 1
    except NoSuchElementException:
        #print("Element Not found! Test Fail")
        return 0
