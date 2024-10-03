from FrameWork.config_files.frame_work_base_driver import FrameWorkBaseDriver


class MainMenuPages(FrameWorkBaseDriver):
    def __init__(self, driver):
        self.driver = driver

    def get_main_menu_pages(self, get_element):
        field_elements_locations = {
            "btn_ent_menu_pages_new_ecai": '//html//body//div[2]//div[1]//div//div//div[1]//div//div//div//div[1]/div//div[2]//a',
            "btn_ent_menu_pages_new_ip": '//a[@id="btnAdd"]'
        }

        return_element_names = {
            "btn_ent_menu_pages_new_ecai": 'Proceed to create New ECAI CLICK',
            "btn_ent_menu_pages_new_ip": 'Proceed to create New Import Permit CLICK'
        }
        return field_elements_locations[get_element], return_element_names[get_element]
