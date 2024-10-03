from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def call(driver,SupportingDocPath):
    try:
        SupDocsFileLoc = driver.find_element(By.XPATH, '//input[@name="file_ecozone_section"]')
        SupDocsFileLoc.send_keys(SupportingDocPath)
        #print("Company Supporting Docs File Location INPUT")
        return 1
    except NoSuchElementException:
        #print("Element Not found! Test Fail")
        return 0
