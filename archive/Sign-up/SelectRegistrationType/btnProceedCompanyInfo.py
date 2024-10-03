from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

def call(driver):
    try:
        proceed_company_info = driver.find_element(By.XPATH, '//button[@id="btn_comp_info"]')
        driver.execute_script("arguments[0].click();", proceed_company_info)
        #print("Test Passed: Click button Proceed to Company Info")
        return 1
    except NoSuchElementException:
        print("Element Not found! Test Fail")
        return 0