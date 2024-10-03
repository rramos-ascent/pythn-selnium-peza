from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from FrameWork.config_files.base_driver import BaseDriver

class ProvideServiceProviceType(BaseDriver):
    def __init__(self, driver):
        self.driver = driver

    field_cbox_service_provider_type0 = ''
    field_cbox_service_provider_type1 = ''
    field_cbox_service_provider_type2 = ''
    field_cbox_service_provider_type3 = '//input[@name="company.services" and @id="option3"]'
    field_cbox_service_provider_type4 = '//input[@name="company.services" and @id="option4"]'
    field_cbox_service_provider_type5 = '//input[@name="company.services" and @id="option5"]'
    field_cbox_service_provider_type6 = '//input[@name="company.services" and @id="option6"]'
    field_cbox_service_provider_type7 = '//input[@name="company.services" and @id="option7"]'
    field_cbox_service_provider_type8 = '//input[@name="company.services" and @id="option8"]'
    field_cbox_service_provider_type9 = '//input[@name="company.services" and @id="option9"]'
    field_cbox_service_provider_type10 = '//input[@name="company.services" and @id="option10"]'
    button_proceed_company_information = '//button[@id="btn_app_info"]'

    RETURN_CBOX_SERVICE_PROVIDE = 'Service provider CHECKBOX SELECTED'
    RETRUN_BTN_PROCEED_COMPANY_INFORMATION = 'Proceed to company information BUTTON CLICK'

    def get_service_provider_type(self, text_sp_select):
        match text_sp_select:
            case 'Air Freight Forwarding':
                return self.wait_element_to_be_clickable(By.XPATH, self.field_cbox_service_provider_type0)
            case 'Security Agency':
                return self.wait_element_to_be_clickable(By.XPATH, self.field_cbox_service_provider_type1)
            case 'Sea Freight Forwarding':
                return self.wait_element_to_be_clickable(By.XPATH, self.field_cbox_service_provider_type2)
            case 'Private Express and/or Messengerial Delivery':
                return self.wait_element_to_be_clickable(By.XPATH, self.field_cbox_service_provider_type3)
            case 'Courier Services':
                return self.wait_element_to_be_clickable(By.XPATH, self.field_cbox_service_provider_type4)
            case 'Trucking/Hauling':
                return self.wait_element_to_be_clickable(By.XPATH, self.field_cbox_service_provider_type5)
            case 'Customs Brokerage':
                return self.wait_element_to_be_clickable(By.XPATH, self.field_cbox_service_provider_type6)
            case 'Importer':
                return self.wait_element_to_be_clickable(By.XPATH, self.field_cbox_service_provider_type7)
            case 'Exporter':
                return self.wait_element_to_be_clickable(By.XPATH, self.field_cbox_service_provider_type8)
            case 'Scrap Buyer':
                return self.wait_element_to_be_clickable(By.XPATH, self.field_cbox_service_provider_type9)
            case 'Insurance Company':
                return self.wait_element_to_be_clickable(By.XPATH, self.field_cbox_service_provider_type10)

    def cbox_service_provider_type(self, testdata):
        try:
            selected_service_type = self.get_service_provider_type(testdata)
            self.execute_script_click(selected_service_type)
            return 1, self.RETURN_CBOX_SERVICE_PROVIDE + " " + testdata
        except NoSuchElementException:
            return 0, self.RETURN_CBOX_SERVICE_PROVIDE + " " + testdata

    def btn_proceed_company_information(self):
        try:
            btn_proceed_company_info = self.wait_element_to_be_clickable(By.XPATH, self.button_proceed_company_information)
            self.execute_script_click(btn_proceed_company_info)
            return 1, self.RETRUN_BTN_PROCEED_COMPANY_INFORMATION
        except NoSuchElementException:
            return 0, self.RETURN_CBOX_SERVICE_PROVIDE
