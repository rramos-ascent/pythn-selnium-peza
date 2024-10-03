from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from FrameWork.config_files.base_driver import BaseDriver

class ProvideRepresentativeInfo(BaseDriver):
    def __init__(self, driver):
        self.driver = driver

    field_txt_representative_fname = '//input[@name="representatives[0][firstname]"]'
    field_txt_representative_mname = '//input[@name="representatives[0][middlename]"]'
    field_txt_representative_lname = '//input[@name="representatives[0][lastname]"]'
    field_txt_representative_position = '//input[@name="representatives[0][company_position]"]'
    field_txt_representative_mobile_num = '//input[@name="representatives[0][mobile_number]"]'
    field_txt_representative_email = '//input[@name="representatives[0][email_address]"]'
    button_proceed_supporting_documents = '//button[@id="btn_supp_docs_service_provider"]'


    RETURN_TXT_REPRESENTATIVE_FNAME = 'Representative Information FNAME INPUT'
    RETURN_TXT_REPRESENTATIVE_MNAME = 'Representative Information MNAME INPUT'
    RETURN_TXT_REPRESENTATIVE_LNAME = 'Representative Information LNAME INPUT'
    RETURN_TXT_REPRESENTATIVE_POSITION = 'Representative Information POSITION INPUT'
    RETURN_TXT_REPRESENTATIVE_MOBILE_NUMBER = 'Representative Information MOBILE NUM INPUT'
    RETURN_TXT_REPRESENTATIVE_EMAIL = 'Representative Information EMAIL INPUT'
    RETURN_BTN_PROCEED_SUP_DOCUMENTS = 'Proceed to supporting documents BUTTON CLICK'


    def txt_representative_fname(self, testdata):
        try:
            input_representative_fname = self.locate_element_by(By.XPATH, self.field_txt_representative_fname)
            input_representative_fname.send_keys(testdata)
            return 1, self.RETURN_TXT_REPRESENTATIVE_FNAME
        except NoSuchElementException:
            return 0, self.RETURN_TXT_REPRESENTATIVE_FNAME

    def txt_representative_mname(self, testdata):
        try:
            input_representative_mname = self.locate_element_by(By.XPATH, self.field_txt_representative_mname)
            input_representative_mname.send_keys(testdata)
            return 1, self.RETURN_TXT_REPRESENTATIVE_MNAME
        except NoSuchElementException:
            return 0, self.RETURN_TXT_REPRESENTATIVE_MNAME

    def txt_representative_lname(self, testdata):
        try:
            input_representative_lname = self.locate_element_by(By.XPATH, self.field_txt_representative_lname)
            input_representative_lname.send_keys(testdata)
            return 1, self.RETURN_TXT_REPRESENTATIVE_LNAME
        except NoSuchElementException:
            return 0, self.RETURN_TXT_REPRESENTATIVE_LNAME

    def txt_representative_position(self, testdata):
        try:
            input_representative_position = self.locate_element_by(By.XPATH, self.field_txt_representative_position)
            input_representative_position.send_keys(testdata)
            return 1, self.RETURN_TXT_REPRESENTATIVE_POSITION
        except NoSuchElementException:
            return 0, self.RETURN_TXT_REPRESENTATIVE_POSITION

    def txt_representative_mobile_num(self, testdata):
        try:
            input_representative_mobile_num = self.locate_element_by(By.XPATH, self.field_txt_representative_mobile_num)
            input_representative_mobile_num.send_keys(testdata)
            return 1, self.RETURN_TXT_REPRESENTATIVE_MOBILE_NUMBER
        except NoSuchElementException:
            return 0, self.RETURN_TXT_REPRESENTATIVE_MOBILE_NUMBER

    def txt_representative_email(self, testdata):
        try:
            input_representative_email = self.locate_element_by(By.XPATH, self.field_txt_representative_email)
            input_representative_email.send_keys(testdata)
            return 1, self.RETURN_TXT_REPRESENTATIVE_EMAIL
        except NoSuchElementException:
            return 0, self.RETURN_TXT_REPRESENTATIVE_EMAIL

    def btn_proceed_supporting_documents(self):
        try:
            click_proceed_supporting_docs = self.wait_element_to_be_clickable(By.XPATH, self.button_proceed_supporting_documents)
            self.execute_script_click(click_proceed_supporting_docs)
            return 1, self.RETURN_BTN_PROCEED_SUP_DOCUMENTS
        except NoSuchElementException:
            return 0, self.RETURN_BTN_PROCEED_SUP_DOCUMENTS


