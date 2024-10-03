from FrameWork.config_files.frame_work_base_driver import FrameWorkBaseDriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException

class ECPSignUpPage(FrameWorkBaseDriver):
    def __init__(self, driver):
        self.driver = driver

    def get_ecp_sign_up_page(self, element_location):
        fields_ecp_sign_up_page = {
            "txt_login_credentials_user_name": '//input[@name="user.username"]',
            "txt_login_credentials_int_password": '//input[@name="user.password"]',
            "txt_login_credentials_conf_password": '//input[@name="user.cpassword"]',
            "btn_login_credentials_proceed": '//div[@id="credentials"]//div//div//div//div[2]//div//button//span[text()="Next"]',
            "txt_personal_last_name": '//input[@name="personal.lastname"]',
            "txt_personal_first_name": '//input[@name="personal.firstname"]',
            "txt_personal_middle_name": '//input[@name="personal.middlename"]',
            "txt_personal_position": '//input[@name="personal.position"]',
            "txt_personal_contact_number": '//input[@name="personal.cno"]',
            "txt_personal_email": '//input[@name="user.email"]',
            "btn_peronal_information_proceed": '//div[@id="personal-info"]//div//div//div//div[2]//div//button[2]//span[text()="Next"]',
            "pth_upload_id_2_x_2_picture": '//input[@name="image_name"]',
            "pth_upload_id_valid_1": '//input[@name="valid_id"]',
            "pth_upload_id_valid_2": '//input[@name="valid_id2"]',
            "btn_upload_id_proceed": '//div[@id="picture-upload"]//div//div//div//div//div[4]//div//button[2]//span[text()="Next"]',
            "txt_importer_info_name": '//input[@name="company.companyName"]',
            "txt_importer_info_tin": '//input[@name="company.tinNumber"]',
            "txt_importer_info_mobile_no": '//input[@name="company.mobileNo"]',
            "txt_importer_info_land_line": '//input[@name="company.landlineNo"]',
            "txt_importer_info_email_address": '//input[@name="company.emaillAddress"]',
            "slct_importer_info_address_region": '//select[@name="company.address.region_id"]',
            "slct_importer_info_address_province": '//select[@name="company.address.province_id"]',
            "slct_importer_info_address_city": '//select[@name="company.address.city_id"]',
            "slct_importer_info_address_barangay": '//select[@name="company.address.barangay_id"]',
            "txt_importer_info_address_street": '//input[@name="company.streetName"]',
            "btn_import_info_proceed": '//div[@id="company-info"]//div//div//div//div[2]//div//button[2]//span[text()="Next"]',
            "pth_supporting_documents_filen_name_1": '//html//body//div[2]//div//div//div//div[2]//form//div[5]//div//div//div//div[1]//div[2]//div[1]//div//div[1]//input',
            "txt_supporting_documents_description_1": '//html//body//div[2]//div//div//div//div[2]//form//div[5]//div//div//div//div[1]//div[2]//div[1]//div//div[3]//input',
            "btn_supporting_documents_proceed": '//div[@id="user-documents"]//div//div//div//div[2]//div//button[2]//span[text()="Next"]',
            "btn_supporting_documents_add": '//div[@id="user-documents"]//div//div//div//div[1]//div[2]//div[1]//div//div[2]//button[@title="Add more files."]'

        }

        return_ecp_sign_up_page = {
            "txt_login_credentials_user_name": 'sign-up login credentials user name INPUT',
            "txt_login_credentials_int_password": 'sign-up login credentials password INPUT',
            "txt_login_credentials_conf_password": 'sign-up login credentials password confirm INPUT',
            "btn_login_credentials_proceed": 'sign-up login credentials proceed CLICK',
            "txt_personal_last_name": 'personal information last name INPUT',
            "txt_personal_first_name": 'personal information first name INPUT',
            "txt_personal_middle_name": 'personal information middel name INPUT',
            "txt_personal_position": 'personal information position INPUT',
            "txt_personal_contact_number": 'personal information contact number INPUT',
            "txt_personal_email": 'personal information email INPUT',
            "btn_peronal_information_proceed": 'sign-up personal information proceed CLICK',
            "pth_upload_id_2_x_2_picture": 'upload picture and id 2 x 2 INPUT',
            "pth_upload_id_valid_1": 'upload picture and id valid id 1 INPUT',
            "pth_upload_id_valid_2": 'upload picture and id valid id 2 INPUT',
            "btn_upload_id_proceed": 'upload picture and id CLICK',
            "txt_importer_info_name": 'importer information company name INPUT',
            "txt_importer_info_tin": 'importer information company tin INPUT',
            "txt_importer_info_mobile_no": 'importer information mobile number INPUT',
            "txt_importer_info_land_line": 'importer information land line INPUT',
            "txt_importer_info_email_address": 'importer information email address INPUT',
            "slct_importer_info_address_region": 'importer information address region SELECT',
            "slct_importer_info_address_province": 'importer information address province SELECT',
            "slct_importer_info_address_city": 'importer information address city SELECT',
            "slct_importer_info_address_barangay": 'importer information address barangay SELECT',
            "txt_importer_info_address_street": 'importer information address street INPUT',
            "btn_import_info_proceed": 'importer information proceed CLICK',
            'pth_supporting_documents_filen_name_1': '',
            'txt_supporting_documents_description_1': '',
            "btn_supporting_documents_proceed": '',
            "btn_supporting_documents_add": ''
        }
        return fields_ecp_sign_up_page[element_location], return_ecp_sign_up_page[element_location]

    def add_supporting_documents_file_name(self, file_path):
        element_pth_supporting_documents_file_name = '//input[@id="file_name"]'
        return_file_name_add = 'supporting documents file name INPUT'
        execution_status = 0

        try:
            initial_list_file_name = self.locate_all_element_by_x_path(element_pth_supporting_documents_file_name)

            for ii in initial_list_file_name:
                if ii.get_attribute("value") == "":
                    ii.send_keys(file_path)
                    execution_status = 1

            return execution_status, return_file_name_add
        except NoSuchElementException and TimeoutException and ElementNotInteractableException:
            return execution_status, return_file_name_add

    def add_supporting_documents_description(self, file_description):
        element_txt_supporting_documents_description = '//input[@id="description"]'
        return_file_description_add = 'supporting documents file description INPUT'
        execution_status = 0

        try:
            initial_list_description = self.locate_all_element_by_x_path(element_txt_supporting_documents_description)

            for ii in initial_list_description:
                if ii.get_attribute("value") == "":
                    ii.send_keys(file_description)
                    execution_status = 1
            return execution_status, return_file_description_add
        except NoSuchElementException and TimeoutException and ElementNotInteractableException:
            return execution_status, return_file_description_add
