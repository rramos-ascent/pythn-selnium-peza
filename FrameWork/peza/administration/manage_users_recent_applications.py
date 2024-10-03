from FrameWork.config_files.frame_work_base_driver import FrameWorkBaseDriver

class AdminManageUsersRecentApps(FrameWorkBaseDriver):
    def __init__(self, driver):
        self.driver = driver

    def get_admin_manage_users_recent_apps(self, get_element):
        field_elements_locations = {
            "txt_dt_search_sign_up_application": '//div[@id="dt_usermaintenance_filter"]//label//input',
            "link_dt_open_first_record": '//table[@id="dt_usermaintenance"]//tbody//tr//td[2]//a//div',
            "option_sign_up_application_status": '//select[@id="authStatus"]',
            "button_sign_up_application_status_proceed": '//button[@id="btnSubmit"]',
            "button_modal_sign_up_status_confirmation": '//html//body//div[3]//div//div[6]//button[1][text()="Yes"]'
        }

        return_element_names = {
            "txt_dt_search_sign_up_application": '',
            "link_dt_open_first_record": '',
            "option_sign_up_application_status": '',
            "button_sign_up_application_status_proceed": '',
            "button_modal_sign_up_status_confirmation": ''
        }

        return field_elements_locations[get_element], return_element_names[get_element]