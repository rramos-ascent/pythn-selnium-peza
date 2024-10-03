from FrameWork.config_files.frame_work_base_driver import FrameWorkBaseDriver

class BermsSProviderElementLocations(FrameWorkBaseDriver):
    def __init__(self, driver):
        self.driver = driver

    def get_berms_sp_supporting_documents(self, get_element):
        field_elements_locations = {
            "main_menu_access": '//div[@id="stepSupportingDocs"]//button//span[1]',
            "path_boc_certificate_registration": '//input[@id="supportingDocFilename3"]',
            "path_sec_certificate_registration": '//div[@id="suppDocWrapper_crsec"]//div[1]//div[1]//div//label//input',
            "path_cor_soleproprietorship": '//div[@id="suppDocWrapper_crsp"]//div[1]//div[1]//div//label//input',
            "path_dole_department_order_174_license": '//div[@id="suppDocWrapper_dole_do"]//div[1]//div[1]//div//label//input',
            "path_cab_registration_certificate": '//div[@id="suppDocWrapper_cab"]//div[1]//div[1]//div//label//input',
            "path_dti_fteb_registration_certificate": '//div[@id="suppDocWrapper_dti_fteb"]//div[1]//div[1]//div//label//input',
            "path_notarized_application_form": '//div[@id="suppDocWrapper_naf"]//div[1]//div[1]//div//label//input',
            "path_income_tax_return": '//div[@id="suppDocWrapper_itr"]//div[1]//div[1]//div//label//input',
            "path_mayors_permit": '//div[@id="suppDocWrapper_mayors_permit"]//div[1]//div[1]//div//label//input',
            "path_pnp_license_to_operate": '//div[@id="suppDocWrapper_pnp_lto"]//div[1]//div[1]//div//label//input',
            "path_list_trucks_signed_by_officers": '//div[@id="suppDocWrapper_olt"]//div[1]//div[1]//div//label//input',
            "txt_multiple_truck_plate_no_00": '//input[@id="supportingDocPlateNumber_0"]',
            "path_copy_lto_cor": '//div[@id="truckerDocsWrapper_0"]//div[1]//div[@id="suppDocWrapper_cr"]//div[1]//div[1]//div//label//input',
            "path_copy_lto_or": '//div[@id="truckerDocsWrapper_0"]//div[2]//div[@id="suppDocWrapper_or"]//div[1]//div[1]//div//label//input',
            "path_copy_ltfrb_franchise_pa": '//div[@id="truckerDocsWrapper_0"]//div[3]//div[@id="suppDocWrapper_pa"]//div[1]//div[1]//div//label//input',
            "button_berms_sp_submit": '//button[@id="btnSubmitApplication"]',
            "rbutton_modal_rules_regulations": '//input[@id="accept"]',
            "button_modal_rules_regulations_submit": '//button[@id="modal_submit"]',
            "button_modal_rules_regulations_modal_confirm": '//html//body//div[4]//div//div[6]//button[1][text()="Yes"]',
            "button_modal_rules_regulations_swal_success": '/html/body/div[3]/div/div[6]/button[1][text()="OK"]'
        }

        return_element_names = {
        }

        return field_elements_locations[get_element], ''

    def get_berms_sp_rep_principal_officers(self, get_element):
        field_elements_locations = {
            "main_menu_access": '//div[@id="berms-application"]//div//div[1]//div[5]//button//span[2]//span[1]',
            "txt_representative_first_name": '//input[@id="representativeFirstName"]',
            "txt_representative_middle_name": '//input[@id="representativeMiddleName"]',
            "txt_representative_last_name": '//input[@id="representativeLastName"]',
            "txt_representative_position": '//input[@id="representativePosition"]',
            "txt_representative_m_contact_number": '//input[@id="representativeMobileNumber"]',
            "txt_representative_email_address": '//input[@id="representativeEmailAddress"]',
            "button_principal_officer_add": '//*[@id="representative-officers"]//div[4]//button',
            "txt_principal_officer_first_name": '//input[@id="officerFirstName"]',
            "txt_principal_officer_middle_name": '//input[@id="officerMiddleName"]',
            "txt_principal_officer_last_name": '//input[@id="officerLastName"]',
            "option_principal_nationality": '//select[@id="officerNationalityId"]',
            "txt_principal_officer_position": '//input[@id="officerPosition"]',
            "txt_principal_officer_mobile": '//input[@id="officerMobileNumber"]',
            "txt_principal_officer_email": '//input[@id="officerEmailAddress"]',
            "button_principal_officer_add_proceed": '//button[@id="btnAddPrincipalOfficer"]'
        }

        return_element_names = {
        }

        return field_elements_locations[get_element], ''

    def get_berms_sp_applications(self, get_element):
        field_elements_locations = {
            "option_type_of_services": '',
        }

        return_element_names = {
        }

        return field_elements_locations[get_element], ''

    def get_berms_sp_applications_others(self, get_element):
        field_option_type_of_services = {
            "Customs Brokerage": '//input[@id="option0"]',
            "Security Agency": '//input[@id="option0"]',
            "Trucking/Hauling": '//input[@id="option3"]',
            "Air Freight Forwarding": '//input[@id="option1"]',
            "Sea Freight Forwarding": '//input[@id="option2"]'
        }

        match get_element:
            case 'option_type_of_services':
                return field_option_type_of_services