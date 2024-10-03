from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

def call(driver,SelectIndex):
    try:
        InputCompanyBarangay = driver.find_element(By.XPATH, '//select[@id="companyBarangayId"]')
        Select(InputCompanyBarangay).select_by_index(SelectIndex)
        #print("Address Barangay INPUT")
        return 1

    except NoSuchElementException:
        #print("Element Not found! Test Fail")
        return 0
