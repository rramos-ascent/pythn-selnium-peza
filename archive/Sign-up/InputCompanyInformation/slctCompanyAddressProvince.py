from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

def call(driver,SelectIndex):
    try:
        InputCompanyProvince = driver.find_element(By.XPATH, '//select[@id="companyProvinceId"]')
        Select(InputCompanyProvince).select_by_index(SelectIndex)
        #print("Address Province INPUT")
        return 1

    except NoSuchElementException:
        #print("Element Not found! Test Fail")
        return 0