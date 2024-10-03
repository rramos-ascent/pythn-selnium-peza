from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

def call(driver,SelectIndex):
    try:
        InputCompanyCity = driver.find_element(By.XPATH, '//select[@id="companyCityId"]')
        Select(InputCompanyCity).select_by_index(SelectIndex)
        #print("Address City INPUT")
        return 1

    except NoSuchElementException:
        #print("Element Not found! Test Fail")
        return 0