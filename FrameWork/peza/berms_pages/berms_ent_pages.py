from FrameWork.config_files.frame_work_base_driver import FrameWorkBaseDriver

class BermsEntpriseElementLocations(FrameWorkBaseDriver):
    def __init__(self, driver):
        self.driver = driver

    def get_berms_ent_pages_confirmation(self, get_element):
        field_elements_locations = {
            "button_confirmation_application_proceed": '//button[@id="btnSubmitApplication"]//span[text()="Submit"]',
            "cbox_modal_acceptance_affidavit": '//input[@id="acceptAffidavit"]',
            "button_modal_acceptance_affidavit_proceed": '//button[@id="affidavitModalSubmit"]',
            "button_swal_acceptance_affidavit_proceed": '//button[1][text()="Yes"]',
            "button_swal_acceptance_affidavit_proceed_confirmation": '//html//body//div[116]//div//div[6]//button[1][text()="OK"]',
            "txt_berms_application_number": '//span[@id="confirmationReferenceNumber"]'
        }

        return_element_names = {
            "button_confirmation_application_proceed": '',
            "cbox_modal_acceptance_affidavit": '',
            "button_modal_acceptance_affidavit_proceed": '',
            "button_swal_acceptance_affidavit_proceed": '',
            "button_swal_acceptance_affidavit_proceed_confirmation": '',
            "txt_berms_application_number": ''
        }

        return field_elements_locations[get_element], return_element_names[get_element]

    def get_berms_ent_pages_application(self, get_element):
        field_elements_locations = {
            "cbox_berms_ent_agree_app_undertaking": '//input[@id="acceptApplicantUndertakings"]',
            "btn_berms_ent_agree_app_undertaking": '//button[@id="btnSubmitUndertaking"]',
            "option_type_enterprise_application": '//select[@id="applicationTypeId"]',
            "rbtn_type_of_enterpirse": '',
            "txt_enterprise_name": '//input[@id="enterpriseName"]',
            "option_psic_section_code": '//select[@name="activity.psic_id"]',
            "option_psic_division_code": '//select[@name="activity.psic_division_code_id"]',
            "option_psic_group_code": '//select[@id="groupCodeId"]',
            "option_psic_classes_code": '//select[@id="classesCodeId"]',
            "option_psic_sub_classes_code": '//select[@id="subClassesCodeId"]',
            "btn_application_proceed": '//div[@id="application"]//div[5]//div//div//button//span[text()="Proceed"]',
            "txt_parent_company_name": '//input[@id="addtlInfocompany_companyName"]',
            "option_parent_company_country": '//select[@id="addtlInfocompany_companyCountryId"]',
            "dp_parent_company_registration_date": '//div[@id="company-info"]//div[2]//div[1]//div[6]//div[3]//input[2]',
            "txt_parent_company_nature_business": '//input[@id="businessNatureName"]',
            "txt_parent_company_profile": '//textarea[@id="businessCompanyProfile"]',
            "txt_official_rep_first_name": '//input[@id="representatives0FirstName"]',
            "txt_official_rep_middle_name": '//input[@id="representatives0MiddleName"]',
            "txt_official_rep_last_name": '//input[@id="representatives0LastName"]',
            "option_official_rep_address_region": '//select[@id="representatives0RegionId"]',
            "option_official_rep_address_province": '//select[@id="representatives0ProvinceId"]',
            "option_official_rep_address_city": '//select[@id="representatives0CityId"]',
            "option_official_rep_address_barangay": '//select[@id="representatives0BarangayId"]',
            "txt_official_rep_address_street_name": '//input[@id="representatives0StreetName"]',
            "txt_official_rep_mobile_num": '//input[@id="representatives0MobileNumber"]',
            "txt_official_rep_land_line": '//input[@id="representatives0telephoneNumber"]',
            "txt_official_rep_email": '//input[@id="representatives0EmailAddress"]',
            "txt_official_rep_website": '//input[@id="representatives0Website"]',
            "button_add_official_respresentative": '//button[@id="btnAddRepresentative"]',
            "txt_official_rep_1_first_name": '//input[@id="representatives1FirstName"]',
            "txt_official_rep_1_middle_name": '//input[@id="representatives1MiddleName"]',
            "txt_official_rep_1_last_name": '//input[@id="representatives1LastName"]',
            "option_official_rep_1_address_region": '//select[@id="representatives1RegionId"]',
            "option_official_rep_1_address_province": '//select[@id="representatives1ProvinceId"]',
            "option_official_rep_1_address_city": '//select[@id="representatives1CityId"]',
            "option_official_rep_1_address_barangay": '//select[@id="representatives1BarangayId"]',
            "txt_official_rep_1_address_street_name": '//input[@id="representatives1StreetName"]',
            "txt_official_rep_1_mobile_num": '//input[@id="representatives1MobileNumber"]',
            "txt_official_rep_1_land_line": '//input[@id="representatives1telephoneNumber"]',
            "txt_official_rep_1_email": '//input[@id="representatives1EmailAddress"]',
            "txt_official_rep_1_website": '//input[@id="representatives1Website"]',
            "btn_company_personal_info_proceed": '//div[@id="company-info"]//div[3]//div//div//button//span[text()="Proceed"]',
            "button_add_business_activity": '//button[@id="btnBusinessProduct"]',
            "text_new_proposed_project_acitivity": '//input[@id="proposedBusinessActivity"]',
            "text_proposed_project_acitivity": '//input[@id="newBusinessProductActivity"]',
            "button_add_business_activity_proceed": '//button[@id="btnSave"]',
            "option_propose_activity": '//select[@id="proposedBusinessActivity"]',
            "txt_propose_activity_desc": '//textarea[@id="description"]',
            "txt_uses_application": '//input[@id="business_prod_service_application"]',
            "drop_propose_process_flow": '//div[@id="activity_product_img_documentsDropzone"]',
            "btn_business_products_proceed": '//div[@id="business-product-activities"]//div[2]//div//div//button//span[text()="Proceed"]'
        }

        return_element_names = {
            "cbox_berms_ent_agree_app_undertaking": 'accept applicants undertaking',
            "btn_berms_ent_agree_app_undertaking": 'proceed applicants undertaking',
            "option_type_enterprise_application": '',
            "rbtn_type_of_enterpirse": '',
            "txt_enterprise_name": 'input enterprise name',
            "option_psic_section_code": 'select psic section',
            "option_psic_division_code": 'select psic division',
            "option_psic_group_code": '',
            "option_psic_classes_code": '',
            "option_psic_sub_classes_code": '',
            "btn_application_proceed": 'click proceed application',
            "txt_parent_company_name": 'parent company name',
            "option_parent_company_country": 'parent company country of origin',
            "dp_parent_company_registration_date": 'parent company registration date',
            "txt_parent_company_nature_business": 'parent company nature of business',
            "txt_parent_company_profile": 'parent company business profile',
            "txt_official_rep_first_name": 'input first name',
            "txt_official_rep_middle_name": 'input middle name',
            "txt_official_rep_last_name": 'input last name',
            "option_official_rep_address_region": 'select address region',
            "option_official_rep_address_province": 'select address province',
            "option_official_rep_address_city": 'select address city',
            "option_official_rep_address_barangay": 'select address barangay',
            "txt_official_rep_address_street_name": 'select address streettr name',
            "txt_official_rep_mobile_num": 'input mobile num',
            "txt_official_rep_land_line": 'input land line',
            "txt_official_rep_email": 'input email',
            "txt_official_rep_website": 'input website',
            "button_add_official_respresentative": '',
            "txt_official_rep_1_first_name": '',
            "txt_official_rep_1_middle_name": '',
            "txt_official_rep_1_last_name": 'input[@id="representatives1LastName"]',
            "option_official_rep_1_address_region": '',
            "option_official_rep_1_address_province": '',
            "option_official_rep_1_address_city": '',
            "option_official_rep_1_address_barangay": '',
            "txt_official_rep_1_address_street_name": '',
            "txt_official_rep_1_mobile_num": '',
            "txt_official_rep_1_land_line": '',
            "txt_official_rep_1_email": '',
            "txt_official_rep_1_website": '',
            "btn_company_personal_info_proceed": 'click proceed company and personal information',
            "button_add_business_activity": '',
            "text_new_proposed_project_acitivity": '',
            "text_proposed_project_acitivity": '',
            "button_add_business_activity_proceed": '',
            "option_propose_activity": 'input proposed activity',
            "txt_propose_activity_desc": 'input description of proposed activity',
            "txt_uses_application": 'input projects uses and application',
            "drop_propose_process_flow": 'drop process flow files',
            "btn_business_products_proceed": 'click proceed business and products activities'
        }

        return field_elements_locations[get_element], return_element_names[get_element]

    def get_application_supporting_documents(self, get_element):
        field_elements_locations = {
            "path_license_to_transact_philippines": '//div[@id="docType_by_law"]//div//div//div[1]//div[1]//div//label//input',
            "dp_license_to_transact_philippines": '//div[@id="docType_by_law"]//div//div//div[3]//div//div[2]//div//input[2]',
            "path_projected_financial_cost": '//div[@id="docType_pfs"]//div//div//div[1]//div[1]//div//label//input',
            "dp_projected_financial_cost_validity": '//div[@id="docType_pfs"]//div//div//div[3]//div//div[2]//div//input[2]',
            "path_notarized_secretary_certificate": '//div[@id="docType_sec_cert"]//div//div//div[1]//div[1]//div//label//input',
            "dp_notarized_secretary_certificate": '//div[@id="docType_sec_cert"]//div//div//div[3]//div//div[2]//div//input[2]',
            "path_notarized_affidavit_option": '//div[@id="docType_nao"]//div//div//div[1]//div[1]//div//label//input',
            "dp_notarized_affidavit_option": '//div[@id="docType_nao"]//div//div//div[3]//div//div[2]//div//input[2]',
            "path_notarized_applicant_undertaking": '//div[@id="docType_und"]//div//div//div[1]//div[1]//div//label//input',
            "dp_notarized_applicant_undertaking": '//div[@id="docType_und"]//div//div//div[3]//div//div[2]//div//input[2]',
            "path_articles_incorporation": '//div[@id="docType_aoi"]//div//div//div[1]//div[1]//div//label//input',
            "dp_articles_incorporation": '//div[@id="docType_aoi"]//div//div//div[3]//div//div[2]//div//input[2]',
            "path_notarized_anti_graft": '//div[@id="docType_aua"]//div//div//div[1]//div[1]//div//label//input',
            "dp_notarized_anti_graft": '//div[@id="docType_aua"]//div//div//div[3]//div//div[2]//div//input[2]',
            "path_general_information_sheet": '//div[@id="docType_gis"]//div//div//div[1]//div[1]//div//label//input',
            "dp_general_information_sheet": '//div[@id="docType_gis"]//div//div//div[3]//div//div[2]//div//input[2]',
            "path_bir_2303": '//div[@id="docType_bir"]//div//div//div[1]//div[1]//div//label//input',
            "dp_bir_2303_validity": '//div[@id="docType_bir"]//div//div//div[3]//div//div[2]//div//input[2]',
            "path_company_profile": '//div[@id="docType_cppc"]//div//div//div[1]//div[1]//div//label//input',
            "dp_company_profile_validity": '//div[@id="docType_cppc"]//div//div//div[3]//div//div[2]//div//input[2]',
            "path_resume_biodata_officer": '//div[@id="docType_rbpo"]//div//div//div[1]//div[1]//div//label//input',
            "dp_resume_biodata_officer_validity": '//div[@id="docType_rbpo"]//div//div//div[3]//div//div[2]//div//input[2]',
            "path_certificate_sec": '//div[@id="docType_crsec"]//div//div//div[1]//div[1]//div//label//input',
            "dp_certificate_sec_validity": '//div[@id="docType_crsec"]//div//div//div[3]//div//div[2]//div//input[2]',
            "path_photo_final_product": '//div[@id="docType_pfp"]//div//div//div[1]//div[1]//div//label//input',
            "dp_photo_final_product_validity": '//div[@id="docType_pfp"]//div//div//div[3]//div//div[2]//div//input[2]',
            # not yet aligned
            "main_menu_access": '//span[text()="Supporting Docs"]',
            "path_certificate_sole_propreitor": '//input[@id="supportingDocFilename1"]',
            "dp_certificate_sole_propreitor_validity": '//div[@id="suppDocWrapper_crsp"]//div[3]//div//div[2]//div//input[2]',
            "path_notarized_accomplished_application": '//input[@id="supportingDocFilename14"]',
            "dp_notarized_accomplished_application": '//div[@id="suppDocWrapper_daa"]//div[3]//div//div[2]//div//input[2]',
            "path_financial_statements_income_tax_returns": '//input[@id="supportingDocFilename16"]',
            "dp_financial_statements_income_tax_returns": '//div[@id="suppDocWrapper_financial_statement"]//div[3]//div//div[2]//div//input[2]',
            "path_export_sales_and_employment": '//input[@id="supportingDocFilename17"]',
            "dp_export_sales_and_employment": '//div[@id="suppDocWrapper_sum_exp"]//div[3]//div//div[2]//div//input[2]',
            "btn_supporting_documents_proceed": '//div[@id="supporting-documents"]//div[3]//div//div//button//span[text()="Proceed"]'
        }

        return_element_names = {
        }
        return field_elements_locations[get_element], ''

    def get_application_supporting_documents_locations(self, get_element):

        field_application_sup_docs_locations_sec = [
            '//html//body//div[5]//div[1]//div//div//div//input[@class="numInput cur-year"]',
            '//html//body//div[5]//div[1]//div//div//select[@class="flatpickr-monthDropdown-months"]',
            '//html//body//div[5]//div[2]//div//div[2]//div/span[@class="flatpickr-day" and text()="'
        ]

        field_application_sup_docs_locations_sole_propreitor = [
            '//html//body//div[6]//div[1]//div//div//div//input[@class="numInput cur-year"]',
            '//html//body//div[6]//div[1]//div//div//select[@class="flatpickr-monthDropdown-months"]',
            '//html//body//div[6]//div[2]//div//div[2]//div/span[@class="flatpickr-day" and text()="'
        ]

        field_application_sup_docs_locations_resume_biodata_officer = [
            '//html//body//div[7]//div[1]//div//div//div//input[@class="numInput cur-year"]',
            '//html//body//div[7]//div[1]//div//div//select[@class="flatpickr-monthDropdown-months"]',
            '//html//body//div[7]//div[2]//div//div[2]//div/span[@class="flatpickr-day" and text()="'
        ]

        field_application_sup_docs_locations_company_profile_old = [
            '//html//body//div[8]//div[1]//div//div//div//input[@class="numInput cur-year"]',
            '//html//body//div[8]//div[1]//div//div//select[@class="flatpickr-monthDropdown-months"]',
            '//html//body//div[8]//div[2]//div//div[2]//div/span[@class="flatpickr-day" and text()="'
        ]

        field_application_sup_docs_locations_bir_2303 = [
            '//html//body//div[9]//div[1]//div//div//div//input[@class="numInput cur-year"]',
            '//html//body//div[9]//div[1]//div//div//select[@class="flatpickr-monthDropdown-months"]',
            '//html//body//div[9]//div[2]//div//div[2]//div/span[@class="flatpickr-day" and text()="'
        ]

        field_application_sup_docs_projected_financial_statement = [
            '//html//body//div[10]//div[1]//div//div//div//input[@class="numInput cur-year"]',
            '//html//body//div[10]//div[1]//div//div//select[@class="flatpickr-monthDropdown-months"]',
            '//html//body//div[10]//div[2]//div//div[2]//div/span[@class="flatpickr-day" and text()="'
        ]

        dp_license_to_transact_philippines = [
            '//div[@class="flatpickr-calendar animate open arrowTop arrowLeft"]//div[1]//div//div//div//input[@class="numInput cur-year"]',
            '//div[@class="flatpickr-calendar animate open arrowTop arrowLeft"]//div[1]//div//div//select[@class="flatpickr-monthDropdown-months"]',
            '//div[@class="flatpickr-calendar animate open arrowTop arrowLeft"]//div[2]//div//div[2]//div/span[@class="flatpickr-day" and text()="'
        ]

        dp_general_information_sheet = [
            '//html//body//div[16]//div[1]//div//div//div//input[@class="numInput cur-year"]',
            '//html//body//div[16]//div[1]//div//div//select[@class="flatpickr-monthDropdown-months"]',
            '//html//body//div[16]//div[2]//div//div[2]//div/span[@class="flatpickr-day" and text()="'
        ]

        dp_notarized_anti_graft = [
            '//html//body//div[17]//div[1]//div//div//div//input[@class="numInput cur-year"]',
            '//html//body//div[17]//div[1]//div//div//select[@class="flatpickr-monthDropdown-months"]',
            '//html//body//div[17]//div[2]//div//div[2]//div/span[@class="flatpickr-day" and text()="'
        ]

        dp_notarized_applicant_undertaking = [
            '//html//body//div[18]//div[1]//div//div//div//input[@class="numInput cur-year"]',
            '//html//body//div[18]//div[1]//div//div//select[@class="flatpickr-monthDropdown-months"]',
            '//html//body//div[18]//div[2]//div//div[2]//div/span[@class="flatpickr-day" and text()="'
        ]

        dp_notarized_accomplished_application =[
            '//html//body//div[19]//div[1]//div//div//div//input[@class="numInput cur-year"]',
            '//html//body//div[19]//div[1]//div//div//select[@class="flatpickr-monthDropdown-months"]',
            '//html//body//div[19]//div[2]//div//div[2]//div/span[@class="flatpickr-day" and text()="'
        ]

        dp_notarized_affidavit_option = [
            '//html//body//div[20]//div[1]//div//div//div//input[@class="numInput cur-year"]',
            '//html//body//div[20]//div[1]//div//div//select[@class="flatpickr-monthDropdown-months"]',
            '//html//body//div[20]//div[2]//div//div[2]//div/span[@class="flatpickr-day" and text()="'
        ]

        dp_financial_statements_income_tax_returns = [
            '//html//body//div[21]//div[1]//div//div//div//input[@class="numInput cur-year"]',
            '//html//body//div[21]//div[1]//div//div//select[@class="flatpickr-monthDropdown-months"]',
            '//html//body//div[21]//div[2]//div//div[2]//div/span[@class="flatpickr-day" and text()="'
        ]

        dp_export_sales_and_employment = [
            '//html//body//div[22]//div[1]//div//div//div//input[@class="numInput cur-year"]',
            '//html//body//div[22]//div[1]//div//div//select[@class="flatpickr-monthDropdown-months"]',
            '//html//body//div[22]//div[2]//div//div[2]//div/span[@class="flatpickr-day" and text()="'
        ]

        dp_notarized_secretary_certificate = [
            '//html//body//div[23]//div[1]//div//div//div//input[@class="numInput cur-year"]',
            '//html//body//div[23]//div[1]//div//div//select[@class="flatpickr-monthDropdown-months"]',
            '//html//body//div[23]//div[2]//div//div[2]//div/span[@class="flatpickr-day" and text()="'
        ]

        dp_articles_incorporation = [
            '//html//body//div[14]//div[1]//div//div//div//input[@class="numInput cur-year"]',
            '//html//body//div[14]//div[1]//div//div//select[@class="flatpickr-monthDropdown-months"]',
            '//html//body//div[14]//div[2]//div//div[2]//div/span[@class="flatpickr-day" and text()="'
        ]

        date_picker_general_locations = [
            '//div[contains(@class,"open")]//div[1]//div//div//div//input[@class="numInput cur-year"]',
            '//div[contains(@class,"open")]//div[1]//div//div//select[@class="flatpickr-monthDropdown-months"]',
            '//div[contains(@class,"open")]//div[2]//div//div[2]//div/span[@class="flatpickr-day" and text()="'
        ]

        match get_element:
            case 'dp_license_to_transact_philippines':
                return date_picker_general_locations
            case 'dp_projected_financial_cost_validity':
                return date_picker_general_locations
            case 'dp_notarized_secretary_certificate':
                return date_picker_general_locations
            case 'dp_notarized_affidavit_option':
                return date_picker_general_locations
            case 'dp_notarized_applicant_undertaking':
                return date_picker_general_locations
            case 'dp_articles_incorporation':
                return date_picker_general_locations
            case 'dp_notarized_anti_graft':
                return date_picker_general_locations
            case 'dp_general_information_sheet':
                return date_picker_general_locations
            case 'dp_bir_2303_validity':
                return date_picker_general_locations
            case 'dp_company_profile_validity':
                return date_picker_general_locations
            case 'dp_resume_biodata_officer_validity':
                return date_picker_general_locations
            case 'dp_certificate_sec_validity':
                return date_picker_general_locations
            case 'dp_photo_final_product_validity':
                return date_picker_general_locations
            # aligned
            case 'dp_certificate_sole_propreitor_validity':
                return field_application_sup_docs_locations_sole_propreitor
            case 'dp_notarized_accomplished_application':
                return dp_notarized_accomplished_application
            case 'dp_financial_statements_income_tax_returns':
                return dp_financial_statements_income_tax_returns
            case 'dp_export_sales_and_employment':
                return dp_export_sales_and_employment
            case _:
                return 0, 'Location not found'

    def get_application_project_cost_financing(self, get_element):
        field_elements_locations = {
            "main_menu_access": '//div[@id="berms-application"]//div//div[1]//div[21]//button//span[2]//span',
            "txt_building_construction": '//div[@id="project-cost-and-source-of-financing"]//div[2]//table//tbody//tr[1]//td[2]//input',
            "txt_machinery_equipment": '//div[@id="project-cost-and-source-of-financing"]//div[2]//table//tbody//tr[2]//td[2]//input',
            "txt_factory_tools": '//div[@id="project-cost-and-source-of-financing"]//div[2]//table//tbody//tr[3]//td[2]//input',
            "txt_transportation": '//div[@id="project-cost-and-source-of-financing"]//div[2]//table//tbody//tr[4]//td[2]//input',
            "txt_office_furniture": '//div[@id="project-cost-and-source-of-financing"]//div[2]//table//tbody//tr[5]//td[2]//input',
            "txt_other_assets": '//div[@id="project-cost-and-source-of-financing"]//div[2]//table//tbody//tr[6]//td[2]//input',
            "txt_pre_opening_expenses": '//div[@id="project-cost-and-source-of-financing"]//div[2]//table//tbody//tr[7]//td[2]//input',
            "txt_working_capital": '//div[@id="project-cost-and-source-of-financing"]//div[2]//table//tbody//tr[8]//td[2]//input',
            "txt_equity": '//table[@id="dt_fundSource"]//tbody//tr[1]//td[3]//input[3]',''
            "txt_additional_entry": '//table[@id="dt_fundSource"]//tbody//tr[2]//td[3]//input[3]',
            "txt_advances": '//table[@id="dt_fundSource"]//tbody//tr[3]//td[3]//input[3]',
            "option_advances_loan_type": '//select[@id="fundSource2"]',
            "txt_loans": '//table[@id="dt_fundSource"]//tbody/tr[4]//td[3]//input[3]',
            "option_loans_loan_type": '//select[@id="fundSource3"]',
            "btn_project_cost_source_proceed": '//div[@id="project-cost-and-source-of-financing"]//div[5]//div//div//button'
        }

        return_element_names = {
            "txt_building_construction": '',
            "txt_machinery_equipment": '',
            "txt_factory_tools": '',
            "txt_transportation": '',
            "txt_office_furniture": '',
            "txt_other_assets": '',
            "txt_pre_opening_expenses": '',
            "txt_working_capital": ''
        }

        return field_elements_locations[get_element], ''

    def get_application_market_aspect(self, get_element):
        field_elements_locations = {
            "main_menu_access": '//div[@id="berms-application"]//div//div[1]//div[19]//button//span[2]//span',
            "option_market_aspect_export": '//select[@id="exportPercent"]',
            "option_market_aspect_domestic": '//select[@id="importPercent"]',
            "option_country_of_export_market": '//select[@id="exportMarketCountryId"]',
            "txt_domestic_clients": '//div[@id="market-aspect"]//div[2]//div[1]//div[2]//div[2]//div[2]//tags//span',
            "txt_export_selling_price_unit_usd": '//input[@id="export_selling_price"]',
            "txt_domestic_selling_price_unit_php": '//input[@id="domestic_selling_price"]',
            "option_projected_volume_sales_value_uom": '//select[@id="projected_volume_sales_id"]',
            "btn_market_aspect_export_add": '//button[@id="btnAddMarketAspectExport" and text()="Add Export"]',
            "option_market_aspect_export_year": '//select[@name="projMarketAspectExport[0].year_no"]',
            "txt_market_aspect_export_volume": '//input[@name="projMarketAspectExport[0].volume_value"]',
            "txt_market_aspect_export_value": '//input[@name="projMarketAspectExport[0].us_value"]',
            "option_market_aspect_1_export_year": '//select[@name="projMarketAspectExport[1].year_no"]',
            "txt_market_aspect_1_export_volume": '//input[@name="projMarketAspectExport[1].volume_value"]',
            "txt_market_aspect_1_export_value": '//input[@name="projMarketAspectExport[1].us_value"]',
            "option_market_aspect_2_export_year": '//select[@name="projMarketAspectExport[2].year_no"]',
            "txt_market_aspect_2_export_volume": '//input[@name="projMarketAspectExport[2].volume_value"]',
            "txt_market_aspect_2_export_value": '//input[@name="projMarketAspectExport[2].us_value"]',
            "btn_market_aspect_local_add": '//button[@id="btnAddMarketAspectImport" and text()="Add Local"]',
            "option_market_aspect_local_year": '//select[@name="projMarketAspectImport[0].year_no"]',
            "txt_market_aspect_local_volume": '//input[@name="projMarketAspectImport[0].volume_value"]',
            "txt_market_aspect_local_value": '//input[@name="projMarketAspectImport[0].us_value"]',
            "option_market_aspect_1_local_year": '//select[@name="projMarketAspectImport[1].year_no"]',
            "txt_market_aspect_1_local_volume": '//input[@name="projMarketAspectImport[1].volume_value"]',
            "txt_market_aspect_1_local_value": '//input[@name="projMarketAspectImport[1].us_value"]',
            "option_market_aspect_2_local_year": '//select[@name="projMarketAspectImport[2].year_no"]',
            "txt_market_aspect_2_local_volume": '//input[@name="projMarketAspectImport[2].volume_value"]',
            "txt_market_aspect_2_local_value": '//input[@name="projMarketAspectImport[2].us_value"]',
            "btn_market_aspect_proceed": '//div[@id="market-aspect"]/div[3]/div/div/button/span[text()="Proceed"]'
        }

        return_element_names = {
            "main_menu_access": '',
            "option_market_aspect_export": '',
            "option_market_aspect_domestic": '',
            "option_country_of_export_market": '',
            "txt_domestic_clients": '',
            "txt_export_selling_price_unit_usd": '',
            "txt_domestic_selling_price_unit_php": '',
            "option_projected_volume_sales_value_uom": '',
            "btn_market_aspect_export_add": '',
            "option_market_aspect_export_year": '',
            "txt_market_aspect_export_volume": '',
            "txt_market_aspect_export_value": '',
            "option_market_aspect_1_export_year": '',
            "txt_market_aspect_1_export_volume": '',
            "txt_market_aspect_1_export_value": '',
            "option_market_aspect_2_export_year": '',
            "txt_market_aspect_2_export_volume": '',
            "txt_market_aspect_2_export_value": '',
            "btn_market_aspect_local_add": '',
            "option_market_aspect_local_year": '',
            "txt_market_aspect_local_volume": '',
            "txt_market_aspect_local_value": '',
            "option_market_aspect_1_local_year": '',
            "txt_market_aspect_1_local_volume": '',
            "txt_market_aspect_1_local_value": '',
            "option_market_aspect_2_local_year": '',
            "txt_market_aspect_2_local_volume": '',
            "txt_market_aspect_2_local_value": '',
            "btn_market_aspect_proceed": ''
        }

        return field_elements_locations[get_element], return_element_names[get_element]

    def get_application_area_utilities_waste_disposal(self, get_element):
        field_elements_locations = {
            "txt_existing_floor_area": '//input[@id="floor_area_sqm"]',
            "txt_area": '//input[@id="total_area_sqm"]',
            "option_location_zone_it_building": '//select[@id="zoneId"]',
            "txt_owner_building_first_name": '//input[@id="unitOwnerFirstname"]',
            "txt_owner_building_middle_name": '//input[@id="unitOwnerMiddlename"]',
            "txt_owner_building_last_name": '//input[@id="unitOwnerLastname"]',
            "txt_owner_lot_first_name": '//input[@id="lotOwnerFirstname"]',
            "txt_owner_lot_middle_name": '//input[@id="lotOwnerMiddlename"]',
            "txt_owner_lot_last_name": '//input[@id="lotOwnerLastname"]',
            "txt_lessor_lot_first_name": '//input[@id="lessorFirstname"]',
            "txt_lessor_lot_middle_name": '//input[@id="lessorMiddlename"]',
            "txt_lessor_lot_last_name": '//input[@id="lessorLastname"]',
            "txt_utilities_requirement_water": '//input[@id="water_yr_req"]',
            "txt_utilities_requirement_electricty": '//input[@id="electric_yr_req"]',
            "txt_area_description_waste_prodcuts": '//textarea[@id="waste_disposal_desc"]',
            "drop_area_description_waste_prodcuts": '//div[@id="activity_wasteproducts_supporting_documentsDropzone"]',
            "txt_area_methods_treatment_disposal": '//textarea[@id="waste_disposal_method_desc"]',
            "drop_area_methods_treatment_disposal": '//div[@id="activity_generatedwaste_supporting_documentsDropzone"]',
            "btn_area_utilities_waste_disposal_proceed": '//div[@id="area-disposable-waste-disposal"]/div[7]/div/div/button/span'
        }

        return_element_names = {
            "txt_existing_floor_area": '',
            "txt_area": '',
            "option_location_zone_it_building": '',
            "txt_owner_building_first_name": '',
            "txt_owner_building_middle_name": '',
            "txt_owner_building_last_name": '',
            "txt_owner_lot_first_name": '',
            "txt_owner_lot_middle_name": '',
            "txt_owner_lot_last_name": '',
            "txt_lessor_lot_first_name": '',
            "txt_lessor_lot_middle_name": '',
            "txt_lessor_lot_last_name": '',
            "txt_utilities_requirement_water": '',
            "txt_utilities_requirement_electricty": '',
            "txt_area_description_waste_prodcuts": '',
            "drop_area_description_waste_prodcuts": '',
            "txt_area_methods_treatment_disposal": '',
            "drop_area_methods_treatment_disposal": '',
            "btn_area_utilities_waste_disposal_proceed": ''
        }

        return field_elements_locations[get_element], return_element_names[get_element]

    def get_application_machinery_production_schedule(self, get_element):
        field_elements_locations = {
            "btn_add_machinery_equipment_list": '//button[@id="btnAddMachineryEquipment"]',
            "txt_machinery_equipment_list_item_description": '//input[@name="equipments[0].item_descripition"]',
            "txt_machinery_equipment_list_quantity": '//input[@id="itemQty0"]',
            "txt_machinery_equipment_list_cost": '//input[@id="itemUnitCost0"]',
            "option_machinery_equipment_list_source": '//select[@id="itemSource0"]',
            "option_machinery_equipment_list_source_country": '//select[@id="origin0"]',
            "txt_production_schedule_no_shifts": '//input[@id="prodSchedShifts0"]',
            "txt_production_schedule_hours_shifts": '//input[@id="prodSchedHourShifts0"]',
            "txt_production_schedule_operating_days": '//input[@id="prodSchedDaysMonth0"]',
            "btn_mahicnery_production_schedule_proceed": '//div[@id="machinery-and-production-schedule"]//div[6]//div//div//button//span[text()="Proceed"]'
        }

        return_element_names = {
            "btn_add_machinery_equipment_list": '',
            "txt_machinery_equipment_list_item_description": '',
            "txt_machinery_equipment_list_quantity": '',
            "txt_machinery_equipment_list_cost": '',
            "option_machinery_equipment_list_source": '',
            "option_machinery_equipment_list_source_country": '',
            "txt_production_schedule_no_shifts": '',
            "txt_production_schedule_hours_shifts": '',
            "txt_production_schedule_operating_days": '',
            "btn_mahicnery_production_schedule_proceed": ''
        }

        return field_elements_locations[get_element], return_element_names[get_element]

    def get_application_manufacturing_process_service_flow(self, get_element):
        field_elements_locations = {
            "txt_area_process_service_flow": '//textarea[@id="manufacturing_process_service_flow_id"]',
            "drop_process_service_flow_diagram_image": '//div[@id="addtlInfo_supporting_documentsDropzone"]',
            "switch_add_process_to_subcontracted": '//input[@id="hasSubcontracted"]',
            "txt_sub_contractor_activity": '//input[@id="subcontractorActivity0"]',
            "txt_sub_contrator_name": '//input[@id="subcontractorName0"]',
            "btn_manufacturing_process_service_flow_proceed": '//div[@id="manufacturing-process-and-service-flow"]//div[6]//div//div//button//span[text()="Proceed"]'
        }

        return_element_names = {
            "txt_area_process_service_flow": '',
            "drop_process_service_flow_diagram_image": '',
            "switch_add_process_to_subcontracted": '',
            "txt_sub_contractor_activity": '',
            "txt_sub_contrator_name": '',
            "btn_manufacturing_process_service_flow_proceed": ''
        }

        return field_elements_locations[get_element], return_element_names[get_element]

    def get_application_manpower_timetable(self, get_element):
        field_elements_locations = {
            "main_menu_access": '//div[@id="berms-application"]//div//div[1]//div[11]//button//span[2]//span[text()="Manpower & Timetable"]',
            "option_manpower_requirement_year": '//select[@id="manpowerYear0"]',
            "txt_manpower_requirement_service_personnel": '//input[@id="servicePersonnelCount0"]',
            "txt_manpower_requirement_indirect_service": '//input[@id="indirectPersonnelCount0"]',
            "txt_manpower_requirement_admin_personnel": '//input[@id="adminPersonnelCount0"]',
            "dp_applicants_manpower_timetable_building_from": '//div[@id="manpower-and-timetable"]//div[2]//div[1]//div[1]//div//div//div[2]//div[1]//input[2]',
            "dp_applicants_manpower_timetable_building_to": '//div[@id="manpower-and-timetable"]//div[2]//div[1]//div[1]//div//div//div[2]//div[2]//input[2]',
            "dp_applicants_manpower_timetable_importation_from": '//div[@id="manpower-and-timetable"]//div[2]//div[1]//div[2]//div//div//div[2]//div[1]/input[2]',
            "dp_applicants_manpower_timetable_importation_to": '//div[@id="manpower-and-timetable"]//div[2]//div[1]//div[2]//div//div//div[2]//div[2]/input[2]',
            "dp_applicants_manpower_timetable_installation_from": '//div[@id="manpower-and-timetable"]//div[2]//div[2]//div[1]//div//div//div[2]//div[1]//input[2]',
            "dp_applicants_manpower_timetable_installation_to": '//div[@id="manpower-and-timetable"]//div[2]//div[2]//div[1]//div//div//div[2]//div[2]//input[2]',
            "dp_applicants_manpower_timetable_hiring_from": '//div[@id="manpower-and-timetable"]//div[2]//div[2]//div[2]//div//div//div[2]//div[1]//input[2]',
            "dp_applicants_manpower_timetable_hiring_to": '//div[@id="manpower-and-timetable"]//div[2]//div[2]//div[2]//div//div//div[2]//div[2]//input[2]',
            "dp_applicants_manpower_timetable_start_from": '//div[@id="manpower-and-timetable"]//div[2]//div[3]//div//div//div//div[2]//div//input[2]',
            "dp_applicants_manpower_timetable_start_to": '//input[@id="timetableProjCommercialOperationsTo"]',
            "btn_manpower_timetable_proceed": '//div[@id="manpower-and-timetable"]//div[6]//div//div//button//span[text()="Proceed"]'
        }

        return_element_names = {
            "main_menu_access": '',
            "option_manpower_requirement_year": '',
            "txt_manpower_requirement_service_personnel": '',
            "txt_manpower_requirement_indirect_service": '',
            "txt_manpower_requirement_admin_personnel": '',
            "dp_applicants_manpower_timetable_building_from": '',
            "dp_applicants_manpower_timetable_building_to": '',
            "dp_applicants_manpower_timetable_importation_from": '',
            "dp_applicants_manpower_timetable_importation_to": '',
            "dp_applicants_manpower_timetable_installation_from": '',
            "dp_applicants_manpower_timetable_installation_to": '',
            "dp_applicants_manpower_timetable_hiring_from": '',
            "dp_applicants_manpower_timetable_hiring_to": '',
            "dp_applicants_manpower_timetable_start_from": '',
            "dp_applicants_manpower_timetable_start_to": '',
            "btn_manpower_timetable_proceed": ''
        }

        return field_elements_locations[get_element], return_element_names[get_element]

    def get_application_information(self, get_element):
        return self.field_berms_ent_application[get_element], self.return_berms_ent_application[get_element]

    def get_application_exi_bus_reg(self, get_element):
        field_berms_ent_application_exi_bus_reg = {
            "txt_applicants_existing_business_registration_office": '//input[@id="govtOfficeName"]',
            "dp_applicants_existing_business_registration_date": '//div[@id="existing-business-registration"]//div[2]//div[2]//input[2]',
            "txt_applicants_existing_business_registration_registration_no": '//input[@id="registration_no"]',
            "txt_applicants_existing_business_registration_sec_primary_purpose": '//input[@id="secPrimaryPurpose"]',
            "txt_capital_structure_auth_amount": '//input[@id="authorizedAmount"]',
            "txt_capital_structure_subs_amount": '//input[@id="subscribeAmount"]',
            "txt_capital_structure_paid_up_amount": '//input[@id="paidUpAmount"]',
            "btn_capital_structure_proceed": '//div[@id="existing-business-registration"]//div[3]//div//div//button//span[text()="Proceed"]'
        }

        return_berms_ent_application_exi_bus_reg = {
            "txt_applicants_existing_business_registration_office": 'input existing office',
            "dp_applicants_existing_business_registration_date": 'input existing registration ate',
            "txt_applicants_existing_business_registration_registration_no": 'input existing registration number',
            "txt_applicants_existing_business_registration_sec_primary_purpose": 'input existing primary purpose',
            "txt_capital_structure_auth_amount": 'input authorized amount',
            "txt_capital_structure_subs_amount": 'input subscribed amount',
            "txt_capital_structure_paid_up_amount": 'input paid-up amount',
            "btn_capital_structure_proceed": 'click proceed capital structure'
        }

        return field_berms_ent_application_exi_bus_reg[get_element], return_berms_ent_application_exi_bus_reg[get_element]

    def get_stockholders_principal_officers(self, get_element):
        field_elements_locations = {
            "btn_add_list_of_proposed_stockholders": '//div[@id="dt_stockholders_wrapper"]//div[3]//div[2]//button[@title="Add Stockholder"]',
            "txt_add_stockholder_first_name": '//input[@id="proposedStockholderFirstName"]',
            "txt_add_stockholder_middle_name": '//input[@id="proposedStockholderMiddleName"]',
            "txt_add_stockholder_last_name": '//input[@id="proposedStockholderLastName"]',
            "option_add_stockholder_nationality": '//select[@id="proposedStockholderNationalityId"]',
            "txt_add_stockholder_number_shares": '//input[@id="proposedStockholderNumberOfShares"]',
            "txt_add_stockholder_amount_subscribe": '//input[@id="proposedStockholderSubscribeAmt"]',
            "txt_add_stockbolder_amount_paid": '//input[@id="proposedStockholderPaidupAmt"]',
            "btn_add_list_of_proposed_stockholders_proceed": '//button[@id="btnAddStockholder"]',
            "btn_add_principal_officer": '//div[@id="dt_principalOfficers_wrapper"]/div[3]/div[2]/button[@title="Add Principal Officer"]',
            "rbtn_if_applicable_other_peza_stockholder": '',
            "txt_add_principal_officer_first_name": '//input[@id="officerFirstName"]',
            "txt_add_principal_officer_middle_name": '//input[@id="officerMiddleName"]',
            "txt_add_principal_officer_last_name": '//input[@id="officerLastName"]',
            "option_add_principal_officer_nationality": '//select[@id="officerNationalityId"]',
            "txt_add_principal_officer_position": '//input[@id="officerPosition"]',
            "btn_add_principal_officer_proceed": '//button[@id="btnAddPrincipalOfficer"]',
            "btn_stockholders_principa_officers_proceed": '//div[@id="stockholders-and-principles"]//div[5]//div//div//button//span[text()="Proceed"]'
        }

        return_element_names = {
            "btn_add_list_of_proposed_stockholders": '',
            "txt_add_stockholder_first_name": '',
            "txt_add_stockholder_middle_name": '',
            "txt_add_stockholder_last_name": '',
            "option_add_stockholder_nationality": '',
            "txt_add_stockholder_number_shares": '',
            "txt_add_stockholder_amount_subscribe": '',
            "txt_add_stockbolder_amount_paid": '',
            "btn_add_list_of_proposed_stockholders_proceed": '',
            "btn_add_principal_officer": '',
            "rbtn_if_applicable_other_peza_stockholder": '',
            "txt_add_principal_officer_first_name": '',
            "txt_add_principal_officer_middle_name": '',
            "txt_add_principal_officer_last_name": '',
            "option_add_principal_officer_nationality": '',
            "txt_add_principal_officer_position": '',
            "btn_add_principal_officer_proceed": '',
            "btn_stockholders_principa_officers_proceed": ''
        }

        return field_elements_locations[get_element], return_element_names[get_element]

    def get_application_other_locations(self, get_element):

        field_berms_ent_application_exi_bus_reg_date = [
            '//html//body//div[4]//div[1]//div//div//div//input[@class="numInput cur-year"]',
            '//html//body//div[4]//div[1]//div//div//select[@class="flatpickr-monthDropdown-months"]',
            '//html//body//div[4]//div[2]//div//div[2]//div//span[@class="flatpickr-day" and text()="'
        ]

        field_berms_ent_application_manpower_timetable_building_from = [
            '//html//body//div[5]//div[1]//div//div//div//input[@class="numInput cur-year"]',
            '//html//body//div[5]//div[1]//div//div//select[@class="flatpickr-monthDropdown-months"]',
            '//html//body//div[5]//div[2]//div//div[2]//div//span[@class="flatpickr-day" and text()="'
        ]

        field_berms_ent_application_manpower_timetable_building_to = [
            '//html//body//div[43]//div[1]//div//div//div//input[@class="numInput cur-year"]',
            '//html//body//div[43]//div[1]//div//div//select[@class="flatpickr-monthDropdown-months"]',
            '//html//body//div[43]//div[2]//div//div[2]//div//span[@class="flatpickr-day" and text()="'
        ]

        field_berms_ent_application_manpower_timetable_importation_from = [
            '//html//body//div[39]//div[1]//div//div//div//input[@class="numInput cur-year"]',
            '//html//body//div[39]//div[1]//div//div//select[@class="flatpickr-monthDropdown-months"]',
            '//html//body//div[39]//div[2]//div//div[2]//div//span[@class="flatpickr-day" and text()="'
        ]

        field_berms_ent_application_manpower_timetable_importation_to = [
            '//html//body//div[61]//div[1]//div//div//div//input[@class="numInput cur-year"]',
            '//html//body//div[61]//div[1]//div//div//select[@class="flatpickr-monthDropdown-months"]',
            '//html//body//div[61]//div[2]//div//div[2]//div//span[@class="flatpickr-day" and text()="'
        ]

        field_berms_ent_application_manpower_timetable_installation_from = [
            '//html//body//div[61]//div[1]//div//div//div//input[@class="numInput cur-year"]',
            '//html//body//div[61]//div[1]//div//div//select[@class="flatpickr-monthDropdown-months"]',
            '//html//body//div[61]//div[2]//div//div[2]//div//span[@class="flatpickr-day" and text()="'
        ]

        field_berms_ent_application_manpower_timetable_installation_to = [
            '//html//body//div[79]//div[1]//div//div//div//input[@class="numInput cur-year"]',
            '//html//body//div[79]//div[1]//div//div//select[@class="flatpickr-monthDropdown-months"]',
            '//html//body//div[79]//div[2]//div//div[2]//div//span[@class="flatpickr-day" and text()="'
        ]

        field_berms_ent_application_manpower_timetable_hiring_from = [
            '//html//body//div[83]//div[1]//div//div//div//input[@class="numInput cur-year"]',
            '//html//body//div[83]//div[1]//div//div//select[@class="flatpickr-monthDropdown-months"]',
            '//html//body//div[83]//div[2]//div//div[2]//div//span[@class="flatpickr-day" and text()="'
        ]

        field_berms_ent_application_manpower_timetable_hiring_to = [
            '//html//body//div[97]//div[1]//div//div//div//input[@class="numInput cur-year"]',
            '//html//body//div[97]//div[1]//div//div//select[@class="flatpickr-monthDropdown-months"]',
            '//html//body//div[97]//div[2]//div//div[2]//div//span[@class="flatpickr-day" and text()="'
        ]

        field_berms_ent_application_manpower_timetable_start_from = [
            '//html//body//div[105]//div[1]//div//div//div//input[@class="numInput cur-year"]',
            '//html//body//div[105]//div[1]//div//div//select[@class="flatpickr-monthDropdown-months"]',
            '//html//body//div[105]//div[2]//div//div[2]//div//span[@class="flatpickr-day" and text()="'
        ]

        field_berms_ent_application_manpower_timetable_start_to = [
            '//html//body//div[33]//div[1]//div//div//div//input[@class="numInput cur-year"]',
            '//html//body//div[33]//div[1]//div//div//select[@class="flatpickr-monthDropdown-months"]',
            '//html//body//div[33]//div[2]//div//div[2]//div//span[@class="flatpickr-day" and text()="'
        ]

        field_rbtn_if_applicable_other_peza_stockholder = {
            "APPLICABLE": '//input[@id="isListedStockholder1"]',
            "NOT APPLICABLE": '//input[@id="isListedStockholder2"]'
        }

        field_rbtn_type_ecozone = {
            "AAA": '//input[@id="enterpriseTypeId34"]',
            "DOMESTIC MARKET": '//input[@id="enterpriseTypeId2"]',
            "FACILITIES": '//input[@id="enterpriseTypeId4"]',
            "I.T.": '//input[@id="enterpriseTypeId6"]',
            "MEDICAL TOURISM": '//input[@id="enterpriseTypeId8"]',
            "UTILITIES": '//input[@id="enterpriseTypeId12"]',
            "AGRO-INDUSTRIAL": '//input[@id="enterpriseTypeId1"]',
            "EXPORT ENTERPRISE": '//input[@id="enterpriseTypeId3"]',
            "FREE TRADE": '//input[@id="enterpriseTypeId5"]',
            "LOGISTICS SERVICE": '//input[@id="enterpriseTypeId7"]',
            "SERVICE": '//input[@id="enterpriseTypeId10"]',
            "TRUCKER MANAGEMENT": '//input[@id="enterpriseTypeId33"]',
            "WAREHOUSE": '//input[@id="enterpriseTypeId9"]',
            "TOURISM": '//*[@id="enterpriseTypeId11"]'
        }

        field_dp_parent_company_registration_date = [
            '//html//body//div[3]//div[1]//div//div//div//input[@class="numInput cur-year"]',
            '//html//body//div[3]//div[1]//div//div//select[@class="flatpickr-monthDropdown-months"]',
            '//html//body//div[3]//div[2]//div//div[2]//div//span[@class="flatpickr-day" and text()="'
        ]

        date_picker_general_locations = [
            '//div[contains(@class,"open")]//div[1]//div//div//div//input[@class="numInput cur-year"]',
            '//div[contains(@class,"open")]//div[1]//div//div//select[@class="flatpickr-monthDropdown-months"]',
            '//div[contains(@class,"open")]//div[2]//div//div[2]//div/span[@class="flatpickr-day" and text()="'
        ]

        match get_element:
            case 'dp_applicants_manpower_timetable_building_from':
                return date_picker_general_locations
            case 'dp_applicants_manpower_timetable_building_to':
                return date_picker_general_locations
            case 'dp_applicants_manpower_timetable_importation_from':
                return date_picker_general_locations
            case 'dp_applicants_manpower_timetable_importation_to':
                return date_picker_general_locations
            case 'dp_applicants_manpower_timetable_installation_from':
                return date_picker_general_locations
            case 'dp_applicants_manpower_timetable_installation_to':
                return date_picker_general_locations
            case 'dp_applicants_manpower_timetable_hiring_from':
                return date_picker_general_locations
            case 'dp_applicants_manpower_timetable_hiring_to':
                return date_picker_general_locations
            case 'dp_applicants_manpower_timetable_start_from':
                return date_picker_general_locations
            # Aligned as general pick
            case 'dp_parent_company_registration_date':
                return field_dp_parent_company_registration_date
            case 'dp_applicants_existing_business_registration_date':
                return field_berms_ent_application_exi_bus_reg_date
            case 'dp_applicants_manpower_timetable_start_to':
                return field_berms_ent_application_manpower_timetable_start_to
            case 'rbtn_if_applicable_other_peza_stockholder':
                return field_rbtn_if_applicable_other_peza_stockholder
            case 'rbtn_type_of_enterpirse':
                return field_rbtn_type_ecozone

    def get_type_of_enterprise(self, get_element):
        return self.rbtn_type_ecozone[get_element], get_element

    def get_processing_views(self, get_element):
        field_elements_locations = {
            "reviewer_link_approval_page": '//div[@id="berms-application"]//div//div[1]//div[25]//button//span[2]//span[text()="Approval"]',
            "reviewer_button_approval_page": '//div[@id="application"]//div[5]//div//div//button[1]',
            "reviewer_option_approval_page_industry": '//select[@id="industryId"]',
            "reviewer_option_approval_page_status": '//select[@id="applicationStatus"]',
            "reviewer_button_approval_page_proceed": '//form[@id="form-approval"]//div[2]//button[2]',
            "reviewer_button_approval_page_proceed_confirm": '//html//body//div[3]//div//div[6]//button[1][text()="Yes"]',
            "reviewer_button_ddg_review": '//button//span[text()="Proceed to DDG Review"]',
            "reviewer_option_ddg_review_status": '//select[@id="applicationStatus"]',
            "reviewer_option_ddg_review_remarks": '//textarea[@id="applicationRemarks"]',
            "reviewer_button_ddg_review_proceed": '//form[@id="form-approval"]//div[2]//button[2]',
            "reviewer_button_ddg_review_proceed_confirm": '//button[text()="Yes"]',
            "reviewer_button_ddg_review_proceed_confirm_ok": '//button[text()="OK"]',
            "customer_button_payment_proceed": '//div[@id="application"]//div[5]//div//div//button[1]//span[text()="Proceed to Payment"]',
            "customer_button_payment_registration_proceed": '//div[@id="application"]//div[6]//div//div//button[1]//span[text()="Proceed to Payment"]',
            "customer_input_payment_method_pp": '//input[@id="radioTwo"]',
            "customer_input_payment_method_pp_acount_1": '//form[@id="form_bermsPayment"]//div//div[1]//div[1]//div[2]//div[1]//div//div[2]//div[2]//div//div//div[1]//div[1]//div//input',
            "customer_button_payment_confirm_payment": '//button[@id="btnConfirmPayment"]',
            "customer_button_cleint_agreement": '//button//span[text()="Proceed to Client Registration Agreement"]',
            "customer_drop_cleint_agreement_signature": '//div[@id="e-SignatureDropzone"]',
            "customer_button_cleint_agreement_proceed": '//form[@id="form-esignature"]/div[2]//div//button[2][@id="btnSubmitApplication"]',
            "customer_button_cleint_agreement_proceed_confirm": '//button[text()="Yes"]',
            "customer_button_cleint_agreement_proceed_confirm_ok": '//button[text()="OK"]',
            "verifier_link_approval_page": '//div[@id="application"]//div[6]//div//div//button[1]',
            "verifier_option_approval_page_status": '//select[@id="applicationStatus"]',
            "verifier_button_approval_page_proceed": '//button[@id="btnSubmitApplication"]',
            "verifier_button_approval_page_proceed_confirm": '//html//body//div[3]//div//div[6]//button[1][text()="Yes"]',
            "staff_button_evaluation_report_proceed": '//div[@id="application"]//div[6]//div//div//button[1]//span[text()="Proceed to Evaluation Report"]',
            "staff_textarea_evaluation_report_notes_1": '//form[@id="form-evaluation"]//div[1]//div[1]//div[17]//div[3]//div//div[3]//div[2]//p',
            "staff_textarea_evaluation_report_notes_2": '//form[@id="form-evaluation"]//div[1]//div[2]//div[4]//div//div[3]//div[2]//p',
            "staff_textarea_evaluation_report_notes_3": '//form[@id="form-evaluation"]//div[1]//div[2]//div[6]//div//div[3]//div[2]//p',
            "staff_textarea_evaluation_report_notes_4": '//form[@id="form-evaluation"]//div[1]//div[2]//div[37]//div//div[3]//div[2]//p',
            "staff_textarea_evaluation_report_notes_5": '//form[@id="form-evaluation"]//div[1]//div[2]//div[46]//div//div[3]//div[2]//p',
            "staff_textarea_evaluation_report_notes_6": '//form[@id="form-evaluation"]//div[1]//div[2]//div[48]//div//div[3]//div[2]//p',
            "staff_textarea_evaluation_report_notes_7": '//form[@id="form-evaluation"]//div[1]//div[2]//div[50]//div//div[3]//div[2]//p',
            "staff_textarea_evaluation_report_notes_8": '//form[@id="form-evaluation"]//div[1]//div[2]//div[52]//div//div[3]//div[2]//p',
            "staff_textarea_evaluation_report_board_fname": '//form[@id="form-evaluation"]//div[1]//div[2]//div[77]//div//div[1]//input[@name="first_name"]',
            "staff_textarea_evaluation_report_board_mname": '//form[@id="form-evaluation"]//div[1]//div[2]//div[77]//div//div[2]//input[@name="middle_name"]',
            "staff_textarea_evaluation_report_board_lname": '//form[@id="form-evaluation"]//div[1]//div[2]//div[77]//div//div[3]//input[@name="last_name"]',
            "staff_button_evaluation_report_proceed_submit": '//button[@id="submitBtn"]',
            "staff_button_evaluation_report_proceed_submit_confirm": '//button[text()="Yes"]',
            "chief_link_evaluation_status": '//div[@id="wizard-validation-berms"]//div[1]//div[5]//button//span[2]//span[text()="Evaluation Status"]',
            "chief_option_evaluation_status_confirm": '//select[@id="applicationStatus"]',
            "chief_option_evaluation_attachment_docs": '//input[@id="files"]',
            "chief_button_evaluation_status_submit": '//button[@id="saveBtn"]',
            "chief_button_evaluation_status_submit_confirm": '//html//body//div[3]//div//div[6]//button[1][text()="Yes"]'
        }

        return_element_names = {

        }

        return field_elements_locations[get_element], ''

    def get_processing_views_staff(self, get_element):
        field_elements_locations = {
            "button_assigning_of_dts": '//div[@id="application"]//div[5]//div//div//button[1]',
            "text_dts_number": '//input[@id="assign_DTS"]',
            "button_assigning_of_dts_submit": '//button[@id="btnSubmitApplication"]',
            "button_assigning_of_dts_submit_confirm": '//button[1][text()="Yes"]'
        }
        return_element_names = {
        }

        return field_elements_locations[get_element], ''

    def get_processing_views_chief(self, get_element):
        field_elements_locations = {
            "button_assigning_of_eso": '//div[@id="application"]//div[6]//div//div//button[1]',
            "option_eso_officers": '//select[@id="esoId"]',
            "button_assigning_of_eso_submit": '//button[@id="btnSubmitApplication"]',
            "button_assigning_of_eso_submit_confirm": '//button[text()="Yes"]',
            "button_assigning_of_eso_submit_confirm_ok": '//button[text()="OK"]',
            "button_evaluation_status_update": '//div[@id="application"]//div[6]//div//div//button[1]//span[text()="Proceed to Evaluation Status"]',
            "option_evaluation_update_status": '//select[@id="applicationStatus"]',
            "path_evaluation_files": '//input[@id="files"]',
            "textarea_evaluation_remarks": '//textarea[@id="applicationRemarks"]',
            "button_evaluation_status_update_proceed": '//button[@id="saveBtn"]',
            "button_evaluation_status_update_proceed_confirm": '//button[text()="Yes"]',
            "button_evaluation_status_update_proceed_confirm_ok": '//button[text()="OK"]'
        }
        return_element_names = {
        }

        return field_elements_locations[get_element], ''

    def get_processing_views_approver(self, get_element):
        field_elements_locations = {
            "button_endorsement_of_application": '//button//span[text()="Proceed to Application Endorsement"]',
            "option_endorsement_status": '//select[@id="applicationStatus"]',
            "textarea_endorsement_remarks": '//textarea[@id="applicationRemarks"]',
            "button_endorsement_of_application_proceed": '//form[@id="form-approval"]//div[2]//button[2]',
            "button_endorsement_of_application_proceed_confirm": '//button[text()="Yes"]',
            "button_endorsement_of_application_proceed_confirm_ok": '//button[text()="OK"]',
            "board_button_board_resolution_approval": '//button//span[text()="Proceed to Board Resolution Approval"]',
            "board_option_board_resolution_status": '//select[@id="applicationStatus"]',
            "board_textarea_board_resolution_remarks": '//textarea[@id="applicationRemarks"]',
            "board_button_board_resolution_approval_proceed": '//form[@id="form-approval"]//div[2]//button[2]',
            "board_button_board_resolution_approval_proceed_confirm": '//button[text()="Yes"]',
            "board_button_board_resolution_approval_proceed_confirm_ok": '//button[text()="OK"]',
            "board_button_board_endorsement": '//button//span[text()="Proceed to Application Endorsement"]',
            "board_option_board_endorsement_status": '//select[@id="applicationStatus"]',
            "board_textarea_board_endorsement_remarks": '//textarea[@id="applicationRemarks"]',
            "board_button_board_endorsement_proceed": '//form[@id="form-approval"]//div[2]//button[2]',
            "board_button_board_endorsement_proceed_confirm": '//button[text()="Yes"]',
            "board_button_board_endorsement_proceed_confirm_ok": '//button[text()="OK"]',
            "board_drop_board_endorsement_signature": ''
        }
        return_element_names = {
        }

        return field_elements_locations[get_element], ''


    def get_processing_views_verifier(self, get_element):
        field_elements_locations = {
            "button_review_endorsement_of_app": '//button//span[text()="Proceed to Review Endorsement"]',
            "option_review_endorsement_status": '//select[@id="applicationStatus"]',
            "textarea_review_endorsement_remarks": '//textarea[@id="applicationRemarks"]',
            "button_review_endorsement_of_app_proceed": '//form[@id="form-approval"]//div[2]//button[2]',
            "button_review_endorsement_of_app_proceed_confirm": '//button[text()="Yes"]',
            "button_review_endorsement_of_app_proceed_confirm_ok": '//button[text()="OK"]',
            "board_button_board_approval": '//button//span[text()="Proceed to Board approval"]',
            "board_dp_cert_resolution_meeting_date": '//input[@id="brMeetingDate"]',
            "board_text_cert_resolution_number": '//span[@id="brResolutionNumber"]',
            "board_text_cert_resolution_entitled": '//span[@id="brEntitledTo"]',
            "board_text_cert_resolution_provisions_1": '//span[@id="brProvision1"]',
            "board_text_cert_resolution_provisions_2": '//span[@id="brProvision2"]',
            "board_text_cert_resolution_signing": '//span[@id="brSigningOfPosition"]',
            "board_text_cert_resolution_signing_document": '//span[@id="brPreRegistration"]',
            "board_text_cert_resolution_signing_office": '//span[@id="brDocumentsDepartment"]',
            "board_textarea_cert_resolution_pre_registration_conditions": '//form[@id="form_BRC"]//div//div//div//div//div[1]//div[1]//div//div[3]//div[2]//p',
            "board_textarea_cert_resolution_registration_conditions": '//form[@id="form_BRC"]//div//div//div//div//div[1]//div[2]//div//div[3]//div[2]//p',
            "board_button_board_approval_proceed": '//form[@id="form_BRC"]//div//div//div//div//div[2]//div//button[2][@id="submitBtn"]',
            "board_button_board_approval_proceed_confirm": '//button[text()="Yes"]',
            "board_button_board_approval_proceed_confirm_ok": '//button[text()="OK"]',
        }
        return_element_names = {
        }

        return field_elements_locations[get_element], ''

    def get_processing_views_verifier_others(self, get_element):
        field_board_dp_cert_resolution_meeting_date = [
            '//html//body//div[3]//div[1]//div//div//div//input[@class="numInput cur-year"]',
            '//html//body//div[3]//div[1]//div//div//select[@class="flatpickr-monthDropdown-months"]',
            '//html//body//div[3]//div[2]//div//div[2]//div//span[@class="flatpickr-day" and text()="',
            '//html//body//div[3]//div[2]//div//div[2]//div//span[@aria-label="'
        ]

        match get_element:
            case 'board_dp_cert_resolution_meeting_date':
                return field_board_dp_cert_resolution_meeting_date