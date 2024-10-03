from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from FrameWork.config_files.base_driver import BaseDriver


class RegistgrationSelectType(BaseDriver):
    def __init__(self, driver):
        self.driver = driver

    field_type_registration_ent = '//input[@name="company.registration_type_id" and @value=1]'
    field_type_registration_dev = '//input[@name="company.registration_type_id" and @value=2]'
    field_type_registration_ser = '//input[@name="company.registration_type_id" and @value=3]'
    field_proceed_select_type = '//button[@id="btn_comp_info"]'

    RETURN_RBTN_TYPE_REGISTRATION = "Registration type Selection"
    RETURN_BTN_PROCEED_SELECT_TYPE = "Click button Proceed to Company Info"

    def get_type_registration(self, type_registration):
        match type_registration:
            case "ENTERPRISE":
                return self.driver.find_element(By.XPATH, self.field_type_registration_ent)
            case "DEVELOPER":
                return self.driver.find_element(By.XPATH, self.field_type_registration_dev)
            case "SERVICE PROVIDER":
                return self.driver.find_element(By.XPATH, self.field_type_registration_ser)
    def get_proceed_select_type(self):
        return self.driver.find_element(By.XPATH, self.field_proceed_select_type)

    def rbtn_type_registration(self, testdata):
        try:
            select_registration = self.get_type_registration(testdata)
            self.execute_script_click(select_registration)
            return 1, self.RETURN_RBTN_TYPE_REGISTRATION
        except NoSuchElementException:
            return 0, self.RETURN_RBTN_TYPE_REGISTRATION

    def btn_proceed_select_type(self):
        try:
            btn_proceed = self.get_proceed_select_type()
            self.execute_script_click(btn_proceed)
            return 1, self.RETURN_BTN_PROCEED_SELECT_TYPE
        except NoSuchElementException:
            return 0, self.RETURN_BTN_PROCEED_SELECT_TYPE

