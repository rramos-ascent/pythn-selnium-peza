from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from FrameWork.config_files.base_driver import BaseDriver


# class ProvideCompanyInformation(BaseDriver):
#     def __init__(self, driver):
#         self.driver = driver
#
#     field_company_tin = '//input[@id="companyTinNumber"]'
#     field_company_name = '//input[@id="companyName"]'
#     field_company_address_region = '//select[@id="companyRegionId"]'
#     field_company_address_province = '//select[@id="companyProvinceId"]'
#     field_company_address_city = '//select[@id="companyCityId"]'
#     field_company_address_barangay = '//select[@id="companyBarangayId"]'
#     field_company_address_street = '//input[@id="companyAddressLine1"]'
#     field_company_contact_mobile_num = '//input[@id="companyMobileNumber"]'
#     field_company_contact_landline = '//input[@id="companyTelephoneNumber"]'
#     field_company_contact_email = '//input[@id="companyEmailAddress"]'
#
#     button_proceed_details_confirm = '//button[@id=""btn_details_confirm_Id]'
#     # Affected by decomissioned functions
#     button_proceed_support_docs = '//button[@id="btn_supp_docs_ecozone"]'
#     button_proceed_rep_information = '//button[@id="btn_rep_info"]'
#
#
#     RETURN_TXT_COMPANY_TIN = "Company TIN INPUT"
#     RETURN_TXT_COMPANY_NAME = "Company NAME INPUT"
#     RETURN_SLCT_ADDRESS_REGION = "Company ADDRESS REGION SELECT"
#     RETURN_SLCT_ADDRESS_PROVINCE = "Company ADDRESS PROVINCE SELECT"
#     RETURN_SLCT_ADDRESS_CITY = "Company ADDRESS CITY SELECT"
#     RETURN_SLCT_ADDRESS_BARANGAY = "Company ADDRESS BARANGAY SELECT"
#     RETURN_TXT_ADDRESS_STREET = "Company ADDRESS STREET SELECT"
#     RETURN_TXT_CONTACT_MOBILE_NUM = "Company CONTACT MOBILE NUMBER INPUT"
#     RETURN_TXT_CONTACT_LANDLINE = "Company CONTACT LANDLINE INPUT"
#     RETURN_TXT_CONTACT_EMAIL = "Company CONTACT EMAIL INPUT"
#     RETURN_BTN_PROCEED_DETAILS_CONFIRM = "Proceed to details confirmation button CLICK"
#     # Affected by decomissioned functions
#     RETURN_BTN_PRCD_SUP_DOCS = "Proceed to supporting documents button CLICK"
#     RETURN_BTN_PRCD_REP_INFO = "Proceed to supporting documents button CLICK"
#
#     def txt_company_tin(self, testdata):
#         try:
#             input_company_tin = self.locate_element_by(By.XPATH, self.field_company_tin)
#             input_company_tin.send_keys(testdata)
#             return 1, self.RETURN_TXT_COMPANY_TIN
#         except NoSuchElementException:
#             return 0, self.RETURN_TXT_COMPANY_TIN
#
#     def txt_company_name(self, testdata):
#         try:
#             input_company_name = self.locate_element_by(By.XPATH, self.field_company_name)
#             input_company_name.send_keys(testdata)
#             return 1, self.RETURN_TXT_COMPANY_NAME
#         except NoSuchElementException:
#             return 0, self.RETURN_TXT_COMPANY_NAME
#
#     def slct_address_region(self, select_option):
#         try:
#             input_company_region = self.locate_element_by(By.XPATH, self.field_company_address_region)
#             self.select_dropdown_by_visible_text(input_company_region, select_option)
#             return 1, self.RETURN_SLCT_ADDRESS_REGION
#         except NoSuchElementException:
#             return 0, self.RETURN_SLCT_ADDRESS_REGION
#
#     def slct_address_province(self, select_option):
#         try:
#             input_company_province = self.locate_element_by(By.XPATH, self.field_company_address_province)
#             self.select_dropdown_by_visible_text(input_company_province, select_option)
#             return 1, self.RETURN_SLCT_ADDRESS_PROVINCE
#         except NoSuchElementException:
#             return 0, self.RETURN_SLCT_ADDRESS_PROVINCE
#
#     def slct_address_city(self, select_option):
#         try:
#             input_company_city = self.locate_element_by(By.XPATH, self.field_company_address_city)
#             self.select_dropdown_by_visible_text(input_company_city, select_option)
#             return 1, self.RETURN_SLCT_ADDRESS_CITY
#         except NoSuchElementException:
#             return 0, self.RETURN_SLCT_ADDRESS_CITY
#
#     def slct_address_barangay(self,select_option):
#         try:
#             input_company_barangay = self.locate_element_by(By.XPATH, self.field_company_address_barangay)
#             self.select_dropdown_by_visible_text(input_company_barangay, select_option)
#             return 1, self.RETURN_SLCT_ADDRESS_BARANGAY
#         except NoSuchElementException:
#             return 0, self.RETURN_SLCT_ADDRESS_BARANGAY
#
#     def txt_address_street(self, testdata):
#         try:
#             input_company_street = self.locate_element_by(By.XPATH, self.field_company_address_street)
#             input_company_street.send_keys(testdata)
#             return 1, self.RETURN_TXT_ADDRESS_STREET
#         except NoSuchElementException:
#             return 0, self.RETURN_TXT_ADDRESS_STREET
#
#     def txt_contact_mobile_num(self, testdata):
#         try:
#             input_mobile_num = self.locate_element_by(By.XPATH, self.field_company_contact_mobile_num)
#             input_mobile_num.send_keys(testdata)
#             return 1, self.RETURN_TXT_CONTACT_MOBILE_NUM
#         except NoSuchElementException:
#             return 0, self.RETURN_TXT_CONTACT_MOBILE_NUM
#
#     def txt_contact_landline(self, testdata):
#         try:
#             input_land_line = self.locate_element_by(By.XPATH, self.field_company_contact_landline)
#             input_land_line.send_keys(testdata)
#             return 1, self.RETURN_TXT_CONTACT_LANDLINE
#         except NoSuchElementException:
#             return 0, self.RETURN_TXT_CONTACT_LANDLINE
#
#     def txt_contact_email(self, testdata):
#         try:
#             input_email = self.locate_element_by(By.XPATH, self.field_company_contact_email)
#             input_email.send_keys(testdata)
#             return 1, self.RETURN_TXT_CONTACT_EMAIL
#         except NoSuchElementException:
#             return 0, self.RETURN_TXT_CONTACT_EMAIL
#
#     # Decomissioned fucntions
#     def btn_proceed_supporting_document(self):
#         try:
#             btn_proceed_supporting_docs = self.wait_element_to_be_clickable(By.XPATH, self.button_proceed_support_docs)
#             self.execute_script_click(btn_proceed_supporting_docs)
#             return 1, self.RETURN_BTN_PRCD_SUP_DOCS
#         except NoSuchElementException:
#             return 0, self.RETURN_BTN_PRCD_SUP_DOCS
#
#     def btn_proceed_representative_information(self):
#         try:
#             btn_proceed_representative_info = self.wait_element_to_be_clickable(By.XPATH, self.button_proceed_rep_information)
#             self.execute_script_click(btn_proceed_representative_info)
#             return 1, self.RETURN_BTN_PRCD_REP_INFO
#         except NoSuchElementException:
#             return 0, self.RETURN_BTN_PRCD_REP_INFO


