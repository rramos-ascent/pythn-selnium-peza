from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def call(driver):
    try:
        btnProceedContactInfo = driver.find_element(By.XPATH, '//button[@id="btn_contact_info_ecozone"]')
        driver.execute_script("arguments[0].click();", btnProceedContactInfo)
        #print("Proceed contact info")
        return 1
    except NoSuchElementException:
        #print("Element Not found! Test Fail")
        return 0