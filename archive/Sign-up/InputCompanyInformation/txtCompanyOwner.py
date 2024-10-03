from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def call(driver,AddressStreet):
    try:
        InputCompanyStreet = driver.find_element(By.XPATH, '//input[@id="ownerName"]')
        InputCompanyStreet.send_keys(AddressStreet)
        return 1
    except NoSuchElementException:
        return 0
