from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

def call(driver):
    try:
        button = driver.find_element(By.XPATH, '//span[text()="  Create an account"]')
        driver.execute_script("arguments[0].click();", button)
        #print("Sign-up page, Passed!")
        return 1
    except NoSuchElementException:
        #print("Sign-up page, failed!")
        return 0