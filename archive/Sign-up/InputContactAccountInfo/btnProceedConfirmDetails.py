from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def call(driver):
    try:
        btnPrcdDetailsConfirm = driver.find_element(By.XPATH, '//button[@id="btn_details_confirm"]')
        driver.execute_script("arguments[0].click();", btnPrcdDetailsConfirm)
        #print("Proceed details confirmation")
        return 1
    except NoSuchElementException:
        #print("Element Not found! Test Fail")
        return 0