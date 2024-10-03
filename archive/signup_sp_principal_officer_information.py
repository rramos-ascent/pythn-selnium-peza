from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from FrameWork.config_files.base_driver import BaseDriver

class ProvidePrincipalOfficerInfo(BaseDriver):
    def __init__(self, driver):
        self.driver = driver

    field_txt_principal_officer_fname = '//input[@id="principalOfficersFirstName"]'
    field_txt_principal_officer_mname = '//input[@id="principalOfficersMiddleName"]'
    field_txt_principal_officer_lname = '//input[@id="principalOfficersLastName"]'
    field_txt_principal_officer_position = '//input[@id="principalOfficersPosition0"]'
    field_txt_principal_officer_mobile_num = '//input[@id="principalOfficersMobileNumber"]'
    field_txt_principal_officer_email = '//input[@id="principalOfficersEmailAddress"]'
    # button_btn_proceed_to_contact_information = '//button[@id="btn_contact_info_service_provider"]//i'
    button_btn_proceed_to_contact_information = '//html//body//form//div//div//div//div//div//div[2]//div//div[1]//div[4]//div//div//div[12]//div'

    RETURN_TXT_PRINCIPAL_OFFICER_FNAME = 'Principal officer first name INPUT'
    RETURN_TXT_PRINCIPAL_OFFICER_MNAME = 'Principal officer middle name INPUT'
    RETURN_TXT_PRINCIPAL_OFFICER_LNAME = 'Principal officer last name INPUT'
    RETURN_TXT_PRINCIPAL_OFFICER_POSITION = 'Principal officer position INPUT'
    RETURN_TXT_PRINCIPAL_OFFICER_MOBILE_NUM = 'Principal officer mobil number INPUT'
    RETURN_TXT_PRINCIPAL_OFFICER_EMAIL = 'Principal officer email INPUT'
    RETURN_BTN_PROCEED_TO_CONTACT_INFORMATION = 'Proceed to contact information BUTTON CLICK'

    def txt_principal_officer_fname(self, testdata):
        try:
            input_txt_principal_officer_fname = self.locate_element_by(By.XPATH, self.field_txt_principal_officer_fname)
            input_txt_principal_officer_fname.send_keys(testdata)
            return 1, self.RETURN_TXT_PRINCIPAL_OFFICER_FNAME
        except NoSuchElementException:
            return 0, self.RETURN_TXT_PRINCIPAL_OFFICER_FNAME

    def txt_principal_officer_mname(self, testdata):
        try:
            input_txt_principal_officer_mname = self.locate_element_by(By.XPATH, self.field_txt_principal_officer_mname)
            input_txt_principal_officer_mname.send_keys(testdata)
            return 1, self.RETURN_TXT_PRINCIPAL_OFFICER_MNAME
        except NoSuchElementException:
            return 0, self.RETURN_TXT_PRINCIPAL_OFFICER_MNAME

    def txt_principal_officer_lname(self, testdata):
        try:
            input_txt_principal_officer_lname = self.locate_element_by(By.XPATH, self.field_txt_principal_officer_lname)
            input_txt_principal_officer_lname.send_keys(testdata)
            return 1, self.RETURN_TXT_PRINCIPAL_OFFICER_LNAME
        except NoSuchElementException:
            return 0, self.RETURN_TXT_PRINCIPAL_OFFICER_LNAME

    def txt_principal_officer_position(self, testdata):
        try:
            input_txt_principal_officer_position = self.locate_element_by(By.XPATH, self.field_txt_principal_officer_position)
            input_txt_principal_officer_position.send_keys(testdata)
            return 1, self.RETURN_TXT_PRINCIPAL_OFFICER_POSITION
        except NoSuchElementException:
            return 0, self.RETURN_TXT_PRINCIPAL_OFFICER_POSITION

    def txt_principal_officer_mobile_num(self, testdata):
        try:
            input_txt_principal_officer_mobile_num = self.locate_element_by(By.XPATH, self.field_txt_principal_officer_mobile_num)
            input_txt_principal_officer_mobile_num.send_keys(testdata)
            return 1, self.RETURN_TXT_PRINCIPAL_OFFICER_MOBILE_NUM
        except NoSuchElementException:
            return 0, self.RETURN_TXT_PRINCIPAL_OFFICER_MOBILE_NUM

    def txt_principal_officer_email(self, testdata):
        try:
            input_txt_principal_officer_email = self.locate_element_by(By.XPATH, self.field_txt_principal_officer_email)
            input_txt_principal_officer_email.send_keys(testdata)
            return 1, self.RETURN_TXT_PRINCIPAL_OFFICER_EMAIL
        except NoSuchElementException:
            return 0, self.RETURN_TXT_PRINCIPAL_OFFICER_EMAIL

    def btn_proceed_to_contact_information(self):
        try:
            click_btn_proceed_to_contact_information = self.wait_element_to_be_clickable(By.XPATH, self.button_btn_proceed_to_contact_information)
            self.execute_script_click(click_btn_proceed_to_contact_information)
            return 1, self.RETURN_BTN_PROCEED_TO_CONTACT_INFORMATION
        except NoSuchElementException:
            return 0, self.RETURN_BTN_PROCEED_TO_CONTACT_INFORMATION











