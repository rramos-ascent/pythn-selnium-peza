from FrameWork.config_files.frame_work_base_driver import FrameWorkBaseDriver


class MainMenuPagesBerms(FrameWorkBaseDriver):
    def __init__(self, driver):
        self.driver = driver

    def get_menu_main_pages_berms(self, get_element):
        field_elements_locations = {
            "btn_dev_menu_pages_new_berms": '//span[text()=" Register an Ecozone"]',
            "btn_ent_menu_pages_new_berms": '//span[text()=" New Ecozone Enterprise"]',
            "btn_ent_menu_pages_new_ecai": '//html//body//div[2]//div[1]//div//div//div[1]//div//div//div//div[1]/div//div[2]//a[text()="New Application "]',
            "search_data_table_berms_enterprise_app": '//div[@id="dt_stakeholders_filter"]//label//input',
            "data_table_berms_ent_application_number": '//table[@id="dt_stakeholders"]//tbody//tr//td[2]//a',
            "search_berms_application_data_table": '//div[@id="dt_stakeholders_filter"]//label//input',
            "link_first_data_berms_application_data_table": '//table[@id="dt_stakeholders"]//tbody//tr//td[2]//a'
        }

        return_element_names = {
            "btn_dev_menu_pages_new_berms": 'Proceed to create New Ecozone Developer CLICK',
            "btn_ent_menu_pages_new_berms":  'Proceed to create New Ecozone Enterprise CLICK',
            "btn_ent_menu_pages_new_ecai": 'Proceed to create New ECAI CLICK',
            "search_data_table_berms_enterprise_app": 'Search dat table for BERMS enterprise application',
            "data_table_berms_ent_application_number": 'Open first application in the list',
            "search_berms_application_data_table": 'Search BERMS application',
            "link_first_data_berms_application_data_table": 'Click first item in the berms application data table'
        }

        return field_elements_locations[get_element], return_element_names[get_element]
