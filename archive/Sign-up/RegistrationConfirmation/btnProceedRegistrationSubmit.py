from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
import time


def call(driver):
    try:
        terms_condition_modal: WebElement = driver.find_element(By.XPATH, '//div[@id="termsAndConditionModal"]')
        btn_submit = terms_condition_modal.find_element(By.XPATH, '//button[@id="btnSubmit"]')
        driver.execute_script("arguments[0].click();", btn_submit)
        #print("Terms and Condition Acceptance")
        time.sleep(5)
        try:
            SuccessModal: WebElement = driver.find_element(By.XPATH, '//div[@id="swal2-html-container"]')
            #print("Sign-up Success")
            time.sleep(15)
            return 1
        except NoSuchElementException:
            #print("Sing-up Failed")
            return 0
    except NoSuchElementException:
        #print("Element Not found! Test Fail")
        return 0