# class ProvideCompanyInformationSupDocs(BaseDriver):
#     def __init__(self, driver):
#         self.driver = driver
#
#     field_pth_supporting_document_file = '//input[@name="file_ecozone_section"]'
#     field_txt_supporting_document_desc = '//input[@name="description_ecozone_section"]'
#     field_txt_supporting_document_validity = '//html//body//form//div//div//div//div//div//div[2]//div//div[1]//div[4]//div//div//div[8]//div[2]//div[1]//div[3]//input[2]'
#     field_txt_supporting_document_validity_loc = ('//html//body//div[3]//div[1]//div//div//div//input', '//html//body//div[3]//div[1]//div//div//select', '//html//body//div[3]//div[2]//div//div[2]//div//span[@class="flatpickr-day" and text()="')
#     button_btn_supporting_document_add = '//button[@id="btnAddSupportingDocument"]'
#     field_pth_bir_form_2303 = '//input[@id="birForm2303Filename0"]'
#     field_date_bir_form_2303_validity = '//html//body//form//div//div//div//div//div//div[2]//div//div[1]//div[4]//div//div//div[9]//div[2]//div[1]//div//div//div[3]//input[2]'
#     field_pth_sec_certificate = '//input[@id="secCertificateFilename0"]'
#     field_date_sec_certificate_validity = '//html//body//form//div//div//div//div//div//div[2]//div//div[1]//div[4]//div//div//div[9]//div[2]//div[2]//div//div//div[3]//input[2]'
#     field_pth_dti_certificate_accreditations = '//input[@id="dtiCertificateAccreditationFilename0"]'
#     field_date_dti_certificate_accreditations_validity = '//html//body//form//div//div//div//div//div//div[2]//div//div[1]//div[4]//div//div//div[9]//div[2]//div[7]//div//div//div[3]//input[2]'
#
#     RETURN_PTH_SUPPORTING_DOCUMENT_FILE = 'Provide supporting documents FILE INPUT'
#     RETURN_TXT_SUPPORTING_DOCUMENT_DESC = 'Provide supporting documents description INPUT'
#     RETURN_TXT_SUPPORTING_DOCUMENT_VALIDITY = 'Provide supporting documents validity INPUT'
#     RETURN_BTN_SUPPORTING_DOCUMENT_ADD = 'Add supporting documents button CLICK'
#     RETURN_PTH_BIR_FORM_2303 = 'Provide company information supporting documents path INPUT'
#     RETURN_DATE_BIR_FORM_2303_VALIDITY = 'Provide company information supporting documents validity INPUT'
#     RETURN_PTH_SEC_CERTIFICATE = 'Provide company information sec certificate path INPUT'
#     RETURN_DATE_SEC_CERTIFICATE_VALIDITY = 'Provide company information sec certificate validity INPUT'
#     RETURN_PTH_DTI_CERTIFICATE_ACCREDITATIONS = 'Provide company information DTI certification and accreditation path INPUT'
#     RETURN_DATE_DTI_CERTIFICATE_ACCREDITATIONS_VALIDITY = 'Provide company information DTI certification and accreditation validity INPUT'
#     def pth_supporting_document_file(self, testdata):
#         try:
#             input_pth_supporting_document_file = self.wait_precense_of_element_located(By.XPATH, self.field_pth_supporting_document_file)
#             input_pth_supporting_document_file.send_keys(testdata)
#             return 1, self.RETURN_PTH_SUPPORTING_DOCUMENT_FILE
#         except NoSuchElementException:
#             return 0, self.RETURN_PTH_SUPPORTING_DOCUMENT_FILE
#
#     def txt_supporting_document_desc(self, testdata):
#         try:
#             input_field_txt_supporting_document_desc = self.wait_precense_of_element_located(By.XPATH, self.field_txt_supporting_document_desc)
#             input_field_txt_supporting_document_desc.send_keys(testdata)
#             return 1, self.RETURN_TXT_SUPPORTING_DOCUMENT_DESC
#         except NoSuchElementException:
#             return 0, self.RETURN_TXT_SUPPORTING_DOCUMENT_DESC
#
#     def txt_supporting_document_validity(self, testdata):
#         try:
#             input_txt_supporting_document_validity = self.wait_precense_of_element_located(By.XPATH, self.field_txt_supporting_document_validity)
#             self.input_data_in_date_field(input_txt_supporting_document_validity, testdata)
#             return 1, self.RETURN_TXT_SUPPORTING_DOCUMENT_VALIDITY
#         except NoSuchElementException:
#             return 0, self.RETURN_TXT_SUPPORTING_DOCUMENT_VALIDITY
#
#     def btn_supporting_document_add(self):
#         try:
#             click_btn_supporting_document_add = self.wait_element_to_be_clickable(By.XPATH, self.button_btn_supporting_document_add)
#             self.execute_script_click(click_btn_supporting_document_add)
#             return 1, self.RETURN_BTN_SUPPORTING_DOCUMENT_ADD
#         except NoSuchElementException:
#             return 0, self.RETURN_BTN_SUPPORTING_DOCUMENT_ADD
#
#     def pth_bir_form_2303(self, testdata):
#         try:
#             input_pth_bir_form_2303 = self.wait_precense_of_element_located(By.XPATH, self.field_pth_bir_form_2303)
#             input_pth_bir_form_2303.send_keys(testdata)
#             return 1, self.RETURN_PTH_BIR_FORM_2303
#         except NoSuchElementException:
#             return 0, self.RETURN_PTH_BIR_FORM_2303
#     def date_bir_form_2303_validity(self, testdata):
#         input_date_bir_form_2303_validity = self.wait_precense_of_element_located(By.XPATH, self.field_date_bir_form_2303_validity)
#         execute_result = self.function_date_picker_select_date(4, testdata, input_date_bir_form_2303_validity)
#         return execute_result, self.RETURN_DATE_BIR_FORM_2303_VALIDITY
#
#     def pth_sec_certificate(self, testdata):
#         try:
#             input_pth_sec_certificate = self.wait_precense_of_element_located(By.XPATH, self.field_pth_sec_certificate)
#             input_pth_sec_certificate.send_keys(testdata)
#             return 1, self.RETURN_PTH_SEC_CERTIFICATE
#         except NoSuchElementException:
#             return 0, self.RETURN_PTH_SEC_CERTIFICATE
#
#     def date_sec_certificate_validity(self, testdata):
#         input_date_sec_certificate_validity = self.wait_precense_of_element_located(By.XPATH, self.field_date_sec_certificate_validity)
#         execute_result = self.function_date_picker_select_date(5, testdata, input_date_sec_certificate_validity)
#         return execute_result, self.RETURN_DATE_SEC_CERTIFICATE_VALIDITY
#
#     def pth_dti_certificate_accreditations(self, testdata):
#         try:
#             input_pth_dti_certificate_accreditations = self.wait_precense_of_element_located(By.XPATH, self.field_pth_dti_certificate_accreditations)
#             input_pth_dti_certificate_accreditations.send_keys(testdata)
#             return 1, self.RETURN_PTH_DTI_CERTIFICATE_ACCREDITATIONS
#         except NoSuchElementException:
#             return 0, self.RETURN_PTH_DTI_CERTIFICATE_ACCREDITATIONS
#
#     def date_dti_certificate_accreditations_validity(self, testdata):
#         input_date_dti_certificate_accreditations_validity = self.wait_precense_of_element_located(By.XPATH, self.field_date_dti_certificate_accreditations_validity)
#         execute_result = self.function_date_picker_select_date(10, testdata, input_date_dti_certificate_accreditations_validity)
#         return execute_result, self.RETURN_DATE_DTI_CERTIFICATE_ACCREDITATIONS_VALIDITY


