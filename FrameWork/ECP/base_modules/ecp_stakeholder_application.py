from FrameWork.config_files.frame_work_base_driver import FrameWorkBaseDriver

class ECPStakeHolderApplicationPage(FrameWorkBaseDriver):
    def __init__(self, driver):
        self.driver = driver

    def get_ecp_stakeholder_application_page(self, element_location):

        fields_ecp_stakeholder_application_page = {
            "btn_ecp_application": '//aside[@id="layout-menu"]//ul//li[2]//a//i',
            "slct_declaration_type": '//select[@id="locatorType"]',
            "txt_entry_number_year": '//input[@id="entry_year"]',
            "txt_entry_number_port": '//input[@id="port_code"]',
            "txt_entry_number_serial": '//input[@id="entry_serial"]',
            "txt_entry_number_number": '//input[@id="entry_number"]',
            "txt_registry_number": '//form[@id="form_main_add_item"]//div//div//div//div//div[2]//div[2]//div//div[2]//input',
            "txt_bl_number": '//form[@id="form_main_add_item"]//div//div//div//div//div[2]//div[3]//div//div[2]//input',
            "txt_consignee_representative": '//*[@id="representative"]',
            "txt_representative_designation": '//*[@id="designation"]',
            "txt_representative_contact": '//*[@id="contact"]',
            "txt_consignee_tin": '//input[@id="consigneeTin"]',
            "txt_consignee_name": '//input[@id="importer"]',
            "txt_consignee_number": '//input[@id="consigneeNumber"]',
            "txt_consignee_address": '//input[@id="consignee_address"]',
            "txt_consignee_email": '//input[@id="consignee_email"]',
            "txt_total_gross_weight": '//input[@id="total_gross_weight"]',
            "txt_accredited_mairdoe": '//input[@id="accredited_mairdoe"]',
            "txt_ltms_business_id": '//input[@id="business_id"]',
            "txt_total_net_weight": '//input[@id="total_net_weight"]',
            "slct_transaction_type": '//select[@id="transactionType"]',
            "txt_remarks": '//input[@id="remarks"]',
            "btn_ecp_info_save": '//button[@id="btnSaveMain"]',
            "btn_ecp_modal_info_save_proceed": '//html//body//div[4]//div//div[6]//button[1]',
            "btn_ecp_swal_info_save_confirm": '//html//body//div[4]//div//div[6]//button[1]'

        }
        return_ecp_stakeholder_application_page = {
            "btn_ecp_application": 'menu ecp application CLICK',
            "slct_declaration_type": 'ecp application declaration type SELECT',
            "txt_entry_number_year": 'ecp application entry number year INPUT',
            "txt_entry_number_port": 'ecp application entry number port INPUT',
            "txt_entry_number_serial": 'ecp application entry number serial INPUT',
            "txt_entry_number_number": 'ecp application entry number number INPUT',
            "txt_registry_number": 'ecp application registry number INPUT',
            "txt_bl_number":  'ecp application bl number INPUT',
            "txt_consignee_representative": '',
            "txt_representative_designation": '',
            "txt_representative_contact": '',
            "txt_consignee_tin": '',
            "txt_consignee_name": '',
            "txt_consignee_number": '',
            "txt_consignee_address": '',
            "txt_consignee_email": '',
            "txt_total_gross_weight": '',
            "txt_accredited_mairdoe": '',
            "txt_ltms_business_id": '',
            "txt_total_net_weight": '',
            "slct_transaction_type": '',
            "txt_remarks": '',
            "btn_ecp_info_save": '',
            "btn_ecp_modal_info_save_proceed": '',
            "btn_ecp_swal_info_save_confirm": ''
        }

        return fields_ecp_stakeholder_application_page[element_location], return_ecp_stakeholder_application_page[element_location]

class ECPStakeHolderApplicationItemPage(FrameWorkBaseDriver):
    def __init__(self, driver):
        self.driver = driver

    def get_ecp_stakeholder_application_item_page(self, element_location):

        fields_ecp_stakeholder_application_page = {
            "btn_sup_doc_add": '//button[@id="btnAddDocu"]',
            "txt_sup_doc_general_description": '//textarea[@id="itemGenDesc"]',
            "pth_sup_doc_file_name": '//input[@id="fileName"]',
            "btn_sup_doc_add_proceed": '//button[@id="btnDocumentSubmit" and text()="Save"]',
            "modal_sup_doc_add_proceed_confirmation": '//h2[@id="swal2-title" and text()="Confirmation"]',
            "btn_sup_doc_add_proceed_modal_proceed": '//html//body//div[5]//div//div[6]//button[1][text()="Yes"]',
            "swal_sup_doc_add_proceed_confirmation": '//h2[@id="swal2-title" and text()="Great!"]',
            "btn_sup_doc_add_proceed_swal_proceed": '//html//body//div[5]//div//div[6]//button[1][text()="OK"]',
            "btn_ecp_details_add": '//button[@id="btnShowUploadDataModal" and text()=" UPLOAD EXCEL FILE"]',
            "pth_ecp_details": '//input[@id="file"]',
            "btn_ecp_details_add_proceed": '//button[@id="btnUploadData" and text()="Upload"]',
            "btn_submit_cpr": '//button[@id="btnSubmitCPR"]',
            "btn_ecp_application_modal_proceed": '//html//body//div[4]//div//div[6]//button[1][text()="Yes, submit it!"]',
            "swal_ecp_application_proceed_confirmation": '//h2[@id="swal2-title" and text()="Application tagged as draft"] ',
            "btn_ecp_application_proceed_swal_proceed": '//html//body//div[4]//div//div[6]//button[1][text()="OK"]'
        }
        return fields_ecp_stakeholder_application_page[element_location], ''
        # fields_ecp_stakeholder_application_page[element_location]''

        # '//button[@id="btnShowUploadDataModal"]'
        # '//input[@id="file"]'
        # '//button[@id="btnUploadData" and text()="Upload"]'