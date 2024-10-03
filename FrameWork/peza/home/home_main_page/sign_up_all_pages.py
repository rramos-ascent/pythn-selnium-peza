from FrameWork.config_files.frame_work_base_driver import FrameWorkBaseDriver


class SignUpAllElementLocations(FrameWorkBaseDriver):
    def __init__(self, driver):
        self.driver = driver

    def get_sp_principal_officer(self, get_element):
        field_elements_locations = {
            "txt_principal_officer_firstname": '//input[@id="principalOfficersFirstName"]',
            "txt_principal_officer_middlename": '//input[@id="principalOfficersMiddleName"]',
            "txt_principal_officer_lastname": '//input[@id="principalOfficersLastName"]',
            "txt_principal_officer_position": '//input[@id="principalOfficersPosition0"]',
            "txt_principal_officer_mobilenum": '//input[@id="principalOfficersMobileNumber"]',
            "txt_principal_officer_email": '//input[@id="principalOfficersEmailAddress"]'
        }

        return_element_names = {
            "txt_principal_officer_firstname": '',
            "txt_principal_officer_middlename": '',
            "txt_principal_officer_lastname": '',
            "txt_principal_officer_position": '',
            "txt_principal_officer_mobilenum": '',
            "txt_principal_officer_email": ''
        }

        return field_elements_locations[get_element], return_element_names[get_element]

    def get_sp_representative_information(self, get_element):
        field_elements_locations = {
            "txt_rep_information_firstname": '//input[@id="representativeFirstName"]',
            "txt_rep_information_middlename": '//input[@id="representativeMiddleName"]',
            "txt_rep_information_lastname": '//input[@id="representativeLastName"]',
            "txt_rep_information_position": '//input[@id="representativePosition0"]',
            "txt_rep_information_mobile_number": '//input[@id="representativeMobileNumber"]',
            "txt_rep_information_email": '//input[@id="representativeEmailAddress"]'
        }

        return_element_names = {
            "txt_rep_information_firstname": '',
            "txt_rep_information_middlename": '',
            "txt_rep_information_lastname": '',
            "txt_rep_information_position": '',
            "txt_rep_information_mobile_number": '',
            "txt_rep_information_email": ''
        }

        return field_elements_locations[get_element], return_element_names[get_element]

    def get_type_service_provider(self, get_element):
        field_elements_locations = {
            "rbutton_service_provider_type": '',
            "button_proceed_company_information": '//button[@id="btn_app_info"]'
        }

        return_element_names = {
            "rbutton_service_provider_type": '',
            "button_proceed_company_information": ''
        }

        return field_elements_locations[get_element], return_element_names[get_element]

    def get_type_service_provider_others(self, get_element):
        rbutton_service_provider_type = {
            "Air Freight Forwarding": '//input[@name="company.services" and @id="option0"]',
            "Security Agency": '//input[@name="company.services" and @id="option1"]',
            "Sea Freight Forwarding": '//input[@name="company.services" and @id="option2"]',
            "Private Express and/or Messengerial Delivery": '//input[@name="company.services" and @id="option3"]',
            "Courier Services": '//input[@name="company.services" and @id="option4"]',
            "Trucking/Hauling": '//input[@name="company.services" and @id="option5"]',
            "Customs Brokerage": '//input[@name="company.services" and @id="option6"]',
            "Importer": '//input[@name="company.services" and @id="option7"]',
            "Exporter": '//input[@name="company.services" and @id="option8"]',
            "Scrap Buyer": '//input[@name="company.services" and @id="option9"]',
            "Insurance Company": '//input[@name="company.services" and @id="option10"]',
            "Janitorial Services": '//input[@name="company.services" and @id="option11"]'
        }

        match get_element:
            case 'rbutton_service_provider_type':
                return rbutton_service_provider_type


    def get_registration_finalization(self, get_element):
        field_elements_locations = {
            "button_proceed_application_confirmation": '//button[@id="btnSubmitRegistration"]',
            "btn_submit_accept_terms_and_cond": '//button[@id="btnSubmit"]',
            "cbox_accept_terms_and_cond": '//input[@id="agreeCheckbox"]',
            "btn_modal_acceptance_confirmation": '//html//body//div[14]//div//div[6]//button[1]'
        }

        return_element_names = {
            "button_proceed_application_confirmation": '',
            "cbox_accept_terms_and_cond": '',
            "btn_submit_accept_terms_and_cond": '',
            "btn_modal_acceptance_confirmation": ''
        }

        return field_elements_locations[get_element], return_element_names[get_element]

    def get_company_information_contact_information(self, get_element):
        field_elements_locations = {
            "txt_contact_information_lastname": '//input[@id="lastname" and @name="lastname"]',
            "txt_contact_information_firstname": '//input[@id="firstname" and @name="firstname"]',
            "txt_contact_information_middlename": '//input[@id="middlename" and @name="middlename"]',
            "txt_contact_information_position": '//input[@id="companyPosition" and @name="company_position"]',
            "txt_contact_information_mobile_num": '//input[@id="mobileNumber" and @name="mobile_number"]',
            "txt_contact_information_email": '//input[@id="email" and @name="auth_user.email_address"]',
            "txt_contact_information_username": '//input[@id="username" and @name="auth_user.username"]',
            "txt_contact_information_password": '//input[@id="password" and @name="auth_user.password"]',
            "txt_contact_information_cpassword": '//input[@id="confirmPassword" and @name="confirm_password"]',
            "button_proceed_application_details": '//button[@id="btn_details_confirm_Id"]'
        }

        return_element_names = {
            "txt_contact_information_lastname": 'Provide contact information lastname INPUT',
            "txt_contact_information_firstname": 'Provide contact information lastname INPUT',
            "txt_contact_information_middlename": 'Provide contact information middlename INPUT',
            "txt_contact_information_position": 'Provide contact information position INPUT',
            "txt_contact_information_mobile_num": 'Provide contact information mobile number INPUT',
            "txt_contact_information_email": 'Provide contact information email INPUT',
            "txt_contact_information_username": 'Provide contact information username INPUT',
            "txt_contact_information_password": 'Provide contact information password INPUT',
            "txt_contact_information_cpassword": 'Provide contact information confirm password INPUT',
            "button_proceed_application_details": 'Proceed application and review details CLICK'
        }

        return field_elements_locations[get_element], return_element_names[get_element]

    def get_company_information_sup_docs(self, get_element):
        field_elements_locations = {
            "path_supporting_document_file": '//input[@name="file_ecozone_section"]',
            "txt_supporting_document_desc": '//input[@name="description_ecozone_section"]',
            "dp_supporting_document_validity": '//html//body//form//div//div//div//div//div//div[2]//div//div[1]//div[4]//div//div//div[8]//div[2]//div[1]//div[3]//input[2]',
            "button_supporting_document_add": '//button[@id="btnAddSupportingDocument"]',
            "pth_bir_form_2303": '//input[@id="birForm2303Filename0"]',
            "date_bir_form_2303_validity": '//div[@id="birForm2303"]//div//div//div[3]//input[2]',
            "pth_sec_certificate": '//input[@id="secCertificateFilename0"]',
            "date_sec_certificate_validity": '//div[@id="secCertificate"]//div//div//div[3]//input[2]',
            "pth_cab_certificate_of_registration": '//input[@id="cabCertificateOfRegistrationFilename0"]',
            "date_cab_certificate_of_registration_validity": '//div[@id="cabCertificateOfRegistration"]//div//div//div[3]//input[2]',
            "pth_dti_certificate_accreditations": '//input[@id="dtiCertificateAccreditationFilename0"]',
            "date_dti_certificate_accreditations_validity": '//div[@id="dtiCertificateAccreditation"]//div//div//div[3]//input[2]',
            "pth_boc_certificate_of_registration": '//input[@id="bocCertificateOfRegistrationFilename0"]',
            "date_boc_certificate_of_registration_validity": '//div[@id="bocCertificateOfRegistration"]//div//div//div[3]//input[2]',
            "pth_pnp_license_to_operate": '//input[@id="pnpLicenseToOperateFilename0"]',
            "date_pnp_license_to_operate_validity": '//div[@id="pnpLicenseToOperate"]//div//div//div[3]//input[2]',
            "pth_dole_department_order": '//input[@id="doleDepartmentOrderFilename0"]',
            "date_dole_department_order_validity": '//div[@id="doleDepartmentOrder"]//div//div//div[3]//input[2]',
            "pth_official_list_of_trucks": '//input[@id="officialListOfTrucksFilename0"]',
            "date_official_list_of_trucks_validity": '//div[@id="officialListOfTrucks"]//div//div//div[3]//input[2]',
            "pth_copy_of_land_transportation": '//input[@id="copyOfLandTransportationFilename0"]',
            "date_copy_of_land_transportation_validity": '//div[@id="copyOfLandTransportation"]//div//div//div[3]//input[2]',
            "pth_copy_of_lto_cr": '//input[@id="copyOfLTOCRFilename0"]',
            "date_copy_of_lto_cr_validity": '//div[@id="copyOfLTOCR"]//div//div//div[3]//input[2]'
        }

        return_element_names = {
            "path_supporting_document_file": '',
            "txt_supporting_document_desc": '',
            "dp_supporting_document_validity": '',
            "button_supporting_document_add": '',
            "pth_bir_form_2303": '',
            "date_bir_form_2303_validity": '',
            "pth_sec_certificate": '',
            "date_sec_certificate_validity": '',
            "pth_cab_certificate_of_registration": '',
            "date_cab_certificate_of_registration_validity": '',
            "pth_dti_certificate_accreditations": '',
            "date_dti_certificate_accreditations_validity": '',
            "pth_boc_certificate_of_registration": '',
            "date_boc_certificate_of_registration_validity": '',
            "pth_pnp_license_to_operate": '',
            "date_pnp_license_to_operate_validity": '',
            "pth_dole_department_order": '',
            "date_dole_department_order_validity": '',
            "pth_official_list_of_trucks": '',
            "date_official_list_of_trucks_validity": '',
            "pth_copy_of_land_transportation": '',
            "date_copy_of_land_transportation_validity": '',
            "pth_copy_of_lto_cr": '',
            "date_copy_of_lto_cr_validity": ''
        }

        return field_elements_locations[get_element], return_element_names[get_element]

    def get_company_information_sup_docs_others(self, get_element):
        dp_supporting_document_validity = [
            '//html//body//div[4]//div[1]//div//div//div//input[@class="numInput cur-year"]',
            '//html//body//div[4]//div[1]//div//div//select[@class="flatpickr-monthDropdown-months"]',
            '//html//body//div[4]//div[2]//div//div[2]//div//span[@class="flatpickr-day" and text()="'
        ]

        date_bir_form_2303_validity = [
            '/html/body/div[4]/div[1]/div/div/div/input[@class="numInput cur-year"]',
            '/html/body/div[4]/div[1]/div/div/select[@class="flatpickr-monthDropdown-months"]',
            '/html/body/div[4]/div[2]/div/div[2]/div/span[@class="flatpickr-day" and text()="'
        ]

        date_sec_certificate_validity = [
            '/html/body/div[5]/div[1]/div/div/div/input[@class="numInput cur-year"]',
            '/html/body/div[5]/div[1]/div/div/select[@class="flatpickr-monthDropdown-months"]',
            '/html/body/div[5]/div[2]/div/div[2]/div/span[@class="flatpickr-day" and text()="'
        ]

        date_cab_certificate_of_registration_validity = [
            '/html/body/div[9]/div[1]/div/div/div/input[@class="numInput cur-year"]',
            '/html/body/div[9]/div[1]/div/div/select[@class="flatpickr-monthDropdown-months"]',
            '/html/body/div[9]/div[2]/div/div[2]/div/span[@class="flatpickr-day" and text()="'

        ]

        date_dti_certificate_accreditations_validity = [
            '/html/body/div[10]/div[1]/div/div/div/input[@class="numInput cur-year"]',
            '/html/body/div[10]/div[1]/div/div/select[@class="flatpickr-monthDropdown-months"]',
            '/html/body/div[10]/div[2]/div/div[2]/div/span[@class="flatpickr-day" and text()="'
        ]

        date_boc_certificate_of_registration_validity = [
            '/html/body/div[11]/div[1]/div/div/div/input[@class="numInput cur-year"]',
            '/html/body/div[11]/div[1]/div/div/select[@class="flatpickr-monthDropdown-months"]',
            '/html/body/div[11]/div[2]/div/div[2]/div/span[@class="flatpickr-day" and text()="'
        ]

        date_pnp_license_to_operate_validity = [
            '/html/body/div[12]/div[1]/div/div/div/input[@class="numInput cur-year"]',
            '/html/body/div[12]/div[1]/div/div/select[@class="flatpickr-monthDropdown-months"]',
            '/html/body/div[12]/div[2]/div/div[2]/div/span[@class="flatpickr-day" and text()="'
        ]

        date_dole_department_order_validity = [
            '/html/body/div[13]/div[1]/div/div/div/input[@class="numInput cur-year"]',
            '/html/body/div[13]/div[1]/div/div/select[@class="flatpickr-monthDropdown-months"]',
            '/html/body/div[13]/div[2]/div/div[2]/div/span[@class="flatpickr-day" and text()="'
        ]

        date_official_list_of_trucks_validity = [
            '/html/body/div[6]/div[1]/div/div/div/input[@class="numInput cur-year"]',
            '/html/body/div[6]/div[1]/div/div/select[@class="flatpickr-monthDropdown-months"]',
            '/html/body/div[6]/div[2]/div/div[2]/div/span[@class="flatpickr-day" and text()="'
        ]

        date_copy_of_land_transportation_validity = [
            '/html/body/div[7]/div[1]/div/div/div/input[@class="numInput cur-year"]',
            '/html/body/div[7]/div[1]/div/div/select[@class="flatpickr-monthDropdown-months"]',
            '/html/body/div[7]/div[2]/div/div[2]/div/span[@class="flatpickr-day" and text()="'
        ]

        date_copy_of_lto_cr_validity = [
            '/html/body/div[8]/div[1]/div/div/div/input[@class="numInput cur-year"]',
            '/html/body/div[8]/div[1]/div/div/select[@class="flatpickr-monthDropdown-months"]',
            '/html/body/div[8]/div[2]/div/div[2]/div/span[@class="flatpickr-day" and text()="'
        ]

        match get_element:
            case 'dp_supporting_document_validity':
                return dp_supporting_document_validity
            case 'date_bir_form_2303_validity':
                return date_bir_form_2303_validity
            case 'date_sec_certificate_validity':
                return date_sec_certificate_validity
            case 'date_cab_certificate_of_registration_validity':
                return date_cab_certificate_of_registration_validity
            case 'date_dti_certificate_accreditations_validity':
                return date_dti_certificate_accreditations_validity
            case 'date_boc_certificate_of_registration_validity':
                return date_boc_certificate_of_registration_validity
            case 'date_pnp_license_to_operate_validity':
                return date_pnp_license_to_operate_validity
            case 'date_dole_department_order_validity':
                return date_dole_department_order_validity
            case 'date_official_list_of_trucks_validity':
                return date_official_list_of_trucks_validity
            case 'date_copy_of_land_transportation_validity':
                return date_copy_of_land_transportation_validity
            case 'date_copy_of_lto_cr_validity':
                return date_copy_of_lto_cr_validity


    def get_company_information(self, get_element):
        field_elements_locations = {
            "option_type_non_peza_service": '//select[@id="serviceTypeId"]',
            "rbutton_company_type": '',
            "txt_company_name": '//input[@id="companyName"]',
            "txt_company_tin": '//input[@id="companyTinNumber"]',
            "option_address_region": '//select[@id="companyRegionId"]',
            "option_address_province": '//select[@id="companyProvinceId"]',
            "option_address_city": '//select[@id="companyCityId"]',
            "option_address_barangay": '//select[@id="companyBarangayId"]',
            "txt_address_street": '//input[@id="companyAddressLine1"]',
            "txt_contact_mobile_num": '//input[@id="companyMobileNumber"]',
            "txt_contact_landline": '//input[@id="companyTelephoneNumber"]',
            "txt_contact_email": '//input[@id="companyEmailAddress"]'
        }

        return_element_names = {
            "option_type_non_peza_service": 'Non-PEZA type of service SELCECT',
            "rbutton_company_type": '',
            "txt_company_name": "Company TIN INPUT",
            "txt_company_tin": "Company NAME INPUT",
            "option_address_region": "Company ADDRESS REGION SELECT",
            "option_address_province": "Company ADDRESS PROVINCE SELECT",
            "option_address_city": "Company ADDRESS CITY SELECT",
            "option_address_barangay": "Company ADDRESS BARANGAY SELECT",
            "txt_address_street": "Company ADDRESS STREET SELECT",
            "txt_contact_mobile_num": "Company CONTACT MOBILE NUMBER INPUT",
            "txt_contact_landline": "Company CONTACT LANDLINE INPUT",
            "txt_contact_email": "Company CONTACT EMAIL INPUT"
        }

        return field_elements_locations[get_element], return_element_names[get_element]

    def get_registration_select(self, get_element):
        field_elements_locations = {
            "rbutton_type_registration": '',
            "button_proceed_select_type": '//button[@id="btn_comp_info"]',
            "rbutton_privacy_policy_accept": '//input[@id="dpCheckbox"]',
            "button_privacy_policy_accept_proceed": '//button[@id="dpSubmit"]'
        }

        return_element_names = {
            "rbutton_type_registration": '',
            "button_proceed_select_type": '',
            "rbutton_privacy_policy_accept": '',
            "button_privacy_policy_accept_proceed": ''
        }

        return field_elements_locations[get_element], return_element_names[get_element]

    def get_company_information_others(self, get_element):
        field_rbutton_company_type = {
            "Sole Proprietorship": '//input[@id="sole_proprietorship"]',
            "Partnership": '//input[@id="partnership"]',
            "Corporation": '//input[@id="corporation"]',
            "Cooperative": '//input[@id="cooperative"]'
        }

        match get_element:
            case 'rbutton_company_type':
                return field_rbutton_company_type

    def get_registration_select_others(self, get_element):
        rbutton_type_registration = {
            "ENTERPRISE": '//input[@name="company.registration_type_id" and @value=1]',
            "DEVELOPER": '//input[@name="company.registration_type_id" and @value=2]',
            "SERVICE PROVIDER": '//input[@name="company.registration_type_id" and @value=3]',
            "OTHERS NON-PEZA": '//input[@name="company.registration_type_id" and @value=4]'
        }

        match get_element:
            case 'rbutton_type_registration':
                return rbutton_type_registration
