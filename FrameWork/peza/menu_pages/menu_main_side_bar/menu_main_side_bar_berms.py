from FrameWork.config_files.frame_work_base_driver import FrameWorkBaseDriver


class MainMenuNavigationBerms(FrameWorkBaseDriver):
    def __init__(self, driver):
        self.driver = driver

    def get_main_menu_side_bar_berms(self, get_element):
        field_elements_locations = {

            "main_menu_berms_app_and_accre": '//aside[@id="layout-menu"]//ul//li[3]//a//div[text()="Applications & Accreditations"]',
            "main_menu_berms_ecai_application": '//aside[@id="layout-menu"]//ul//li[11]//a//div[text()="Applications & Certificates"]'
        }

        return_element_names = {
            "main_menu_berms_app_and_accre": 'Go to the BERMS Application and Accreditation',
            "main_menu_ecai_application": 'Go to the BERMS Application and Accreditation'
        }

        return field_elements_locations[get_element], return_element_names[get_element]

    def get_main_menu_side_bar_admin(self, get_element):
        field_elements_locations = {
            "main_menu_admin_manage_users": '//div[text()="Manage Users"]',
            "main_menu_admin_manage_users_recent_applications": '//div[text()="Recent Applications"]'
        }

        return_element_names = {
            "main_menu_admin_manage_users": '',
            "main_menu_admin_manage_users_recent_applications": ''
        }

        return field_elements_locations[get_element], return_element_names[get_element]

    def get_top_profile_menu(self, get_element):
        field_elements_locations = {
            "link_user_profile_menu": '//div[@id="navbar-collapse"]//ul//li[5]//a//div//img',
            "button_user_profile_menu_logout": '//div[@id="navbar-collapse"]/ul/li[5]/ul/li[10]/a/span[text()="Log Out"]'
        }

        return_element_names = {
            "link_user_profile_menu": '',
            "button_user_profile_menu_logout": ''
        }

        return field_elements_locations[get_element], return_element_names[get_element]