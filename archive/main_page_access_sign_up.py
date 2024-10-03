from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from FrameWork.config_files.base_driver import BaseDriver
import time


class MainPageAccessSignUp(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    field_access_sign_up = "//span[text()='  Create an account']"

    RETURN_ACCESS_SIGN_UP = "Access to sign-up page"

    def access_sign_up(self):
        try:
            sign_up_button = self.wait_element_to_be_clickable(By.XPATH, self.field_access_sign_up)
            self.execute_script_click(sign_up_button)
            time.sleep(5)
            return 1, self.RETURN_ACCESS_SIGN_UP
        except NoSuchElementException:
            return 0, self.RETURN_ACCESS_SIGN_UP
