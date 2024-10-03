from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def call(driver,SupportingDocDesc):
    try:
        SupDocsFileDesc = driver.find_element(By.XPATH, '//input[@id="supportingDocumentDescription"]')
        SupDocsFileDesc.send_keys(SupportingDocDesc)
        #print("Company Supporting Docs description INPUT")
        return 1
    except NoSuchElementException:
        #print("Element Not found! Test Fail")
        return 0