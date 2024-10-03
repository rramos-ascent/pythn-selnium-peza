from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def call(driver, testdata):
    try:
        input_company_name = driver.find_element(By.XPATH, '//input[@id="companyName"]')
        input_company_name.send_keys(testdata)
        #print("Company NAME INPUT: " + CompanyName)
        return 1
    except NoSuchElementException:
        #print("Element Not found! Test Fail")
        return 0