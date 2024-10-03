from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def call(driver):
    try:
        btnSignupTermsCond = driver.find_element(By.XPATH, '//button[@class="btn btn-primary btn-submit skip-submit-loading skip-text-change"]')
        driver.execute_script("arguments[0].click();", btnSignupTermsCond)
        #print("Terms and Condition info")
        return 1
    except NoSuchElementException:
        #print("Element Not found! Test Fail")
        return 0