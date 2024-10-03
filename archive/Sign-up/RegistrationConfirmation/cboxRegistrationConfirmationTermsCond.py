from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement


def call(driver):
    try:
        terms_condition_modal: WebElement = driver.find_element(By.XPATH, '//div[@id="termsAndConditionModal"]')
        #print("Terms and Condition info modal")
        try:
            btn_submit = terms_condition_modal.find_element(By.XPATH, '//button[@id="btnSubmit"]')
            btn_status = btn_submit.get_attribute("disabled")
            #print(btn_status)
            if btn_status == "true":
                try:
                    cbox_terms_condition_accept = terms_condition_modal.find_element(By.XPATH, '//input[@id="agreeCheckbox"]')
                    driver.execute_script("arguments[0].click();", cbox_terms_condition_accept)
                    #print("Terms and Condition info modal, acceptance checkbox")
                    return 1
                except NoSuchElementException:
                    #print("Element Not found! Test Fail, 4")
                    return 0
            else:
                #print("Element Not found! Test Fail, 3")
                return 0
        except NoSuchElementException:
            #print("Element Not found! Test Fail, 2")
            return 0
    except NoSuchElementException:
        #print("Element Not found! Test Fail, 1")
        return 0