class ProvideCompanyInformationRepInfo(BaseDriver):
    def __init__(self, driver):
        self.driver = driver

    field_txt_rep_information_firstname = '//input[@id="representativeFirstName"]'
    field_txt_rep_information_middlename = '//input[@id="representativeMiddleName"]'
    field_txt_rep_information_lastname = '//input[@id="representativeLastName"]'
    field_txt_rep_information_position = '//input[@id="representativePosition0"]'
    field_txt_rep_information_mobile_number = '//input[@id="representativeMobileNumber"]'
    field_txt_rep_information_email = '//input[@id="representativeEmailAddress"]'

    RETURN_TXT_REP_INFORMATION_FIRSTNAME = 'Representative information firstname INPUT'
    RETURN_TXT_REP_INFORMATION_MIDDLENAME = 'Representative information middlename INPUT'
    RETURN_TXT_REP_INFORMATION_LASTNAME = 'Representative information lastname INPUT'
    RETURN_TXT_REP_INFORMATION_POSITION = 'Representative information position INPUT'
    RETURN_TXT_REP_INFORMATION_MOBILE_NUMBER = 'Representative information mobile number INPUT'
    RETURN_TXT_REP_INFORMATION_EMAIL = 'Representative information representative INPUT'

    def txt_rep_information_firstname(self, testdata):
        try:
            input_txt_rep_information_firstname = self.locate_element_by(By.XPATH, self.field_txt_rep_information_firstname)
            input_txt_rep_information_firstname.send_keys(testdata)
            return 1, self.RETURN_TXT_REP_INFORMATION_FIRSTNAME
        except NoSuchElementException:
            return 0, self.RETURN_TXT_REP_INFORMATION_FIRSTNAME

    def txt_rep_information_middlename(self, testdata):
        try:
            input_txt_rep_information_middlename = self.locate_element_by(By.XPATH,self.field_txt_rep_information_middlename)
            input_txt_rep_information_middlename.send_keys(testdata)
            return 1, self.RETURN_TXT_REP_INFORMATION_MIDDLENAME
        except NoSuchElementException:
            return 0, self.RETURN_TXT_REP_INFORMATION_MIDDLENAME

    def txt_rep_information_lastname(self, testdata):
        try:
            input_txt_rep_information_lastname = self.locate_element_by(By.XPATH,self.field_txt_rep_information_lastname)
            input_txt_rep_information_lastname.send_keys(testdata)
            return 1, self.RETURN_TXT_REP_INFORMATION_POSITION
        except NoSuchElementException:
            return 0, self.RETURN_TXT_REP_INFORMATION_POSITION

    def txt_rep_information_position(self, testdata):
        try:
            input_txt_rep_information_position = self.locate_element_by(By.XPATH,self.field_txt_rep_information_position)
            input_txt_rep_information_position.send_keys(testdata)
            return 1, self.RETURN_TXT_REP_INFORMATION_EMAIL
        except NoSuchElementException:
            return 0, self.RETURN_TXT_REP_INFORMATION_EMAIL

    def txt_rep_information_mobile_number(self, testdata):
        try:
            input_txt_rep_information_mobile_number = self.locate_element_by(By.XPATH,self.field_txt_rep_information_mobile_number)
            input_txt_rep_information_mobile_number.send_keys(testdata)
            return 1, self.RETURN_TXT_REP_INFORMATION_MOBILE_NUMBER
        except NoSuchElementException:
            return 0, self.RETURN_TXT_REP_INFORMATION_MOBILE_NUMBER

    def txt_rep_information_email(self, testdata):
        try:
            input_txt_rep_information_email = self.locate_element_by(By.XPATH,self.field_txt_rep_information_email)
            input_txt_rep_information_email.send_keys(testdata)
            return 1, self.RETURN_TXT_REP_INFORMATION_EMAIL
        except NoSuchElementException:
            return 0, self.RETURN_TXT_REP_INFORMATION_EMAIL


