from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

def call(driver,testdata):
    try:
        btn_proceed_com_info = driver.find_element(By.XPATH, '//input[@name="company.registration_type_id" and @value=' + testdata +']')
        driver.execute_script("arguments[0].click();", btn_proceed_com_info)
        #print("Proceed to Company Info")
        return 1
    except NoSuchElementException:
        #print("Element Not found! Test Fail")
        return 0
