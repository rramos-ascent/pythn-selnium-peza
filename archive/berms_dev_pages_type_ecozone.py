from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from FrameWork.config_files.base_driver import BaseDriver

class ProvideTypeEcoZone(BaseDriver):
    def __init__(self, driver):
        self.driver = driver

    def get_berms_dev_pages_type_ecozone(self, selected_ecozone_type):

        rbtn_type_ecozon = {
        "MANUFACTURING ECOZONE": '//input[@id="economicZoneId1"]',
        "INFORMATION TECHNOLOGY PARK": '//input[@id="economicZoneId3"]',
        "INFORMATION TECHNOLOGY CENTER": '//input[@id="economicZoneId4"]',
        "TOURISM ECOZONE": '//input[@id="economicZoneId5"]',
        "MEDICAL TOURISM PARK": '//input[@id="economicZoneId6"]',
        "MEDICAL TOURISM CENTER": '//input[@id="economicZoneId7"]',
        "RETIREMENT ECOZONE PARK": '//input[@id="economicZoneId8"]',
        "RETIREMENT ECOZONE CENTER": '//input[@id="economicZoneId9"]'
        }

    def process_berms_dev_pages_type_ecozone(self, element_location):
        try:
            click_process_berms_dev_pages_type_ecozone = self.wait_element_to_be_clickable(By.XPATH, element_location)
            self.execute_script_click(click_process_berms_dev_pages_type_ecozone)
            return 1
        except NoSuchElementException:
            return 0

