from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from FrameWork.config_files.base_driver import BaseDriver
from FrameWork.pkg_utilities.utility_script_general import UtilityPackage
import time


class ProvideSPSupportingDocuments(BaseDriver):
    def __init__(self, driver):
        self.driver = driver

    field_pth_permit_license_trucks = '//input[@name="permits_and_licenses_truck[0][filename]"]'
    field_txt_permit_license_trucks_validity = '//input[@id="permitsAndLicensesTruckValidityDate0"]'
    field_txt_permit_license_trucks_validity_disp = '//html//body//form//div//div//div//div//div//div[2]//div//div//div[2]//div//div[5]//div[4]//div[1]//div//div//div[3]//input[2]'
    field_pth_truck_company_official = '//input[@name="official_list_of_trucks[0][filename]"]'
    field_txt_truck_company_official_validity = '//input[@id="officialListOfTrucksValidityDate0"]'
    field_txt_truck_company_official_validity_disp = '//html//body//form//div//div//div//div//div//div[2]//div//div//div[2]//div//div[5]//div[4]//div[3]//div//div//div[3]//input[2]'
    field_pth_copy_of_ltfrb_pa = '//input[@name="copy_of_land_transportation[0][filename]"]'
    field_pth_copy_of_ltfrb_pa_validity = '//input[@id="copyOfLandTransportationValidityDate0"]'
    field_pth_copy_of_ltfrb_pa_validity_disp = '//html//body//form//div//div//div//div//div//div[2]//div//div//div[2]//div//div[5]//div[4]//div[4]//div//div//div[3]//input[2]'
    field_pth_copy_of_lto_orcr = '//input[@name="copy_of_lto_cr[0][filename]"]'
    field_txt_copy_of_lto_orcr_validity = '//input[@id="copyOfLTOCRValidityDate0"]'
    field_txt_copy_of_lto_orcr_validity_disp = '//html//body//form//div//div//div//div//div//div[2]//div//div//div[2]//div//div[5]//div[4]//div[5]//div//div//div[3]//input[2]'
    field_pth_permits_license_fforwarders = '//input[@name="freight_forwarder_permits[0][filename]"]'
    field_txt_permits_license_fforwarders_validity = '//input[@id="freightForwarderPermitsValidityDate0"]'
    field_txt_permits_license_fforwarders_validity_disp = '//html//body//form//div//div//div//div//div//div[2]//div//div//div[2]//div//div[5]//div[4]//div[5]//div//div//div[3]//input[2]'
    field_pth_cab_cor = '//div[@id="cabCertificateOfRegistration"]//div//div//div[2]//input[@name="cab_certificate_of_registration[0][filename]"]'
    field_txt_cab_cor_validity = '//div[@id="cabCertificateOfRegistration"]//div//div//div[3]//input[@id="cabCertificateOfRegistrationValidityDate0"]'
    field_txt_cab_cor_validity_disp = '//div[@id="cabCertificateOfRegistration"]//div//div//div[3]//input[2]'
    field_pth_dti_certificate = '//div[@id="dtiCertificateAccreditation"]//div//div//div[2]//input[@name="dti_certificate_accreditation[0][filename]"]'
    field_txt_dti_certificate_validity = '//div[@id="dtiCertificateAccreditation"]//div//div//div[3]//input[@id="dtiCertificateAccreditationValidityDate0"]'
    field_txt_dti_certificate_validity_disp = '//div[@id="dtiCertificateAccreditation"]//div//div//div[3]//input[2]'
    field_pth_individual_licensed_broker = '//input[@name="individual_licensed_broker[0][filename]"]'
    field_txt_individual_licensed_broker_validity = '//input[@id="individualLicensedBrokerValidityDate0"]'
    field_txt_individual_licensed_broker_validity_disp = '//html//body//form//div//div//div//div//div//div[2]//div//div//div[2]//div//div[5]//div[4]//div[8]//div//div//div[3]//input[2]'
    field_pth_boc_customs_registration = '//div[@id="bocCertificateOfRegistration"]//div//div//div[2]//input[@name="boc_certificate_of_registration[0][filename]"]'
    field_txt_boc_customs_registration_validity = '//div[@id="bocCertificateOfRegistration"]//div//div//div[3]//input[@id="bocCertificateOfRegistrationValidityDate0"]'
    field_txt_boc_customs_registration_validity_disp = '//div[@id="bocCertificateOfRegistration"]//div//div//div[3]//input[2]'
    field_pth_security_agency_doc = '//input[@name="security_agency[0][filename]"]'
    field_txt_security_agency_doc_validity = '//input[@id="securityAgencyValidityDate0"]'
    field_txt_security_agency_doc_validity_disp = '//html//body//form//div//div//div//div//div//div[2]//div//div//div[2]//div//div[5]//div[4]//div[10]//div//div//div[3]//input[2]'
    field_pth_pnp_lto = '//input[@name="pnp_license_to_operate[0][filename]"]'
    field_txt_pnp_lto_validity = '//input[@id="pnpLicenseToOperateValidityDate0"]'
    field_txt_pnp_lto_validity_disp = '//html//body//form//div//div//div//div//div//div[2]//div//div//div[2]//div//div[5]//div[4]//div[9]//div//div//div[3]//input[2]'
    field_pth_dole_do174 = '//input[@name="dole_department_order[0][filename]"]'
    field_txt_dole_do174_validity = '//input[@id="doleDepartmentOrderValidityDate0"]'
    field_txt_dole_do174_validity_disp = '//html//body//form//div//div//div//div//div//div[2]//div//div//div[2]//div//div[5]//div[4]//div[10]//div//div//div[3]//input[2]'
    field_pth_bir_2303_form = '//div[@id="birForm2303"]//div//div//div[2]//input[@id="birForm2303Filename0"]'
    field_txt_bir_2303_form_validity = '//div[@id="birForm2303"]//div//div//div[3]//input[@name="bir_form_2303[0][validity_date]"]'
    field_txt_bir_2303_form_validity_disp = '//div[@id="birForm2303"]//div//div//div[3]//input[2]'
    field_pth_sec_certificate = '//div[@id="secCertificate"]//div//div//div[2]//input[@id="secCertificateFilename0"]'
    field_txt_sec_certificate_validity = '//div[@id="secCertificate"]//div//div//div[3]//input[@name="sec_certificate[0][validity_date]"]'
    field_txt_sec_certificate_validity_disp = '//div[@id="secCertificate"]//div//div//div[3]//input[2]'
    button_proceed_principal_officer = '//button[@id="btn_principal_officer"]'

    RETURN_PTH_PERMIT_LICENSE_TRUCKS = 'SP Supporting documents permit license of trucks FILE INPUT'
    RETURN_TXT_PERMIT_LICENSE_TRUCKS_VALIDITY = 'SP Supporting documents permit license of trucks validity DATE INPUT'
    RETURN_PTH_TRUCK_COMPANY_OFFICIAL = 'SP Supporting documents truck company officials FILE INPUT'
    RETURN_TXT_TRUCK_COMPANY_OFFICIAL_VALIDITY = 'SP Supporting documents truck company officials validity DATE INPUT'
    RETURN_PTH_COPY_OF_LTFRB_PA = 'SP Supporting documents copy of LTFRB PA FILE INPUT'
    RETURN_PTH_COPY_OF_LTFRB_PA_VALIDITY = 'SP Supporting documents copy of LTFRB PA validity DATE INPUT'
    RETURN_PTH_COPY_OF_LTO_ORCR = 'SP Supporting documents copy of LTO ORCR FILE INPUT'
    RETURN_TXT_COPY_OF_LRO_ORCR_VALIDITY = 'SP Supporting documents copy of LTO ORCR validity DATE INPUT'
    RETURN_PTH_PERMIT_LICENSE_FFORWARDERS = 'SP Supporting documents liscense permits of freight forwarders FILE INPUT'
    RETURN_TXT_PERMIT_LICENSE_FFORWARDERS_VALIDITY = 'SP Supporting documents liscense permits of freight forwarders validity DATE INPUT'
    RETURN_PTH_CAB_COR = 'SP Supporting documents CAB certificate of registration FILE INPUT'
    RETURN_TXT_CAB_COR_VALIDITY = 'SP Supporting documents CAB certificate of registration validity DATE INPUT'
    RETURN_PTH_DTI_CERTIFICATE = 'SP Supporting documents DTI certificate of registration FILE INPUT'
    RETURN_TXT_DTI_CERTIFICATE_VALIDITY = 'SP Supporting documents DTI certificate of registration validity DATE INPUT'
    RETURN_PATH_INDIVIDUAL_LICENSED_BROKER = 'SP Supporting documents individual licensed broker FILE INPUT'
    RETURN_TXT_INDIVIDUAL_LICENSED_BROKER_VALIDITY = 'SP Supporting documents individual liscensed broker validity DATE INPUT'
    RETURN_PATH_BOC_CUSTOMS_REGISTRATION = 'SP Supporting documents customs registration FILE INPUT'
    RETURN_TXT_BOC_CUSTOMS_REGISTRATION_VALIDITY = 'SP Supporting documents customs registration validity DATE INPUT'
    RETURN_PATH_SECURITY_AGENCY_DOC = 'SP Supporting documents security agency docs FILE INPUT'
    RETURN_TXT_SECURITY_AGENCY_DOC_VALIDITY = 'SP Supporting documents security agency docs validity DATE INPUT'
    RETURN_PATH_PNP_LTO = 'SP Supporting documents PNP License to operate FILE INPUT'
    RETURN_TXT_PNP_LTO_VALIDITY = 'SP Supporting documents PNP License to operate validity DATE INPUT'
    RETURN_PATH_DOLE_DO174 = 'SP Supporting documents DOLE deparment order 174 FILE INPUT'
    RETURN_TXT_DOLE_DO174_VALIDITY = 'SP Supporting documents DOLE deparment order 174 validity DATE INPUT'
    RETURN_PATH_BIR_2303_FORM = 'SP Supporting documents BIR 2303 form FILE INPUT'
    RETURN_TXT_BIR_2303_FORM_VALIDITY = 'SP Supporting documents BIR 2303 form validity DATE INPUT'
    RETURN_PTH_SEC_CERTIFICATE = 'SP Supporting documents SEC Certificate FILE INPUT'
    RETURN_TXT_SEC_CERTIFICATE_VALIDITY = 'SP Supporting documents SEC Certificate validity DATE INPUT'
    RETURN_PROCEED_PRINCIPAL_OFFICER = 'Proceed to principal office BUTTON CLICK'

    scripting_utility_tools = UtilityPackage()

    def force_date_input(self, date_value, date_field, date_display):
        try:
            input_txt_date_field = self.locate_element_by(By.XPATH, date_field)
            input_txt_date_display = self.locate_element_by(By.XPATH, date_display)
            self.execute_script_date_value(self.convert_date_format(date_value), input_txt_date_field)
            self.execute_script_date_value(date_value, input_txt_date_display)
            return 1
        except NoSuchElementException:
            return 0

    def pth_bir_2303_form(self, testdata):
        try:
            input_pth_bir_2303_form = self.wait_precense_of_element_located(By.XPATH, self.field_pth_bir_2303_form)
            input_pth_bir_2303_form.send_keys(testdata)
            time.sleep(5)
            return 1, self.RETURN_PATH_BIR_2303_FORM
        except NoSuchElementException:
            return 0, self.RETURN_PATH_BIR_2303_FORM

    def txt_bir_2303_form_validity(self, testdata):
        input_txt_bir_2303_form_validity = self.wait_precense_of_element_located(By.XPATH, self.field_txt_bir_2303_form_validity_disp)
        execute_result = self.date_picker_select_date(4, testdata, input_txt_bir_2303_form_validity)
        time.sleep(5)
        return execute_result, self.RETURN_TXT_BIR_2303_FORM_VALIDITY

    def pth_sec_certificate(self, testdata):
        try:
            input_pth_sec_certificate = self.wait_element_to_be_clickable(By.XPATH, self.field_pth_sec_certificate)
            input_pth_sec_certificate.send_keys(testdata)
            return 1, self.RETURN_PTH_SEC_CERTIFICATE
        except NoSuchElementException:
            return 0, self.RETURN_PTH_SEC_CERTIFICATE

    def txt_sec_certificate_validity(self, testdata):
        input_txt_sec_certificate_validity = self.wait_precense_of_element_located(By.XPATH,
                                                                                   self.field_txt_sec_certificate_validity_disp)
        execute_result = self.date_picker_select_date(5, testdata, input_txt_sec_certificate_validity)
        time.sleep(5)
        return execute_result, self.RETURN_TXT_SEC_CERTIFICATE_VALIDITY

    def pth_truck_company_official(self, testdata):
        try:
            input_pth_truck_company_official = self.wait_element_to_be_clickable(By.XPATH,
                                                                                 self.field_pth_truck_company_official)
            input_pth_truck_company_official.send_keys(testdata)
            return 1, self.RETURN_PTH_TRUCK_COMPANY_OFFICIAL
        except NoSuchElementException:
            return 0, self.RETURN_PTH_TRUCK_COMPANY_OFFICIAL

    def txt_truck_company_official_validity(self, testdata):
        input_txt_truck_company_official_validity = self.wait_precense_of_element_located(By.XPATH,
                                                                                          self.field_txt_truck_company_official_validity_disp)
        execute_result = self.date_picker_select_date(6, testdata, input_txt_truck_company_official_validity)
        time.sleep(5)
        return execute_result, self.RETURN_TXT_TRUCK_COMPANY_OFFICIAL_VALIDITY

    def pth_copy_of_ltfrb_pa(self, testdata):
        try:
            input_pth_copy_of_ltfrb_pa = self.wait_element_to_be_clickable(By.XPATH, self.field_pth_copy_of_ltfrb_pa)
            input_pth_copy_of_ltfrb_pa.send_keys(testdata)
            return 1, self.RETURN_PTH_COPY_OF_LTFRB_PA
        except NoSuchElementException:
            return 0, self.RETURN_PTH_COPY_OF_LTFRB_PA

    def txt_copy_of_ltfrb_pa_validity(self, testdata):
        input_txt_copy_of_ltfrb_pa_validity = self.wait_precense_of_element_located(By.XPATH,
                                                                                    self.field_pth_copy_of_ltfrb_pa_validity_disp)
        execute_result = self.date_picker_select_date(7, testdata, input_txt_copy_of_ltfrb_pa_validity)
        time.sleep(5)
        return execute_result, self.RETURN_PTH_COPY_OF_LTFRB_PA_VALIDITY

    def pth_copy_of_lto_orcr(self, testdata):
        try:
            input_pth_copy_of_lto_orcr = self.wait_element_to_be_clickable(By.XPATH, self.field_pth_copy_of_lto_orcr)
            input_pth_copy_of_lto_orcr.send_keys(testdata)
            return 1, self.RETURN_PTH_COPY_OF_LTO_ORCR
        except NoSuchElementException:
            return 0, self.RETURN_PTH_COPY_OF_LTO_ORCR

    def txt_copy_of_lto_orcr_validity(self, testdata):
        input_txt_copy_of_lto_orcr_validity = self.wait_precense_of_element_located(By.XPATH,
                                                                                    self.field_txt_copy_of_lto_orcr_validity_disp)
        execute_result = self.date_picker_select_date(8, testdata, input_txt_copy_of_lto_orcr_validity)
        time.sleep(5)
        return execute_result, self.RETURN_TXT_COPY_OF_LRO_ORCR_VALIDITY

    def pth_cab_certificate_of_reg(self, testdata):
        try:
            input_pth_cab_cor = self.wait_element_to_be_clickable(By.XPATH, self.field_pth_cab_cor)
            input_pth_cab_cor.send_keys(testdata)
            return 1, self.RETURN_PTH_CAB_COR
        except NoSuchElementException:
            return 0, self.RETURN_PTH_CAB_COR

    def txt_cab_certificate_of_reg_validity(self, testdata):
        input_txt_cab_certificate_of_reg_validity = self.wait_precense_of_element_located(By.XPATH,
                                                                                          self.field_txt_cab_cor_validity_disp)
        execute_result = self.date_picker_select_date(9, testdata, input_txt_cab_certificate_of_reg_validity)
        time.sleep(5)
        return execute_result, self.RETURN_TXT_CAB_COR_VALIDITY

    def pth_dti_certificate_of_accre(self, testdata):
        try:
            input_pth_dti_certificate = self.wait_element_to_be_clickable(By.XPATH, self.field_pth_dti_certificate)
            input_pth_dti_certificate.send_keys(testdata)
            return 1, self.RETURN_PTH_DTI_CERTIFICATE
        except NoSuchElementException:
            return 0, self.RETURN_PTH_DTI_CERTIFICATE

    def txt_dti_certificate_of_accre_validity(self, testdata):
        input_txt_dti_certificate_of_accre_validity = self.wait_precense_of_element_located(By.XPATH,
                                                                                            self.field_txt_dti_certificate_validity_disp)
        execute_result = self.date_picker_select_date(10, testdata, input_txt_dti_certificate_of_accre_validity)
        time.sleep(5)
        return execute_result, self.RETURN_TXT_DTI_CERTIFICATE_VALIDITY

    def pth_boc_customs_registration(self, testdata):
        try:
            input_pth_boc_customs_registration = self.wait_element_to_be_clickable(By.XPATH,
                                                                                   self.field_pth_boc_customs_registration)
            input_pth_boc_customs_registration.send_keys(testdata)
            return 1, self.RETURN_PATH_BOC_CUSTOMS_REGISTRATION
        except NoSuchElementException:
            return 0, self.RETURN_PATH_BOC_CUSTOMS_REGISTRATION

    def txt_boc_customs_registration_validity(self, testdata):
        input_txt_boc_customs_registration_validity = self.wait_precense_of_element_located(By.XPATH,
                                                                                            self.field_txt_boc_customs_registration_validity_disp)
        execute_result = self.date_picker_select_date(11, testdata, input_txt_boc_customs_registration_validity)
        time.sleep(5)
        return execute_result, self.RETURN_TXT_BOC_CUSTOMS_REGISTRATION_VALIDITY

    def pth_pnp_lto(self, testdata):
        try:
            input_pth_pnp_lto = self.wait_element_to_be_clickable(By.XPATH, self.field_pth_pnp_lto)
            input_pth_pnp_lto.send_keys(testdata)
            return 1, self.RETURN_PATH_PNP_LTO
        except NoSuchElementException:
            return 0, self.RETURN_PATH_PNP_LTO

    def txt_pnp_lto_validity(self, testdata):
        input_txt_pnp_lto = self.wait_precense_of_element_located(By.XPATH, self.field_txt_pnp_lto_validity_disp)
        execute_result = self.date_picker_select_date(12, testdata, input_txt_pnp_lto)
        time.sleep(5)
        return execute_result, self.RETURN_TXT_PNP_LTO_VALIDITY

    def pth_dole_do174(self, testdata):
        try:
            input_pth_dole_do174 = self.wait_element_to_be_clickable(By.XPATH, self.field_pth_dole_do174)
            input_pth_dole_do174.send_keys(testdata)
            return 1, self.RETURN_PATH_DOLE_DO174
        except NoSuchElementException:
            return 0, self.RETURN_PATH_DOLE_DO174

    def txt_dole_do174_validity(self, testdata):
        input_txt_dole_do174 = self.wait_precense_of_element_located(By.XPATH, self.field_txt_dole_do174_validity_disp)
        execute_result = self.date_picker_select_date(13, testdata, input_txt_dole_do174)
        time.sleep(5)
        return execute_result, self.RETURN_TXT_DOLE_DO174_VALIDITY

    def pth_permit_license_trucks(self, testdata):
        try:
            input_pth_permit_license_trucks = self.wait_element_to_be_clickable(By.XPATH,
                                                                                self.field_pth_permit_license_trucks)
            input_pth_permit_license_trucks.send_keys(testdata)
            return 1, self.RETURN_PTH_PERMIT_LICENSE_TRUCKS
        except NoSuchElementException:
            return 0, self.RETURN_PTH_PERMIT_LICENSE_TRUCKS

    def txt_permit_license_trucks_validity(self, testdata):
        execute_result = self.force_date_input(testdata, self.field_txt_permit_license_trucks_validity,
                                               self.field_txt_permit_license_trucks_validity_disp)
        return execute_result, self.RETURN_TXT_PERMIT_LICENSE_TRUCKS_VALIDITY

    def pth_permits_license_fforwarders(self, testdata):
        try:
            input_pth_permits_license_fforwarders = self.wait_element_to_be_clickable(By.XPATH,
                                                                                      self.field_pth_permits_license_fforwarders)
            input_pth_permits_license_fforwarders.send_keys(testdata)
            return 1, self.RETURN_PTH_PERMIT_LICENSE_FFORWARDERS
        except NoSuchElementException:
            return 0, self.RETURN_PTH_PERMIT_LICENSE_FFORWARDERS

    def txt_permits_license_fforwarders_validity(self, testdata):
        execute_result = self.force_date_input(testdata, self.field_txt_permits_license_fforwarders_validity,
                                               self.field_txt_permits_license_fforwarders_validity_disp)
        return execute_result, self.RETURN_TXT_PERMIT_LICENSE_FFORWARDERS_VALIDITY

    def pth_dti_indvi_licensed_broker(self, testdata):
        try:
            input_pth_dti_indvi_licensed_broker = self.wait_element_to_be_clickable(By.XPATH,
                                                                                    self.field_pth_individual_licensed_broker)
            input_pth_dti_indvi_licensed_broker.send_keys(testdata)
            return 1, self.RETURN_PATH_INDIVIDUAL_LICENSED_BROKER
        except NoSuchElementException:
            return 0, self.RETURN_PATH_INDIVIDUAL_LICENSED_BROKER

    def txt_dti_indvi_licensed_broker(self, testdata):
        execute_result = self.force_date_input(testdata, self.field_txt_individual_licensed_broker_validity,
                                               self.field_txt_individual_licensed_broker_validity_disp)
        return execute_result, self.RETURN_TXT_INDIVIDUAL_LICENSED_BROKER_VALIDITY

    def pth_security_agency(self, testdata):
        try:
            input_pth_security_agency = self.wait_element_to_be_clickable(By.XPATH, self.field_pth_security_agency_doc)
            input_pth_security_agency.send_keys(testdata)
            return 1, self.RETURN_PATH_SECURITY_AGENCY_DOC
        except NoSuchElementException:
            return 0, self.RETURN_PATH_SECURITY_AGENCY_DOC

    def txt_security_agency(self, testdata):
        execute_result = self.force_date_input(testdata, self.field_txt_security_agency_doc_validity,
        self.field_txt_security_agency_doc_validity_disp)
        return execute_result, self.RETURN_TXT_SECURITY_AGENCY_DOC_VALIDITY

    def btn_proceed_principal_officer(self):
        try:
            click_btn_proceed_principal_officer = self.wait_element_to_be_clickable(By.XPATH,
                                                                                    self.button_proceed_principal_officer)
            self.execute_script_click(click_btn_proceed_principal_officer)
            return 1, self.RETURN_PROCEED_PRINCIPAL_OFFICER
        except NoSuchElementException:
            return 0, self.RETURN_PROCEED_PRINCIPAL_OFFICER

    def date_picker_select_date(self, date_input_position, date_input_value, date_input_element):
        date_input_element.click()
        get_data_position_date_loc = self.scripting_utility_tools.date_picker_position_location(date_input_position)
        get_data_position_date_data = self.scripting_utility_tools.date_picker_data_strptime(date_input_value)

        select_date_picker_year = get_data_position_date_loc[0]
        select_date_picker_month = get_data_position_date_loc[1]
        intial_date_picker_date = get_data_position_date_loc[2]

        date_picker_year = get_data_position_date_data[0]
        date_picker_month = get_data_position_date_data[1]
        date_picker_date = get_data_position_date_data[2]

        select_date_picker_date = intial_date_picker_date + date_picker_date + '"]'

        input_date_picker_month_txt = self.scripting_utility_tools.date_picker_select_month(date_picker_month)

        try:
            input_date_picker_year = self.wait_precense_of_element_located(By.XPATH, select_date_picker_year)
            input_date_picker_month = self.wait_precense_of_element_located(By.XPATH, select_date_picker_month)
            try:
                input_date_picker_year.click()
                input_date_picker_year.clear()
                input_date_picker_year.send_keys(date_picker_year)

                self.select_dropdown_by_visible_text(input_date_picker_month, input_date_picker_month_txt)

                select_date_picker_date = self.wait_precense_of_element_located(By.XPATH, select_date_picker_date)
                time.sleep(2)
                select_date_picker_date.click()
                return 1
            except NoSuchElementException and ElementNotInteractableException:
                return 0
        except NoSuchElementException and ElementNotInteractableException:
            return 0
