from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def call(driver,SupportingDocValidity):
    try:
        SupDocsValidity = driver.find_element(By.XPATH, '//input[@id="supportingDocumentValidity"]')
        driver.execute_script("arguments[0].value =" + SupportingDocValidity + ";", SupDocsValidity)
        #print("Company Supporting Docs validity INPUT ", SupDocsValidity.get_property("value"))
        return 1
    except NoSuchElementException:
        #print("Element Not found! Test Fail")
        return 0
