from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from FrameWork.config_files.base_driver import BaseDriver

class ProvideContactInformation(BaseDriver):
    def __init__(self, driver):
        self.driver = driver

    field_contact_info_lname = '//input[@id="lastname"]'
    field_contact_info_fname = '//input[@id="firstname"]'
    field_contact_info_mname = '//input[@id="middlename"]'
    field_contact_info_position = '//input[@id="companyPosition"]'
    field_contact_info_mobile_num = '//input[@id="mobileNumber"]'
    field_contact_info_email = '//input[@id="email"]'
    field_contact_info_account_username = '//input[@id="username"]'
    field_contact_info_account_password = '//input[@id="password"]'
    field_contact_info_account_cpassword = '//input[@id="confirmPassword"]'
    button_proceed_application_review = '//button[@id="btn_details_confirm"]'

    RETURN_TXT_CONTACT_INFO_LNAME = 'Contact Information LAST NAME INPUT'
    RETURN_TXT_CONTACT_INFO_FNAME = 'Contact Information FIRST NAME INPUT'
    RETURN_TXT_CONTACT_INFO_MNAME = 'Contact Information MIDDLE NAME INPUT'
    RETURN_TXT_CONTACT_INFO_POSITION = 'Contact Information POSITION INPUT'
    RETURN_TXT_CONTACT_INFO_MOBILE_NUM = 'Contact Information MOBILE NUMBER INPUT'
    RETURN_TXT_CONTACT_INFO_EMAIL = 'Contact Information MOBILE NUMBER INPUT'
    RETURN_TXT_CONTACT_INFO_ACCOUNT_USERNAME = 'Contact Information ACCOUNT USERNAME INPUT'
    RETURN_TXT_CONTACT_INFO_ACCOUNT_PASSWORD = 'Contact Information ACCOUNT PASSWORD INPUT'
    RETURN_TXT_CONTACT_INFO_ACCOUNT_CPASSWORD = 'Contact Information ACCOUNT CONFIRM PASSWORD INPUT'
    RETURN_BTN_CONTACT_INFO_ACCOUNT_CPASSWORD = 'Proceed application and review BUTTON CLICK'
    def txt_contact_info_lname(self, testdata):
        try:
            contact_last_name = self.locate_element_by(By.XPATH, self.field_contact_info_lname)
            contact_last_name.send_keys(testdata)
            return 1, self.RETURN_TXT_CONTACT_INFO_LNAME
        except NoSuchElementException:
            return 0, self.RETURN_TXT_CONTACT_INFO_LNAME

    def txt_contact_info_fname(self, testdata):
        try:
            contact_first_name = self.locate_element_by(By.XPATH, self.field_contact_info_fname)
            contact_first_name.send_keys(testdata)
            return 1, self.RETURN_TXT_CONTACT_INFO_FNAME
        except NoSuchElementException:
            return 0, self.RETURN_TXT_CONTACT_INFO_FNAME

    def txt_contact_info_mname(self, testdata):
        try:
            contact_middle_name = self.locate_element_by(By.XPATH, self.field_contact_info_mname)
            contact_middle_name.send_keys(testdata)
            return 1, self.RETURN_TXT_CONTACT_INFO_MNAME
        except NoSuchElementException:
            return 0, self.RETURN_TXT_CONTACT_INFO_MNAME

    def txt_contact_info_position(self, testdata):
        try:
            contact_position = self.locate_element_by(By.XPATH, self.field_contact_info_position)
            contact_position.send_keys(testdata)
            return 1, self.RETURN_TXT_CONTACT_INFO_POSITION
        except NoSuchElementException:
            return 0, self.RETURN_TXT_CONTACT_INFO_POSITION

    def txt_contact_info_mobile_num(self, testdata):
        try:
            contact_mobile_num = self.locate_element_by(By.XPATH, self.field_contact_info_mobile_num)
            contact_mobile_num.send_keys(testdata)
            return 1, self.RETURN_TXT_CONTACT_INFO_MOBILE_NUM
        except NoSuchElementException:
            return 0, self.RETURN_TXT_CONTACT_INFO_MOBILE_NUM

    def txt_contact_info_email(self, testdata):
        try:
            contact_email = self.locate_element_by(By.XPATH, self.field_contact_info_email)
            contact_email.send_keys(testdata)
            return 1, self.RETURN_TXT_CONTACT_INFO_EMAIL
        except NoSuchElementException:
            return 0, self.RETURN_TXT_CONTACT_INFO_EMAIL

    def txt_contact_info_account_username(self, testdata):
        try:
            contact_account_username = self.locate_element_by(By.XPATH, self.field_contact_info_account_username)
            contact_account_username.send_keys(testdata)
            return 1, self.RETURN_TXT_CONTACT_INFO_ACCOUNT_USERNAME
        except NoSuchElementException:
            return 0, self.RETURN_TXT_CONTACT_INFO_ACCOUNT_USERNAME

    def txt_contact_info_account_password(self, testdata):
        try:
            contact_account_password = self.locate_element_by(By.XPATH, self.field_contact_info_account_password)
            contact_account_password.send_keys(testdata)
            return 1, self.RETURN_TXT_CONTACT_INFO_ACCOUNT_PASSWORD
        except NoSuchElementException:
            return 0, self.RETURN_TXT_CONTACT_INFO_ACCOUNT_PASSWORD

    def txt_contact_info_account_cpassword(self, testdata):
        try:
            contact_account_cpassword = self.locate_element_by(By.XPATH, self.field_contact_info_account_cpassword)
            contact_account_cpassword.send_keys(testdata)
            return 1, self.RETURN_TXT_CONTACT_INFO_ACCOUNT_CPASSWORD
        except NoSuchElementException:
            return 0, self.RETURN_TXT_CONTACT_INFO_ACCOUNT_CPASSWORD

    def btn_proceed_application_review(self):
        try:
            btn_proceed_application_review = self.wait_element_to_be_clickable(By.XPATH, self.button_proceed_application_review)
            self.execute_script_click(btn_proceed_application_review)
            return 1, self.RETURN_BTN_CONTACT_INFO_ACCOUNT_CPASSWORD
        except NoSuchElementException:
            return 0, self.RETURN_BTN_CONTACT_INFO_ACCOUNT_CPASSWORD


