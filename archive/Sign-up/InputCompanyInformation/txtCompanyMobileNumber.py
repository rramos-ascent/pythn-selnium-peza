from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def call(driver,MobileNum):
    try:
        InputCompanyMobileNum = driver.find_element(By.XPATH, '//input[@id="companyMobileNumber"]')
        InputCompanyMobileNum.send_keys(MobileNum)
        #print("Company Mobile Number, " + MobileNum)
        return 1
    except NoSuchElementException:
        #print("Element Not found! Test Fail")
        return 0