class ProvideCompanyInformationPrincipalOfficer(BaseDriver):
    def __init__(self, driver):
        self.driver = driver

    field_txt_principal_officer_firstname = '//input[@id="principalOfficersFirstName"]'
    field_txt_principal_officer_middlename = '//input[@id="principalOfficersMiddleName"]'
    field_txt_principal_officer_lastname = '//input[@id="principalOfficersLastName"]'
    field_txt_principal_officer_position = '//input[@id="principalOfficersPosition0"]'
    field_txt_principal_officer_mobilenum = '//input[@id="principalOfficersMobileNumber"]'
    field_txt_principal_officer_email = '//input[@id="principalOfficersEmailAddress"]'

    RETURN_TXT_PRINCIPAL_OFFICER_FIRSTNAME = 'Provide principal officer firstname INPUT'
    RETURN_TXT_PRINCIPAL_OFFICER_MIDDLENAME = 'Provide principal officer middlename INPUT'
    RETURN_TXT_PRINCIPAL_OFFICER_LASTNAME = 'Provide principal officer lastname INPUT'
    RETURN_TXT_PRINCIPAL_OFFICER_POSITION = 'Provide principal officer position INPUT'
    RETURN_TXT_PRINCIPAL_OFFICER_MOBILENUM = 'Provide principal officer mobile number INPUT'
    RETURN_TXT_PRINCIPAL_OFFICER_EMAIL = 'Provide principal officer email address INPUT'


    def txt_principal_officer_firstname(self, testdata):
        try:
            input_txt_principal_officer_firstname = self.locate_element_by(By.XPATH, self.field_txt_principal_officer_firstname)
            input_txt_principal_officer_firstname.send_keys(testdata)
            return 1, self.RETURN_TXT_PRINCIPAL_OFFICER_FIRSTNAME
        except NoSuchElementException:
            return 0, self.RETURN_TXT_PRINCIPAL_OFFICER_FIRSTNAME

    def txt_principal_officer_middlename(self, testdata):
        try:
            input_txt_principal_officer_middlename = self.locate_element_by(By.XPATH, self.field_txt_principal_officer_middlename)
            input_txt_principal_officer_middlename.send_keys(testdata)
            return 1, self.RETURN_TXT_PRINCIPAL_OFFICER_MIDDLENAME
        except NoSuchElementException:
            return 0, self.RETURN_TXT_PRINCIPAL_OFFICER_MIDDLENAME

    def txt_principal_officer_lastname(self, testdata):
        try:
            input_txt_principal_officer_lastname = self.locate_element_by(By.XPATH, self.field_txt_principal_officer_lastname)
            input_txt_principal_officer_lastname.send_keys(testdata)
            return 1, self.RETURN_TXT_PRINCIPAL_OFFICER_LASTNAME
        except NoSuchElementException:
            return 0, self.RETURN_TXT_PRINCIPAL_OFFICER_LASTNAME

    def txt_principal_officer_position(self, testdata):
        try:
            input_txt_principal_officer_position = self.locate_element_by(By.XPATH, self.field_txt_principal_officer_position)
            input_txt_principal_officer_position.send_keys(testdata)
            return 1, self.RETURN_TXT_PRINCIPAL_OFFICER_POSITION
        except NoSuchElementException:
            return 0, self.RETURN_TXT_PRINCIPAL_OFFICER_POSITION

    def txt_principal_officer_mobilenum(self, testdata):
        try:
            input_txt_principal_officer_mobilenum = self.locate_element_by(By.XPATH, self.field_txt_principal_officer_mobilenum)
            input_txt_principal_officer_mobilenum.send_keys(testdata)
            return 1, self.RETURN_TXT_PRINCIPAL_OFFICER_MOBILENUM
        except NoSuchElementException:
            return 0, self.RETURN_TXT_PRINCIPAL_OFFICER_MOBILENUM

    def txt_principal_officer_email(self, testdata):
        try:
            input_txt_principal_officer_email = self.locate_element_by(By.XPATH, self.field_txt_principal_officer_email)
            input_txt_principal_officer_email.send_keys(testdata)
            return 1, self.RETURN_TXT_PRINCIPAL_OFFICER_EMAIL
        except NoSuchElementException:
            return 0, self.RETURN_TXT_PRINCIPAL_OFFICER_EMAIL


