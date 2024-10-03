from FrameWork.config_files.frame_work_base_driver import FrameWorkBaseDriver
from FrameWork.ECP.base_modules.ecp_main_page import ECPHomePage
from FrameWork.ECP.base_modules.ecp_sign_up import ECPSignUpPage
from FrameWork.ECP.base_modules.ecp_stakeholder_application import ECPStakeHolderApplicationPage, ECPStakeHolderApplicationItemPage
from FrameWork.pkg_utilities.utility_script_general import UtilityPackage

class ECPExecuteTestCases(FrameWorkBaseDriver):
    def __init__(self, driver):
        self.driver = driver

    manual_test_data = '000220'

    def ecp_function_element_action_click(self, element_location):
        return self.function_element_action_click(element_location)

    def ecp_function_element_action_input(self, element_location, test_data):
        return self.function_element_action_input(element_location, test_data)

    def ecp_function_element_action_select_vt(self, element_location, test_data):
        locate_select_field = self.locate_element_by_x_path(element_location)
        if locate_select_field == 0:
            return 0
        else:
            return self.function_element_action_select_vt(element_location, test_data)

    def ecp_function_element_action_2_modal_confirm(self, confirm_modal, confirm_button):
        return self.function_element_action_2_modal_confirm(confirm_modal, confirm_button)

    def function_call_test_cases(self, test_case_data):
        match test_case_data[0]:
            case 'ecp_home_page_login':
                return self.function_ecp_home_page_login(test_case_data)
            case 'ecp_sign_up_page':
                return self.function_ecp_sign_up_page(test_case_data)
            case 'ecp_stakeholder_application_page':
                return self.function_ecp_stakeholder_application_page(test_case_data)
            case 'ecp_stakeholder_application_item_page':
                return self.function_ecp_stakeholder_application_item_page(test_case_data)
            case 'utility_function':
                return self.utility_function(test_case_data)
            case _:
                return 0, 'No module match'

    def function_ecp_stakeholder_application_item_page(self, test_case_execute):
        element_ecp_stakeholder_application_item_page = ECPStakeHolderApplicationItemPage(self.driver)
        match test_case_execute[1]:
            case 'click_button_supporting_document_add':
                field_element_location = element_ecp_stakeholder_application_item_page.get_ecp_stakeholder_application_item_page("btn_sup_doc_add")
                execution_result = self.ecp_function_element_action_click(field_element_location[0])
                return execution_result, field_element_location[1]
            case 'input_text_supporting_document_general_description':
                field_element_location = element_ecp_stakeholder_application_item_page.get_ecp_stakeholder_application_item_page("txt_sup_doc_general_description")
                execution_result = self.ecp_function_element_action_input(field_element_location[0], test_case_execute[2])
                return execution_result, field_element_location[1]
            case 'input_path_supporting_document_file_name':
                field_element_location = element_ecp_stakeholder_application_item_page.get_ecp_stakeholder_application_item_page("pth_sup_doc_file_name")
                execution_result = self.ecp_function_element_action_input(field_element_location[0], test_case_execute[2])
                return execution_result, field_element_location[1]
            case 'click_button_supporting_document_add_proceed':
                field_element_location = element_ecp_stakeholder_application_item_page.get_ecp_stakeholder_application_item_page("btn_sup_doc_add_proceed")
                execution_result = self.ecp_function_element_action_click(field_element_location[0])
                return execution_result,  field_element_location[1]
            case 'close_button_supporting_documents_add_modal':
                field_element_location_modal = element_ecp_stakeholder_application_item_page.get_ecp_stakeholder_application_item_page("modal_sup_doc_add_proceed_confirmation")
                field_element_location_button = element_ecp_stakeholder_application_item_page.get_ecp_stakeholder_application_item_page("btn_sup_doc_add_proceed_modal_proceed")
                modal_execution_result = self.ecp_function_element_action_2_modal_confirm(field_element_location_modal[0], field_element_location_button[0])
                if modal_execution_result == 1:
                    field_element_location_swal = element_ecp_stakeholder_application_item_page.get_ecp_stakeholder_application_item_page("swal_sup_doc_add_proceed_confirmation")
                    field_element_swal_button = element_ecp_stakeholder_application_item_page.get_ecp_stakeholder_application_item_page("btn_sup_doc_add_proceed_swal_proceed")
                    execution_result = self.ecp_function_element_action_2_modal_confirm(field_element_location_swal[0],field_element_swal_button[0])
                else:
                    execution_result = 0
                return execution_result, ''
            case 'click_button_ecp_details_add':
                field_element_location = element_ecp_stakeholder_application_item_page.get_ecp_stakeholder_application_item_page("btn_ecp_details_add")
                execution_result = self.ecp_function_element_action_click(field_element_location[0])
                return execution_result,  field_element_location[1]
            case 'input_path_ecp_details_file_name':
                field_element_location = element_ecp_stakeholder_application_item_page.get_ecp_stakeholder_application_item_page("pth_ecp_details")
                execution_result = self.ecp_function_element_action_input(field_element_location[0], test_case_execute[2])
                return execution_result, field_element_location[1]
            case 'click_button_ecp_details_add_proceed':
                field_element_location = element_ecp_stakeholder_application_item_page.get_ecp_stakeholder_application_item_page("btn_ecp_details_add_proceed")
                execution_result = self.ecp_function_element_action_click(field_element_location[0])
                return execution_result,  field_element_location[1]
            case 'close_button_ecp_details_add_modal':
                field_element_location_modal = element_ecp_stakeholder_application_item_page.get_ecp_stakeholder_application_item_page("modal_sup_doc_add_proceed_confirmation")
                field_element_location_button = element_ecp_stakeholder_application_item_page.get_ecp_stakeholder_application_item_page("btn_sup_doc_add_proceed_modal_proceed")
                modal_execution_result = self.ecp_function_element_action_2_modal_confirm(field_element_location_modal[0], field_element_location_button[0])
                if modal_execution_result == 1:
                    field_element_location_swal = element_ecp_stakeholder_application_item_page.get_ecp_stakeholder_application_item_page("swal_sup_doc_add_proceed_confirmation")
                    field_element_swal_button = element_ecp_stakeholder_application_item_page.get_ecp_stakeholder_application_item_page("btn_sup_doc_add_proceed_swal_proceed")
                    execution_result = self.ecp_function_element_action_2_modal_confirm(field_element_location_swal[0],field_element_swal_button[0])
                else:
                    execution_result = 0
                return execution_result, ''
            case 'click_button_ecp_application_submit':
                field_element_location = element_ecp_stakeholder_application_item_page.get_ecp_stakeholder_application_item_page("btn_submit_cpr")
                execution_result = self.ecp_function_element_action_click(field_element_location[0])
                return execution_result,  field_element_location[1]
            case 'close_button_ecp_application_modal':
                field_element_location_button = element_ecp_stakeholder_application_item_page.get_ecp_stakeholder_application_item_page("btn_ecp_application_modal_proceed")
                modal_execution_result = self.ecp_function_element_action_click(field_element_location_button[0])
                if modal_execution_result == 1:
                    field_element_location_swal = element_ecp_stakeholder_application_item_page.get_ecp_stakeholder_application_item_page("swal_ecp_application_proceed_confirmation")
                    field_element_swal_button = element_ecp_stakeholder_application_item_page.get_ecp_stakeholder_application_item_page("btn_ecp_application_proceed_swal_proceed")
                    execution_result = self.ecp_function_element_action_2_modal_confirm(field_element_location_swal[0],field_element_swal_button[0])
                else:
                    execution_result = 0
                return execution_result, ''
            case _:
                return 0, 'No module match'

    def function_ecp_stakeholder_application_page(self, test_case_execute):
        element_ecp_stakeholder_application_page = ECPStakeHolderApplicationPage(self.driver)
        match test_case_execute[1]:
            case 'click_button_create_account':
                field_element_location = element_ecp_stakeholder_application_page.get_ecp_stakeholder_application_page("btn_ecp_application")
                execution_result = self.ecp_function_element_action_click(field_element_location[0])
                return execution_result, field_element_location[1]
            case 'select_slct_ecp_declaration_type':
                field_element_location = element_ecp_stakeholder_application_page.get_ecp_stakeholder_application_page("slct_declaration_type")
                execution_result = self.ecp_function_element_action_select_vt(field_element_location[0], test_case_execute[2])
                return execution_result, field_element_location[1]
            case 'input_text_ecp_entry_number_year':
                field_element_location = element_ecp_stakeholder_application_page.get_ecp_stakeholder_application_page("txt_entry_number_year")
                execution_result = self.ecp_function_element_action_input(field_element_location[0], test_case_execute[2])
                return execution_result, field_element_location[1]
            case 'input_text_ecp_entry_number_port':
                field_element_location = element_ecp_stakeholder_application_page.get_ecp_stakeholder_application_page("txt_entry_number_port")
                execution_result = self.ecp_function_element_action_input(field_element_location[0], test_case_execute[2])
                return execution_result, field_element_location[1]
            case 'input_text_ecp_entry_number_serial':
                field_element_location = element_ecp_stakeholder_application_page.get_ecp_stakeholder_application_page("txt_entry_number_serial")
                execution_result = self.ecp_function_element_action_input(field_element_location[0], test_case_execute[2])
                return execution_result, field_element_location[1]
            case 'input_text_ecp_entry_number_number':
                field_element_location = element_ecp_stakeholder_application_page.get_ecp_stakeholder_application_page("txt_entry_number_number")
                execution_result = self.ecp_function_element_action_input(field_element_location[0], self.manual_test_data)
                return execution_result, field_element_location[1]
            case 'input_text_ecp_registry_number':
                field_element_location = element_ecp_stakeholder_application_page.get_ecp_stakeholder_application_page("txt_registry_number")
                execution_result = self.ecp_function_element_action_input(field_element_location[0], test_case_execute[2])
                return execution_result, field_element_location[1]
            case 'input_text_ecp_bl_number':
                field_element_location = element_ecp_stakeholder_application_page.get_ecp_stakeholder_application_page("txt_bl_number")
                execution_result = self.ecp_function_element_action_input(field_element_location[0], test_case_execute[2])
                return execution_result, field_element_location[1]
            case 'input_text_ecp_consignee_rep':
                field_element_location = element_ecp_stakeholder_application_page.get_ecp_stakeholder_application_page("txt_consignee_representative")
                execution_result = self.ecp_function_element_action_input(field_element_location[0], test_case_execute[2])
                return execution_result, field_element_location[1]
            case 'input_text_ecp_consignee_rep_designation':
                field_element_location = element_ecp_stakeholder_application_page.get_ecp_stakeholder_application_page("txt_representative_designation")
                execution_result = self.ecp_function_element_action_input(field_element_location[0], test_case_execute[2])
                return execution_result, field_element_location[1]
            case 'input_text_ecp_consignee_rep_contact':
                field_element_location = element_ecp_stakeholder_application_page.get_ecp_stakeholder_application_page("txt_representative_contact")
                execution_result = self.ecp_function_element_action_input(field_element_location[0], test_case_execute[2])
                return execution_result, field_element_location[1]
            case 'input_text_ecp_consignee_tin':
                field_element_location = element_ecp_stakeholder_application_page.get_ecp_stakeholder_application_page("txt_consignee_tin")
                execution_result = self.ecp_function_element_action_input(field_element_location[0], test_case_execute[2])
                return execution_result, field_element_location[1]
            case 'input_text_ecp_consignee_name':
                field_element_location = element_ecp_stakeholder_application_page.get_ecp_stakeholder_application_page("txt_consignee_name")
                execution_result = self.ecp_function_element_action_input(field_element_location[0], test_case_execute[2])
                return execution_result, field_element_location[1]
            case 'input_text_ecp_consignee_number':
                field_element_location = element_ecp_stakeholder_application_page.get_ecp_stakeholder_application_page("txt_consignee_number")
                execution_result = self.ecp_function_element_action_input(field_element_location[0], test_case_execute[2])
                return execution_result, field_element_location[1]
            case 'input_text_ecp_consignee_address':
                field_element_location = element_ecp_stakeholder_application_page.get_ecp_stakeholder_application_page("txt_consignee_address")
                execution_result = self.ecp_function_element_action_input(field_element_location[0], test_case_execute[2])
                return execution_result, field_element_location[1]
            case 'input_text_ecp_consignee_email':
                field_element_location = element_ecp_stakeholder_application_page.get_ecp_stakeholder_application_page("txt_consignee_email")
                execution_result = self.ecp_function_element_action_input(field_element_location[0], test_case_execute[2])
                return execution_result, field_element_location[1]
            case 'input_text_ecp_total_gross_weight':
                field_element_location = element_ecp_stakeholder_application_page.get_ecp_stakeholder_application_page("txt_total_gross_weight")
                execution_result = self.ecp_function_element_action_input(field_element_location[0], test_case_execute[2])
                return execution_result, field_element_location[1]
            case 'input_text_ecp_accredited_mairdoe':
                field_element_location = element_ecp_stakeholder_application_page.get_ecp_stakeholder_application_page("txt_accredited_mairdoe")
                execution_result = self.ecp_function_element_action_input(field_element_location[0], test_case_execute[2])
                return execution_result, field_element_location[1]
            case 'input_text_ecp_ltms_id':
                field_element_location = element_ecp_stakeholder_application_page.get_ecp_stakeholder_application_page("txt_ltms_business_id")
                execution_result = self.ecp_function_element_action_input(field_element_location[0], test_case_execute[2])
                return execution_result, field_element_location[1]
            case 'input_text_ecp_total_net_weight':
                field_element_location = element_ecp_stakeholder_application_page.get_ecp_stakeholder_application_page("txt_total_net_weight")
                execution_result = self.ecp_function_element_action_input(field_element_location[0], test_case_execute[2])
                return execution_result, field_element_location[1]
            case 'select_slct_ecp_transaction_type':
                field_element_location = element_ecp_stakeholder_application_page.get_ecp_stakeholder_application_page("slct_transaction_type")
                execution_result = self.ecp_function_element_action_select_vt(field_element_location[0], test_case_execute[2])
                return execution_result, field_element_location[1]
            case 'input_text_ecp_remarks':
                field_element_location = element_ecp_stakeholder_application_page.get_ecp_stakeholder_application_page("txt_remarks")
                execution_result = self.ecp_function_element_action_input(field_element_location[0], test_case_execute[2])
                return execution_result, field_element_location[1]
            case 'click_button_ecp_application_save':
                field_element_location = element_ecp_stakeholder_application_page.get_ecp_stakeholder_application_page("btn_ecp_info_save")
                execution_result = self.ecp_function_element_action_click(field_element_location[0])
                return execution_result, field_element_location[1]
            case 'click_button_modal_ecp_application_save':
                field_element_location = element_ecp_stakeholder_application_page.get_ecp_stakeholder_application_page("btn_ecp_modal_info_save_proceed")
                execution_result = self.ecp_function_element_action_click(field_element_location[0])
                return execution_result, field_element_location[1]
            case 'click_button_swal_ecp_application_save_confirm':
                field_element_location = element_ecp_stakeholder_application_page.get_ecp_stakeholder_application_page("btn_ecp_swal_info_save_confirm")
                execution_result = self.ecp_function_element_action_click(field_element_location[0])
                return execution_result, field_element_location[1]
            case _:
                return 0, 'No module match'
    def function_ecp_home_page_login(self, test_case_execute):
        element_ecp_home_page = ECPHomePage(self.driver)
        match test_case_execute[1]:
            case 'click_button_create_account':
                field_element_location = element_ecp_home_page.ecp_home_page("btn_create_account")
                execution_result = self.ecp_function_element_action_click(field_element_location[0])
                return execution_result, field_element_location[1]
            case 'input_text_user_name':
                field_element_location = element_ecp_home_page.ecp_home_page("txt_user_name")
                execution_result = self.ecp_function_element_action_input(field_element_location[0], test_case_execute[2])
                return execution_result, field_element_location[1]
            case 'input_text_password':
                field_element_location = element_ecp_home_page.ecp_home_page("txt_password")
                execution_result = self.ecp_function_element_action_input(field_element_location[0], test_case_execute[2])
                return execution_result, field_element_location[1]
            case 'click_button_login_proceed':
                field_element_location = element_ecp_home_page.ecp_home_page("btn_login_proceed")
                execution_result = self.ecp_function_element_action_click(field_element_location[0])
                return execution_result, field_element_location[1]
            case _:
                return 0, 'No module match'

    def function_ecp_sign_up_page(self, test_case_execute):
        element_ecp_sign_up_page = ECPSignUpPage(self.driver)
        match test_case_execute[1]:
            case 'input_text_login_name':
                field_element_location = element_ecp_sign_up_page.get_ecp_sign_up_page("txt_login_credentials_user_name")
                execution_result = self.ecp_function_element_action_input(field_element_location[0], test_case_execute[2])
                return execution_result, field_element_location[1]
            case 'input_text_initial_password':
                field_element_location = element_ecp_sign_up_page.get_ecp_sign_up_page("txt_login_credentials_int_password")
                execution_result = self.ecp_function_element_action_input(field_element_location[0], test_case_execute[2])
                return execution_result, field_element_location[1]
            case 'input_text_confirm_password':
                field_element_location = element_ecp_sign_up_page.get_ecp_sign_up_page("txt_login_credentials_conf_password")
                execution_result = self.ecp_function_element_action_input(field_element_location[0], test_case_execute[2])
                return execution_result, field_element_location[1]
            case 'click_button_login_credential_next_page':
                field_element_location = element_ecp_sign_up_page.get_ecp_sign_up_page("btn_login_credentials_proceed")
                execution_result = self.ecp_function_element_action_click(field_element_location[0])
                return execution_result, field_element_location[1]
            case 'input_text_personal_information_last_name':
                field_element_location = element_ecp_sign_up_page.get_ecp_sign_up_page("txt_personal_last_name")
                execution_result = self.ecp_function_element_action_input(field_element_location[0], test_case_execute[2])
                return execution_result, field_element_location[1]
            case 'input_text_personal_information_first_name':
                field_element_location = element_ecp_sign_up_page.get_ecp_sign_up_page("txt_personal_first_name")
                execution_result = self.ecp_function_element_action_input(field_element_location[0], test_case_execute[2])
                return execution_result, field_element_location[1]
            case 'input_text_personal_information_middle_name':
                field_element_location = element_ecp_sign_up_page.get_ecp_sign_up_page("txt_personal_middle_name")
                execution_result = self.ecp_function_element_action_input(field_element_location[0], test_case_execute[2])
                return execution_result, field_element_location[1]
            case 'input_text_personal_information_position':
                field_element_location = element_ecp_sign_up_page.get_ecp_sign_up_page("txt_personal_position")
                execution_result = self.ecp_function_element_action_input(field_element_location[0], test_case_execute[2])
                return execution_result, field_element_location[1]
            case 'input_text_personal_information_contact_number':
                field_element_location = element_ecp_sign_up_page.get_ecp_sign_up_page("txt_personal_contact_number")
                execution_result = self.ecp_function_element_action_input(field_element_location[0], test_case_execute[2])
                return execution_result, field_element_location[1]
            case 'input_text_personal_information_email':
                field_element_location = element_ecp_sign_up_page.get_ecp_sign_up_page("txt_personal_email")
                execution_result = self.ecp_function_element_action_input(field_element_location[0], test_case_execute[2])
                return execution_result, field_element_location[1]
            case 'click_button_personal_information_proceed':
                field_element_location = element_ecp_sign_up_page.get_ecp_sign_up_page("btn_peronal_information_proceed")
                execution_result = self.ecp_function_element_action_click(field_element_location[0])
                return execution_result, field_element_location[1]
            case 'input_path_upload_picture_id_2_x_2':
                field_element_location = element_ecp_sign_up_page.get_ecp_sign_up_page("pth_upload_id_2_x_2_picture")
                execution_result = self.ecp_function_element_action_input(field_element_location[0], test_case_execute[2])
                return execution_result, field_element_location[1]
            case 'input_path_upload_picture_id_valid_1':
                field_element_location = element_ecp_sign_up_page.get_ecp_sign_up_page("pth_upload_id_valid_1")
                execution_result = self.ecp_function_element_action_input(field_element_location[0], test_case_execute[2])
                return execution_result, field_element_location[1]
            case 'input_path_upload_picture_id_valid_2':
                field_element_location = element_ecp_sign_up_page.get_ecp_sign_up_page("pth_upload_id_valid_2")
                execution_result = self.ecp_function_element_action_input(field_element_location[0], test_case_execute[2])
                return execution_result, field_element_location[1]
            case 'click_button_upload_picture_id_proceed':
                field_element_location = element_ecp_sign_up_page.get_ecp_sign_up_page("btn_upload_id_proceed")
                execution_result = self.ecp_function_element_action_click(field_element_location[0])
                return execution_result, field_element_location[1]
            case 'input_text_importer_information_name':
                field_element_location = element_ecp_sign_up_page.get_ecp_sign_up_page("txt_importer_info_name")
                execution_result = self.ecp_function_element_action_input(field_element_location[0], test_case_execute[2])
                return execution_result, field_element_location[1]
            case 'input_text_importer_information_tin':
                field_element_location = element_ecp_sign_up_page.get_ecp_sign_up_page("txt_importer_info_tin")
                execution_result = self.ecp_function_element_action_input(field_element_location[0], test_case_execute[2])
                return execution_result, field_element_location[1]
            case 'input_text_importer_information_mobile_no':
                field_element_location = element_ecp_sign_up_page.get_ecp_sign_up_page("txt_importer_info_mobile_no")
                execution_result = self.ecp_function_element_action_input(field_element_location[0], test_case_execute[2])
                return execution_result, field_element_location[1]
            case 'input_text_importer_information_land_line':
                field_element_location = element_ecp_sign_up_page.get_ecp_sign_up_page("txt_importer_info_land_line")
                execution_result = self.ecp_function_element_action_input(field_element_location[0], test_case_execute[2])
                return execution_result, field_element_location[1]
            case 'input_text_importer_information_email':
                field_element_location = element_ecp_sign_up_page.get_ecp_sign_up_page("txt_importer_info_email_address")
                execution_result = self.ecp_function_element_action_input(field_element_location[0], test_case_execute[2])
                return execution_result, field_element_location[1]
            case 'select_slct_importer_informationa_address_region':
                field_element_location = element_ecp_sign_up_page.get_ecp_sign_up_page("slct_importer_info_address_region")
                execution_result = self.ecp_function_element_action_select_vt(field_element_location[0], test_case_execute[2])
                return execution_result, field_element_location[1]
            case 'select_slct_importer_informationa_address_province':
                field_element_location = element_ecp_sign_up_page.get_ecp_sign_up_page("slct_importer_info_address_province")
                execution_result = self.ecp_function_element_action_select_vt(field_element_location[0], test_case_execute[2])
                return execution_result, field_element_location[1]
            case 'select_slct_importer_informationa_address_city':
                field_element_location = element_ecp_sign_up_page.get_ecp_sign_up_page("slct_importer_info_address_city")
                execution_result = self.ecp_function_element_action_select_vt(field_element_location[0], test_case_execute[2])
                return execution_result, field_element_location[1]
            case 'select_slct_importer_informationa_address_barangay':
                field_element_location = element_ecp_sign_up_page.get_ecp_sign_up_page("slct_importer_info_address_barangay")
                execution_result = self.ecp_function_element_action_select_vt(field_element_location[0], test_case_execute[2])
                return execution_result, field_element_location[1]
            case 'input_text_importer_information_address_street':
                field_element_location = element_ecp_sign_up_page.get_ecp_sign_up_page("txt_importer_info_address_street")
                execution_result = self.ecp_function_element_action_input(field_element_location[0], test_case_execute[2])
                return execution_result, field_element_location[1]
            case 'click_button_importer_information_proceed':
                field_element_location = element_ecp_sign_up_page.get_ecp_sign_up_page("btn_import_info_proceed")
                execution_result = self.ecp_function_element_action_click(field_element_location[0])
                return execution_result, field_element_location[1]
            case 'input_path_supporting_documents_file_name_1':
                field_element_location = element_ecp_sign_up_page.get_ecp_sign_up_page("pth_supporting_documents_filen_name_1")
                execution_result = self.ecp_function_element_action_input(field_element_location[0], test_case_execute[2])
                return execution_result, field_element_location[1]
            case 'input_text_supporting_documents_description_1':
                field_element_location = element_ecp_sign_up_page.get_ecp_sign_up_page("txt_supporting_documents_description_1")
                execution_result = self.ecp_function_element_action_input(field_element_location[0], test_case_execute[2])
                return execution_result, field_element_location[1]
            case 'input_path_supporting_documents_file_name_add':
                execution_result = element_ecp_sign_up_page.add_supporting_documents_file_name(test_case_execute[2])
                return execution_result[0], execution_result[1]
            case 'input_text_supporting_documents_description_add':
                execution_result = element_ecp_sign_up_page.add_supporting_documents_description(test_case_execute[2])
                return execution_result[0], execution_result[1]
            case 'click_button_supporting_documents_proceed':
                field_element_location = element_ecp_sign_up_page.get_ecp_sign_up_page("btn_supporting_documents_proceed")
                execution_result = self.ecp_function_element_action_click(field_element_location[0])
                return execution_result, field_element_location[1]
            case 'click_button_supporting_documents_add':
                field_element_location = element_ecp_sign_up_page.get_ecp_sign_up_page("btn_supporting_documents_add")
                execution_result = self.ecp_function_element_action_click(field_element_location[0])
                return execution_result, field_element_location[1]
            case _:
                return 0, 'No module match'

    def utility_function(self, execute_test_case):
        get_utility_function = UtilityPackage()
        match execute_test_case[1]:
            case 'process_time_out_provided_time':
                return get_utility_function.process_time_out_provided_time(execute_test_case[2])
            case _:
                return 0, 'No script match'

