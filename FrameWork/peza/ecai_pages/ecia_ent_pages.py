from FrameWork.config_files.frame_work_base_driver import FrameWorkBaseDriver

class EcaiEnterpriseElementLocations(FrameWorkBaseDriver):
    def __init__(self, driver):
        self.driver = driver

    def get_ecai_ent_pages(self, get_element):
        field_elements_locations = {
            "option_ecai_type_application": '//select[@id="applicationType"]',
            "option_ecai_zone_application": '//select[@id="zoneId"]',
            "option_ecai_enterprise_type": '//select[@id="enterpriseTypeId"]',
            "option_ecai_industry_type": '//select[@id="industryId"]',
            "path_ecai_file_description": '//input[@id="headerSupportingDocFilename0"]',
            "txt_ecai_file_description": '//input[@id="headerSupportingDocDescription0"]',
            "cbox_ecai_1_registered_activity": '//table[@id="dt_registered_activity"]//tbody//tr//td[2]//input',
            "cbox_ecai_registered_activity": '',
            "button_ecai_add_item": '//button[1]//span[text()="Add Item"]',
            "option_ecai_add_item_modal_nature_of_import": '//select[@id="natureOfImportId"]',
            "txt_ecai_add_item_modal_ahtn_code": '//span[@id="select2-ahtnCodeId-container"]',
            "txt_ecai_add_item_modal_ahtn_search": '//div[@id="modalECAI"]//span//span//span[1]//input',
            "option_ecai_add_item_modal_list_1": '//ul[@id="select2-ahtnCodeId-results"]//li[1]',
            "txtarea_ecai_add_item_modal_item_code": '//textarea[@id="itemsRequested"]',
            "txtarea_ecai_add_item_modal_description": '//textarea[@id="itemDescription"]',
            "path_ecai_add_item_modal_file_name": '//input[@id="supportingDocFilename0"]',
            "txt_ecai_add_item_modal_file_description": '//input[@id="supportingDocDescription0"]',
            "button_ecai_add_item_modal_proceed": '//button[@id="btnSubmit"]',
            "button_ecai_application_proceed": '//button[@id="btnSubmitApplication"]',
            "button_ecai_application_proceed_confirm": '//html//body//div[5]//div//div[6]//button[1]',
            "txt_bank_reference_number": '//span[@id="orderPaymentReferenceNumber"]'
        }

        return_element_names = {
            "option_ecai_type_application": 'Select type of ECAI application',
            "option_ecai_zone_application": 'Select type of zone application',
            "option_ecai_enterprise_type": 'Select type of enterprise type application',
            "option_ecai_industry_type": 'Select type of industry type application',
            "path_ecai_file_description": 'Provide CNLA file',
            "txt_ecai_file_description": 'Input file description application',
            "cbox_ecai_1_registered_activity": 'choose 1st registered activity',
            "cbox_ecai_registered_activity": '',
            "button_ecai_add_item": 'Add item button',
            "option_ecai_add_item_modal_nature_of_import": 'Select ecai item nature of import',
            "txt_ecai_add_item_modal_ahtn_code": 'click ahtn code list',
            "txt_ecai_add_item_modal_ahtn_search": 'search ahtn code',
            "option_ecai_add_item_modal_list_1": 'select second item in the selection',
            "txtarea_ecai_add_item_modal_item_code": '',
            "txtarea_ecai_add_item_modal_description": '',
            "path_ecai_add_item_modal_file_name": '',
            "txt_ecai_add_item_modal_file_description": '',
            "button_ecai_add_item_modal_proceed": '',
            "button_ecai_application_proceed": '',
            "button_ecai_application_proceed_confirm": '',
            "txt_bank_reference_number": ''
        }

        return field_elements_locations[get_element], return_element_names[get_element]

    def get_ecai_ent_pages_others(self, get_element):
        field_cbox_ecai_registered_activity = {
            1: '//table[@id="dt_registered_activity"]//tbody//tr[1]//td[2]//input',
            2: '//table[@id="dt_registered_activity"]//tbody//tr[2]//td[2]//input',
            3: '//table[@id="dt_registered_activity"]//tbody//tr[3]//td[2]//input',
        }

        match get_element:
            case 'cbox_ecai_registered_activity':
                return field_cbox_ecai_registered_activity