# class ProvideCompanyInformationContactInfo(BaseDriver):
#     def __init__(self, driver):
#         self.driver = driver
#
#     field_txt_contact_information_lastname = '//input[@id="lastname" and @name="lastname"]'
#     field_txt_contact_information_firstname = '//input[@id="firstname" and @name="firstname"]'
#     field_txt_contact_information_middlename = '//input[@id="middlename" and @name="middlename"]'
#     field_txt_contact_information_position = '//input[@id="companyPosition" and @name="company_position"]'
#     field_txt_contact_information_mobile_num = '//input[@id="mobileNumber" and @name="mobile_number"]'
#     field_txt_contact_information_email = '//input[@id="email" and @name="auth_user.email_address"]'
#     field_txt_contact_information_username = '//input[@id="username" and @name="auth_user.username"]'
#     field_txt_contact_information_password = '//input[@id="password" and @name="auth_user.password"]'
#     field_txt_contact_information_cpassword = '//input[@id="confirmPassword" and @name="confirm_password"]'
#     button_btn_proceed_application_details = '//button[@id="btn_details_confirm_Id"]'
#
#     RETURN_TXT_CONTACT_INFORMATION_LASTNAME = 'Provide contact information lastname INPUT'
#     RETURN_TXT_CONTACT_INFORMATION_FIRSTNAME = 'Provide contact information lastname INPUT'
#     RETURN_TXT_CONTACT_INFORMATION_MIDDLENAME = 'Provide contact information middlename INPUT'
#     RETURN_TXT_CONTACT_INFORMATION_POSITION = 'Provide contact information position INPUT'
#     RETURN_TXT_CONTACT_INFORMATION_MOBILE_NUM = 'Provide contact information mobile number INPUT'
#     RETURN_TXT_CONTACT_INFORMATION_EMAIL = 'Provide contact information email INPUT'
#     RETURN_TXT_CONTACT_INFORMATION_USERNAME = 'Provide contact information username INPUT'
#     RETURN_TXT_CONTACT_INFORMATION_PASSWORD = 'Provide contact information password INPUT'
#     RETURN_TXT_CONTACT_INFORMATION_CPASSWORD = 'Provide contact information confirm password INPUT'
#     RETURN_BTN_PROCEED_APPLICATION_DETAILS = 'Proceed application and review details CLICK'
#
#
#     def txt_contact_information_lastname(self, testdata):
#         try:
#             input_txt_contact_information_lastname = self.locate_element_by(By.XPATH, self.field_txt_contact_information_lastname)
#             input_txt_contact_information_lastname.send_keys(testdata)
#             return 1, self.RETURN_TXT_CONTACT_INFORMATION_LASTNAME
#         except NoSuchElementException:
#             return 0, self.RETURN_TXT_CONTACT_INFORMATION_LASTNAME
#
#     def txt_contact_information_firstname(self, testdata):
#         try:
#             input_txt_contact_information_firstname = self.locate_element_by(By.XPATH, self.field_txt_contact_information_firstname)
#             input_txt_contact_information_firstname.send_keys(testdata)
#             return 1, self.RETURN_TXT_CONTACT_INFORMATION_FIRSTNAME
#         except NoSuchElementException:
#             return 0, self.RETURN_TXT_CONTACT_INFORMATION_FIRSTNAME
#
#     def txt_contact_information_middlename(self, testdata):
#         try:
#             input_txt_contact_information_middlename = self.locate_element_by(By.XPATH, self.field_txt_contact_information_middlename)
#             input_txt_contact_information_middlename.send_keys(testdata)
#             return 1, self.RETURN_TXT_CONTACT_INFORMATION_MIDDLENAME
#         except NoSuchElementException:
#             return 0, self.RETURN_TXT_CONTACT_INFORMATION_MIDDLENAME
#
#     def txt_contact_information_position(self, testdata):
#         try:
#             input_txt_contact_information_position = self.locate_element_by(By.XPATH, self.field_txt_contact_information_position)
#             input_txt_contact_information_position.send_keys(testdata)
#             return 1, self.RETURN_TXT_CONTACT_INFORMATION_POSITION
#         except NoSuchElementException:
#             return 0, self.RETURN_TXT_CONTACT_INFORMATION_POSITION
#
#     def txt_contact_information_mobile_num(self, testdata):
#         try:
#             input_txt_contact_information_mobile_num = self.locate_element_by(By.XPATH, self.field_txt_contact_information_mobile_num)
#             input_txt_contact_information_mobile_num.send_keys(testdata)
#             return 1, self.RETURN_TXT_CONTACT_INFORMATION_MOBILE_NUM
#         except NoSuchElementException:
#             return 0, self.RETURN_TXT_CONTACT_INFORMATION_MOBILE_NUM
#
#     def txt_contact_information_email(self, testdata):
#         try:
#             input_txt_contact_information_email = self.locate_element_by(By.XPATH, self.field_txt_contact_information_email)
#             input_txt_contact_information_email.send_keys(testdata)
#             return 1, self.RETURN_TXT_CONTACT_INFORMATION_EMAIL
#         except NoSuchElementException:
#             return 0, self.RETURN_TXT_CONTACT_INFORMATION_EMAIL
#
#     def txt_contact_information_username(self, testdata):
#         try:
#             input_txt_contact_information_username = self.locate_element_by(By.XPATH,self.field_txt_contact_information_username)
#             input_txt_contact_information_username.send_keys(testdata)
#             return 1, self.RETURN_TXT_CONTACT_INFORMATION_USERNAME
#         except NoSuchElementException:
#             return 0, self.RETURN_TXT_CONTACT_INFORMATION_USERNAME
#
#     def txt_contact_information_password(self, testdata):
#         try:
#             input_txt_contact_information_password = self.locate_element_by(By.XPATH,self.field_txt_contact_information_password)
#             input_txt_contact_information_password.send_keys(testdata)
#             return 1, self.RETURN_TXT_CONTACT_INFORMATION_PASSWORD
#         except NoSuchElementException:
#             return 0, self.RETURN_TXT_CONTACT_INFORMATION_PASSWORD
#
#     def txt_contact_information_cpassword(self, testdata):
#         try:
#             input_txt_contact_information_cpassword = self.locate_element_by(By.XPATH,self.field_txt_contact_information_cpassword)
#             input_txt_contact_information_cpassword.send_keys(testdata)
#             return 1, self.RETURN_TXT_CONTACT_INFORMATION_CPASSWORD
#         except NoSuchElementException:
#             return 0, self.RETURN_TXT_CONTACT_INFORMATION_CPASSWORD
#
#     def btn_proceed_application_details(self):
#         try:
#             self.action_chain_move_to_element(self.button_btn_proceed_application_details)
#             click_btn_proceed_application_details = self.wait_element_to_be_clickable(By.XPATH, self.button_btn_proceed_application_details)
#             # self.execute_script_click(click_btn_proceed_application_details)
#             # self.execute_script_click(click_btn_proceed_application_details)
#             click_btn_proceed_application_details.click()
#             click_btn_proceed_application_details.click()
#             return 1, self.RETURN_BTN_PROCEED_APPLICATION_DETAILS
#         except NoSuchElementException:
#             return 0, self.RETURN_BTN_PROCEED_APPLICATION_DETAILS