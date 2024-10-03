from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

def call(driver, TestURL):
    try:
        driver.get(TestURL)
        driver.maximize_window()
        #print("Test Passed: Website initiated")
        return 1
    except NoSuchElementException:
        #print("Cannot not open website: Test Fail")
        return 0
