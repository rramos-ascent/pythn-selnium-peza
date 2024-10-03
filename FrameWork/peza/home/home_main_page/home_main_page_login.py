from FrameWork.config_files.frame_work_base_driver import FrameWorkBaseDriver


class HomePageLogin(FrameWorkBaseDriver):
    def __init__(self, driver):
        self.driver = driver

    def get_home_main_page_login(self, get_element):
        field_elements_locations = {
            "txt_home_main_page_user_name": '//input[@id="username"]',
            "txt_home_main_page_password": '//input[@id="password"]',
            "btn_home_main_page_proceed_login": '//button[text()="Sign in"]',
            "button_access_sign_up": '//span[text()="  Create an account"]'
        }

        return_element_names = {
            "txt_home_main_page_user_name": 'Provide home page username INPUT',
            "txt_home_main_page_password": 'Provide home page passwsord INPUT',
            "btn_home_main_page_proceed_login": 'Proceed account login',
            "button_access_sign_up": 'Access to sign-up page'
        }

        return field_elements_locations[get_element], return_element_names[get_element]
    #
    # def txt_home_main_page_user_name(self, testdata):
    #     try:
    #         input_txt_home_main_page_user_name = self.locate_element_by(By.XPATH, self.field_txt_home_main_page_user_name)
    #         input_txt_home_main_page_user_name.send_keys(testdata)
    #         return 1, self.RETURN_TXT_HOME_MAIN_PAGE_USER_NAME
    #     except NoSuchElementException:
    #         return 0, self.RETURN_TXT_HOME_MAIN_PAGE_USER_NAME
    #
    # def txt_home_main_page_password(self, testdata):
    #     try:
    #         input_txt_home_main_page_password = self.locate_element_by(By.XPATH, self.field_txt_home_main_page_password)
    #         input_txt_home_main_page_password.send_keys(testdata)
    #         return 1, self.RETURN_TXT_HOME_MAIN_PAGE_PASSWORD
    #     except NoSuchElementException:
    #         return 0, self.RETURN_TXT_HOME_MAIN_PAGE_PASSWORD
    #
    # def btn_home_main_page_proceed_login(self):
    #     try:
    #         button_btn_home_main_page_proceed_login = self.locate_element_by(By.XPATH, self.button_btn_home_main_page_proceed_login)
    #         button_btn_home_main_page_proceed_login.click()
    #         return 1, self.RETURN_BTN_HOME_MAIN_PAGE_PROCEED_LOGIN
    #     except NoSuchElementException:
    #         return 0, self.RETURN_BTN_HOME_MAIN_PAGE_PROCEED_LOGIN




