from FrameWork.config_files.frame_work_base_driver import FrameWorkBaseDriver

class ECPHomePage(FrameWorkBaseDriver):
    def __init__(self, driver):
        self.driver = driver

    def ecp_home_page(self, element_location):
        field_ecp_home_page = {
            "btn_create_account": '//form[@id="frm_login"]//div[3]//a[text()="Create an account"]',
            "txt_user_name": '//input[@id="username"]',
            "txt_password": '//input[@id="password"]',
            "btn_login_proceed": '//form[@id="frm_login"]//div[3]//button[text()="SIGN IN"]'
        }

        RETURN_ECP_HOME_PAGE = {
            "btn_create_account": 'homepage create account CLICK',
            "txt_user_name": '',
            "txt_password": '',
            "btn_login_proceed": ''
        }
        return field_ecp_home_page[element_location], RETURN_ECP_HOME_PAGE[element_location]
