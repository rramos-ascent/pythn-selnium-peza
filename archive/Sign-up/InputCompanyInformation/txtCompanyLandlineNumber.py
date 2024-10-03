from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def call(driver,LandlineNum):
    try:
        InputCompanyTelNum = driver.find_element(By.XPATH, '//input[@id="companyTelephoneNumber"]')
        InputCompanyTelNum.send_keys(LandlineNum)
        #print("Company Telphone Number INPUT, " + LandlineNum)
        return 1
    except NoSuchElementException:
        #print("Element Not found! Test Fail")
        return 0
