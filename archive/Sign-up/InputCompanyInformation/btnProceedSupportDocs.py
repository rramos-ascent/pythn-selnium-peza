from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def call(driver):
    try:
        ProceedSupportingDocs = driver.find_element(By.XPATH, '//button[@id="btn_supp_docs_ecozone"]')
        driver.execute_script("arguments[0].click();", ProceedSupportingDocs)
        #print("Proceed to Supporting Documents")
        return 1
    except NoSuchElementException:
        #print("Element Not found! Test Fail")
        return 0
