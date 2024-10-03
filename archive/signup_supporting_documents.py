from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from FrameWork.config_files.base_driver import BaseDriver
from FrameWork.pkg_utilities.utility_script_general import UtilityPackage

class ProvideSupportingDocuments(BaseDriver):
    def __init__(self, driver):
        self.driver = driver

    field_supporting_doc_path = '//input[@name="file_ecozone_section"]'
    field_supporting_doc_valid = '//html//body//form//div//div//div//div//div//div[2]//div//div//div[2]//div//div[5]//div[2]//div//div[1]//div//div[1]//div[3]//input[2]'
    field_supporting_doc_desc = '//input[@id="supportingDocumentDescription"]'
    button_add_supporting_doc = '//button[@id="btnAddSupportingDocument"]'
    button_proceed_contact_info = '//button[@id="btn_contact_info_ecozone"]'


    RETURN_TXT_SUPPORTING_DOCS_PATH = 'Company Supporting Docs File Location INPUT'
    RETURN_TXT_SUPPORTING_DOCS_VALID = 'Company Supporting Docs File Validity INPUT'
    RETURN_TXT_SUPPORTING_DOCS_DESC = 'Company Supporting Docs File Description INPUT'
    RETURN_BTN_SUPPORTING_DOCS_ADD = 'Company Supporting Docs File ADD CLICK'
    RETURN_BTN_PROCEED_CONTACT_INFO = 'Proceed to contact info Button CLICK'

    def path_supporting_document_file(self, testdata):
        try:
            input_sup_docs_location = self.locate_element_by(By.XPATH, self.field_supporting_doc_path)
            input_sup_docs_location.send_keys(testdata)
            return 1, self.RETURN_TXT_SUPPORTING_DOCS_PATH
        except NoSuchElementException:
            return 0, self.RETURN_TXT_SUPPORTING_DOCS_PATH

    def txt_supporting_document_desc(self, testdata):
        try:
            input_sup_docs_description = self.locate_element_by(By.XPATH, self.field_supporting_doc_desc )
            input_sup_docs_description.send_keys(testdata)
            return 1, self.RETURN_TXT_SUPPORTING_DOCS_DESC
        except NoSuchElementException:
            return 0, self.RETURN_TXT_SUPPORTING_DOCS_DESC

    def txt_supporting_document_valid(self, testdata):
        try:
            input_supporting_doc_valid = self.locate_element_by(By.XPATH, self.field_supporting_doc_valid)
            self.execute_script_click(input_supporting_doc_valid)
            input_supporting_doc_valid.clear()
            date_picker_select = UtilityPackage(self.driver)
            date_picker_select.date_picker_select_date(testdata)
            print(input_supporting_doc_valid.get_property("value"))
            # input_supporting_doc_valid.send_keys(testdata, Keys.TAB)
            return 1, self.RETURN_TXT_SUPPORTING_DOCS_VALID
        except NoSuchElementException:
            return 0, self.RETURN_TXT_SUPPORTING_DOCS_VALID

    def btn_add_supporting_docs(self):
        try:
            btn_add_sup_documents = self.locate_element_by(By.XPATH, self.button_add_supporting_doc)
            self.execute_script_click(btn_add_sup_documents)
            return 1, self.RETURN_BTN_SUPPORTING_DOCS_ADD
        except NoSuchElementException:
            return 0, self.RETURN_BTN_SUPPORTING_DOCS_ADD

    def btn_proceed_contact_info(self):
        try:
            btn_proceed_cont_information = self.wait_element_to_be_clickable(By.XPATH, self.button_proceed_contact_info)
            self.execute_script_click(btn_proceed_cont_information)
            return 1, self.RETURN_BTN_PROCEED_CONTACT_INFO
        except NoSuchElementException:
            return 0, self.RETURN_BTN_PROCEED_CONTACT_INFO