from FrameWork.config_files.frame_work_base_driver import FrameWorkBaseDriver


class BermsDeveloperElementLocations(FrameWorkBaseDriver):
    def __init__(self, driver):
        self.driver = driver

    def get_berms_dev_pages_application(self, get_element):
        field_elements_locations = {
            "cbox_berms_dev_agree_app_undertaking": '//input[@id="acceptApplicantUndertakings"]',
            "btn_berms_dev_agree_app_undetaking": '//button[@id="btnSubmitUndertaking"]',
            "txt_berms_dev_application_propose_eco_zone": '//input[@id="proposedEconomicZoneName"]',
            "option_berms_dev_application_psic": '//select[@name="activity.psic_id"]',
            "option_berms_dev_application_psic_activity": '//select[@name="activity.psic_division_code_id"]',
            "option_psic_group_code": '//select[@id="groupCodeId"]',
            "option_psic_classes_code": '//select[@id="classesCodeId"]',
            "option_psic_sub_classes_code": '//select[@id="subClassesCodeId"]',
            "rbtn_berms_dev_application_type_ecozone": '',
            "btn_berms_dev_application_proceed": '//html//body//div[2]//div[1]//div//div//div[1]//div[2]//div//div//div[2]//div//div[1]//div//div[2]//form//div[1]//div//div[2]//div//div//button//span',
            "txt_berms_dev_company_info_website": '//input[@id="contactWebsite"]',
            "btn_berms_dev_company_info_proceed": '//div[@id="company-info"]//div[2]//div[2]//div//div//button//span[text()="Proceed"]'
        }

        return_element_names = {
            "cbox_berms_dev_agree_app_undertaking": 'Check berms dev application of undertaking agree CLICK',
            "btn_berms_dev_agree_app_undetaking": 'Proceed in acceptance of the application of undertaking CLICK',
            "txt_berms_dev_application_propose_eco_zone": 'Provide proposed name of ecozone INPUT',
            "option_berms_dev_application_psic": 'Provide application psic SELECT',
            "option_berms_dev_application_psic_activity": 'Provide application psic activity SELECT',
            "option_psic_group_code": '',
            "option_psic_classes_code": '',
            "option_psic_sub_classes_code": '',
            "rbtn_berms_dev_application_type_ecozone": 'Provide application type of ecozone SELECT',
            "btn_berms_dev_application_proceed": 'Proceed from application to company info CLICK',
            "txt_berms_dev_company_info_website": 'Provide company info website INPUT',
            "btn_berms_dev_company_info_proceed": 'Proceed company info to official representative CLICK'
        }

        return field_elements_locations[get_element], return_element_names[get_element]

    def get_berms_dev_pages_application_others(self, get_element):
        rbtn_berms_dev_application_type_ecozone = {
            "MANUFACTURING ECOZONE": '//input[@id="economicZoneId1"]',
            "INFORMATION TECHNOLOGY PARK": '//input[@id="economicZoneId3"]',
            "INFORMATION TECHNOLOGY CENTER": '//input[@id="economicZoneId4"]',
            "TOURISM ECOZONE": '//input[@id="economicZoneId5"]',
            "MEDICAL TOURISM PARK": '//input[@id="economicZoneId6"]',
            "MEDICAL TOURISM CENTER": '//input[@id="economicZoneId7"]',
            "RETIREMENT ECOZONE PARK": '//input[@id="economicZoneId8"]',
            "RETIREMENT ECOZONE CENTER": '//input[@id="economicZoneId9"]'
        }

        match get_element:
            case 'rbtn_berms_dev_application_type_ecozone':
                return rbtn_berms_dev_application_type_ecozone

    def get_berms_dev_pages_off_rep(self, get_element):
        field_elements_locations = {
            "txt_berms_dev_off_rep_first_name": '//input[@id="representatives0FirstName"]',
            "txt_berms_dev_off_rep_middle_name": '//input[@id="representatives0MiddleName"]',
            "txt_berms_dev_off_rep_last_name": '//input[@id="representatives0LastName"]',
            "option_berms_dev_off_rep_address_region": '//select[@id="representatives0RegionId"]',
            "option_berms_dev_off_rep_address_province": '//select[@id="representatives0ProvinceId"]',
            "option_berms_dev_off_rep_address_city": '//select[@id="representatives0CityId"]',
            "option_berms_dev_off_rep_address_barangay": '//select[@id="representatives0BarangayId"]',
            "txt_berms_dev_off_rep_address_street": '//input[@id="representatives0StreetName"]',
            "txt_berms_dev_off_rep_mobile_num": '//input[@id="representatives0MobileNumber"]',
            "txt_berms_dev_off_rep_land_line": '//input[@id="representatives0telephoneNumber"]',
            "txt_berms_dev_off_rep_email_address": '//input[@id="representatives0EmailAddress"]',
            "txt_berm_dev_off_rep_website": '//input[@id="representatives0Website"]',
            "btn_berms_dev_off_rep_proceed": '//div[@id="representative"]//div[3]//div//div//button//span[text()="Proceed"]'
        }

        return_element_names = {
            "txt_berms_dev_off_rep_first_name": 'Provide official representative first name INPUT',
            "txt_berms_dev_off_rep_middle_name": 'Provide official representative middle name INPUT',
            "txt_berms_dev_off_rep_last_name": 'Provide official representative last name INPUT',
            "option_berms_dev_off_rep_address_region": 'Provide official representative address region INPUT',
            "option_berms_dev_off_rep_address_province": 'Provide official representative address province INPUT',
            "option_berms_dev_off_rep_address_city": 'Provide official representative address city INPUT',
            "option_berms_dev_off_rep_address_barangay": 'Provide official representative address barangay INPUT',
            "txt_berms_dev_off_rep_address_street": 'Provide official representative address street INPUT',
            "txt_berms_dev_off_rep_mobile_num": 'Provide official representative mobile number INPUT',
            "txt_berms_dev_off_rep_land_line": 'Provide official representative landline number INPUT',
            "txt_berms_dev_off_rep_email_address": 'Provide official representative email address INPUT',
            "txt_berm_dev_off_rep_website": 'Provide official representative website INPUT',
            "btn_berms_dev_off_rep_proceed": 'Proceed from official representative to Capital Structure INPUT'
        }

        return field_elements_locations[get_element], return_element_names[get_element]

    def get_berms_dev_pages_capital_structure(self, get_element):
        field_elements_locations = {
            "main_menu_access": '//div[@id="berms-application"]//div//div[1]//div[7]//button//span[2]//span[1]',
            "txt_berms_dev_capital_structure_authorized": '//input[@id="authorizedAmount"]',
            "txt_berms_dev_capital_structure_subscribed": '//input[@id="subscribeAmount"]',
            "txt_berms_dev_capital_struture_paid_up": '//input[@id="paidUpAmount"]',
            "txt_berms_dev_capital_struture_paid_in": '//input[@id="paidInAmount"]',
            "btn_berms_dev_capital_structure_add_stockholder": '//button[@id="btnAddStockholder"]',
            "btn_berms_dev_capital_structure_proceed": '//div[@id="capital-info"]//div[2]//div//div//button//span[text()="Proceed"]',
            "txt_berms_dev_capital_structure_propose_stockholder_fname": '//input[@id="proposedStockholderFirstName"]',
            "txt_berms_dev_capital_structure_propose_stockholder_mname": '//input[@id="proposedStockholderMiddleName"]',
            "txt_berms_dev_capital_structure_propose_stockholder_lname": '//input[@id="proposedStockholderLastName"]',
            "option_berms_dev_capital_structure_propose_stockholder_nationality": '//select[@id="proposedStockholderNationalityId"]',
            "txt_berms_dev_capital_structure_propose_stockholder_num_shares": '//input[@id="proposedStockholderNumberOfShares"]',
            "txt_berms_dev_capital_structure_propose_stockholder_subs_amount": '//input[@id="proposedStockholderSubscribeAmt"]',
            "txt_berms_dev_capital_structure_propose_stockholder_paid_up_amount": '//input[@id="proposedStockholderPaidupAmt"]',
            "btn_berms_dev_capital_structure_propose_stockholder_add": '//form[@id="form_proposedStockholders"]//button[@id="btnAddStockholder"]'
        }

        return_element_names = {
            "main_menu_access": '',
            "txt_berms_dev_capital_structure_authorized": 'Provide capital structure authorized amount INPUT',
            "txt_berms_dev_capital_structure_subscribed": 'Provide capital structure subscribed amount INPUT',
            "txt_berms_dev_capital_struture_paid_up": 'Provide capital structure paid up amount INPUT',
            "txt_berms_dev_capital_struture_paid_in": 'Provide capital structure paid in amount INPUT',
            "btn_berms_dev_capital_structure_add_stockholder": 'Add capital structure stockholder CLICK',
            "btn_berms_dev_capital_structure_proceed": 'Proceed from capital structure to principal officers CLICK',
            "txt_berms_dev_capital_structure_propose_stockholder_fname": 'Provide stockholder first name INPUT',
            "txt_berms_dev_capital_structure_propose_stockholder_mname": 'Provide stockholder middel name INPUT',
            "txt_berms_dev_capital_structure_propose_stockholder_lname": 'Provide stockholder last name INPUT',
            "option_berms_dev_capital_structure_propose_stockholder_nationality": 'Provide stockholder nationality INPUT',
            "txt_berms_dev_capital_structure_propose_stockholder_num_shares": 'Provide stockholder number of shares INPUT',
            "txt_berms_dev_capital_structure_propose_stockholder_subs_amount": 'Provide stockholder subscribed amount INPUT',
            "txt_berms_dev_capital_structure_propose_stockholder_paid_up_amount": 'Provide stockholder paid up amount INPUT',
            "btn_berms_dev_capital_structure_propose_stockholder_add": 'Proceed add of stockholder CLICK'
        }

        return field_elements_locations[get_element], return_element_names[get_element]

    def get_berms_dev_pages_principal_officer(self, get_element):
        field_elements_locations = {
            "button_prcpl_officer_add": '//div[@id="dt_principalOfficers_wrapper"]//div[3]//div[2]//button[@title="Add Principal Officer"]',
            "txt_prcpl_off_first_name": '//input[@id="officerFirstName"]',
            "txt_prcpl_off_middle_name": '//input[@id="officerMiddleName"]',
            "txt_prcpl_off_last_name": '//input[@id="officerLastName"]',
            "option_prcpl_off_nationality": '//select[@id="officerNationalityId"]',
            "txt_prcpl_off_position": '//input[@id="officerPosition"]',
            "button_prcpl_off_add_proceed": '//button[@id="btnAddPrincipalOfficer"]',
            "btn_berms_dev_other_projects_add": '//button[@data-bs-target="#projectInvolvementModal"]',
            "txt_berms_dev_other_projects_project_name": '//input[@id="projectName"]',
            "option_berms_dev_other_projects_project_year": '//select[@id="projectYearEstablished"]',
            "txt_berms_dev_other_projects_project_description": '//textarea[@id="projectDescription"]',
            "btn_berms_dev_other_projects_add_proceed": '//button[@id="btnAddProjectInvolvement"]',
            "btn_berms_dev_principal_officer_proceed": '//*[@id="principal-officers"]//div[2]//div[3]//div//div//button'
        }

        return_element_names = {
            "button_prcpl_officer_add": 'Add Principal officers CLICK',
            "txt_prcpl_off_first_name": 'Provide principal officer first name INPUT',
            "txt_prcpl_off_middle_name": 'Provide principal officer middle name INPUT',
            "txt_prcpl_off_last_name": 'Provide principal officer last name INPUT',
            "option_prcpl_off_nationality": 'Provide principal officer nationality SELECT',
            "txt_prcpl_off_position": 'Provide principal officer position INPUT',
            "button_prcpl_off_add_proceed": 'Proceed add principal officer CLICK',
            "btn_berms_dev_other_projects_add": 'Add other Projects Involvement CLICK',
            "txt_berms_dev_other_projects_project_name": 'Provide other project project name INPUT',
            "option_berms_dev_other_projects_project_year": 'Provide other project project year INPUT',
            "txt_berms_dev_other_projects_project_description": 'Provide other project project description INPUT',
            "btn_berms_dev_other_projects_add_proceed": 'Proceed other project to add CLICK',
            "btn_berms_dev_principal_officer_proceed": 'Proceed from principal officer to the land CLICK'
        }

        return field_elements_locations[get_element], return_element_names[get_element]

    def get_berms_dev_pages_the_land(self, get_element):
        field_elements_locations = {
            "option_berms_dev_the_land_loc_region": '//select[@name="land.address.region_id"]',
            "option_berms_dev_the_land_loc_province": '//select[@name="land.address.province_id"]',
            "option_berms_dev_the_land_loc_city": '//select[@name="land.address.city_id"]',
            "option_berms_dev_the_land_loc_barangay": '//select[@name="land.address.barangay_id"]',
            "txt_berms_dev_the_land_loc_street": '//input[@name="land.address.line_1"]',
            "txt_berms_dev_the_land_zip_code": '//input[@id="landPostalCode"]',
            "txt_berms_dev_the_land_land_area": '//input[@name="land.land_area"]',
            "txt_berms_dev_the_land_floor_area": '//input[@id="landFloorArea"]',
            "txt_berms_dev_the_land_existing_land_agriculture": '//input[@name="land.existing_land_use_desc"]',
            "cbox_berms_dev_the_land_existing_land_non_agriculture": '',
            "txt_berms_dev_the_land_existing_land_non_agriculture_others": '//input[@id="nonAgriculturalOtherValue"]',
            "cbox_berms_dev_the_land_existing_land_zone_june_1988": '',
            "txt_berms_dev_the_land_existing_land_zone_june_1988_others": '//input[@id="zoneClassificationOtherValue"]',
            "cbox_berms_dev_the_land_existing_land_topography": '',
            "txt_berms_dev_the_land_existing_land_boundaries_north": '//input[@id="boundariesNorth"]',
            "txt_berms_dev_the_land_existing_land_boundaries_east": '//input[@id="boundariesEast"]',
            "txt_berms_dev_the_land_existing_land_boundaries_west": '//input[@id="boundariesWest"]',
            "txt_berms_dev_the_land_existing_land_boundaries_south": '//input[@id="boundariesSouth"]',
            "cbox_berms_dev_the_land_existing_land_ownership_right": '',
            "txt_berms_dev_the_land_existing_land_ownership_right_others": '//input[@id="ownershipOtherValue"]',
            "cbox_berms_dev_the_land_existing_land_tenancy": '',
            "btn_berms_dev_the_land_existing_land_proximity_to_ports_add": '//div[@id="dt_majorPorts_wrapper"]//div//div//button',
            "txt_berms_dev_the_land_existing_land_proximity_to_ports_port": '//input[@id="portName"]',
            "txt_berms_dev_the_land_existing_land_proximity_to_ports_distance": '//input[@id="portDistance"]',
            "btn_berms_dev_the_land_existing_land_proximity_to_ports_proceed": '//button[@id="btnAddMajorPort"]',
            "txt_berms_dev_the_land_off_site_details_accesibility": '//textarea[@id="landOffsiteAccessibilityTranportation"]',
            "txt_berms_dev_the_land_off_site_details_other_communication": '//textarea[@id="landOffsiteOtherCommunication"]',
            "txt_berms_dev_the_land_off_site_details_telecommunication": '//textarea[@id="landOffsiteTelecommunicationProvider"]',
            "txt_berms_dev_the_land_off_site_details_power_source": '//textarea[@id="landOffsitePowerSystemSource"]',
            "txt_berms_dev_the_land_off_site_details_power_franchisee": '//textarea[@id="landOffsitePowerFranchisee"]',
            "txt_berms_dev_the_land_off_site_details_power_transmission": '//textarea[@id="landOffsitePowerTransmissionAndDistribution"]',
            "txt_berms_dev_the_land_off_site_details_water_source": '//textarea[@id="landOffsiteWaterSystemSource"]',
            "txt_berms_dev_the_land_off_site_details_distribution_system": '//textarea[@id="landOffsiteDistributionSystem"]',
            "btn_berms_dev_the_land_proceed": '//div[@id="the-land"]//div[2]//div//div//button//span[text()="Proceed"]'
        }

        return_element_names = {
            "option_berms_dev_the_land_loc_region": 'Provide the land address region SELECT',
            "option_berms_dev_the_land_loc_province": 'Provide the land address province SELECT',
            "option_berms_dev_the_land_loc_city": 'Provide the land address city SELECT',
            "option_berms_dev_the_land_loc_barangay": 'Provide the land address barangay SELECT',
            "txt_berms_dev_the_land_loc_street": 'Provide the land address street INPUT',
            "txt_berms_dev_the_land_zip_code": 'Provide the land address zip code INPUT',
            "txt_berms_dev_the_land_land_area": 'Provide the land area INPUT',
            "txt_berms_dev_the_land_floor_area": 'Provide the land area INPUT',
            "txt_berms_dev_the_land_existing_land_agriculture": 'Provide the land existing land description INPUT',
            "cbox_berms_dev_the_land_existing_land_non_agriculture": '',
            "txt_berms_dev_the_land_existing_land_non_agriculture_others": 'Provide the land existing land non-agricultural others INPUT',
            "cbox_berms_dev_the_land_existing_land_zone_june_1988": '',
            "txt_berms_dev_the_land_existing_land_zone_june_1988_others": 'Provide the land zone other INPUT',
            "cbox_berms_dev_the_land_existing_land_topography": '',
            "txt_berms_dev_the_land_existing_land_boundaries_north": 'Provide the land boundaries north INPUT',
            "txt_berms_dev_the_land_existing_land_boundaries_east": 'Provide the land boundaries east INPUT',
            "txt_berms_dev_the_land_existing_land_boundaries_west": 'Provide the land boundaries west INPUT',
            "txt_berms_dev_the_land_existing_land_boundaries_south": 'Provide the land boundaries south INPUT',
            "cbox_berms_dev_the_land_existing_land_ownership_right": '',
            "txt_berms_dev_the_land_existing_land_ownership_right_others": 'Provide the land ownership others INPUT',
            "cbox_berms_dev_the_land_existing_land_tenancy": '',
            "btn_berms_dev_the_land_existing_land_proximity_to_ports_add": 'Add proximity to major ports CLICK',
            "txt_berms_dev_the_land_existing_land_proximity_to_ports_port": 'Provide the land major ports port INPUT',
            "txt_berms_dev_the_land_existing_land_proximity_to_ports_distance": 'Provide the land major ports distance INPUT',
            "btn_berms_dev_the_land_existing_land_proximity_to_ports_proceed": 'Proceed add ports CLICK',
            "txt_berms_dev_the_land_off_site_details_accesibility": 'Provide off-site infra, facility, utilities accessibility INPUT',
            "txt_berms_dev_the_land_off_site_details_other_communication": 'Provide off-site infra, facility, utilities other communication INPUT',
            "txt_berms_dev_the_land_off_site_details_telecommunication": 'Provide off-site infra, facility, utilities telecommunication INPUT',
            "txt_berms_dev_the_land_off_site_details_power_source": 'Provide off-site infra, facility, utilities power source INPUT',
            "txt_berms_dev_the_land_off_site_details_power_franchisee": 'Provide off-site infra, facility, utilities power franchisee INPUT',
            "txt_berms_dev_the_land_off_site_details_power_transmission": 'Provide off-site infra, facility, utilities power transmission INPUT',
            "txt_berms_dev_the_land_off_site_details_water_source": 'Provide off-site infra, facility, utilities water source INPUT',
            "txt_berms_dev_the_land_off_site_details_distribution_system": 'Provide off-site infra, facility, utilities distribution system INPUT',
            "btn_berms_dev_the_land_proceed": 'Proceed the land CLICK'
        }

        return field_elements_locations[get_element], return_element_names[get_element]

    def get_berms_dev_pages_the_land_others(self, get_element):
        cbox_berms_dev_the_land_existing_land_non_agriculture = {
            "BARREN": '//input[@id="nonAgriculturalBarrenIdleLand"]',
            "GRASS LAND": '//input[@id="nonAgriculturalGrassLand"]',
            "OTHERS": '//input[@id="nonAgriculturalOthers"]'
        }

        cbox_berms_dev_the_land_existing_land_zone_june_1988 = {
            "AGRICULTURE": '//input[@id="zoneClassificationAgriculture"]',
            "COMMERCIAL": '//input[@id="zoneClassificationCommercial"]',
            "INDUSTRIAL": '//input[@id="zoneClassificationIndustrial"]',
            "RESIDENTIAL": '//input[@id="zoneClassificationResidential"]',
            "OTHERS": '//input[@id="zoneClassificationOthers"]'
        }
        cbox_berms_dev_the_land_existing_land_topography = {
            "FLAT": '//input[@id="topograhpyFlat"]',
            "SLIGHTLY SLOPPING": '//input[@id="topograhpySlightlySlopping"]',
            "HILL": '//input[@id="topograhpyHill"]',
            "VERY STEEP": '//input[@id="topograhpyVerySteep"]'
        }

        cbox_berms_dev_the_land_existing_land_ownership_right = {
            "FULL OWNERSHIP": '//input[@id="ownershipFullOwnership"]',
            "JOINT VENTURE": '//input[@id="ownershipJointVentureAgreement"]',
            "LEASE CONTRACT": '//input[@id="ownershipLeaseContract"]',
            "MOA": '//input[@id="ownershipMOA"]',
            "OTHERS": '//input[@id="ownershipOthers"]'
        }

        cbox_berms_dev_the_land_existing_land_tenancy = {
            "TERMINATED": '//input[@id="tenancyTenanted"]',
            "NON-TERMINATED": '//input[@id="tenancyNonTenanted"]'
        }

        match get_element:
            case 'cbox_berms_dev_the_land_existing_land_non_agriculture':
                return cbox_berms_dev_the_land_existing_land_non_agriculture
            case 'cbox_berms_dev_the_land_existing_land_zone_june_1988':
                return cbox_berms_dev_the_land_existing_land_zone_june_1988
            case 'cbox_berms_dev_the_land_existing_land_topography':
                return cbox_berms_dev_the_land_existing_land_topography
            case 'cbox_berms_dev_the_land_existing_land_ownership_right':
                return cbox_berms_dev_the_land_existing_land_ownership_right
            case 'cbox_berms_dev_the_land_existing_land_tenancy':
                return cbox_berms_dev_the_land_existing_land_tenancy

    def get_berms_dev_pages_the_project(self, get_element):
        field_elements_locations = {
            "txt_loc_region_land_loc_industrial_area": '//input[@id="defaultFacilityArea0"]',
            "option_land_loc_industrial_percent": '//select[@id="defaultFacilityPercent0"]',
            "txt_land_loc_common_utility_area": '//input[@id="defaultFacilityArea1"]',
            "option_land_loc_common_utility_percent": '//select[@id="defaultFacilityPercent1"]',
            "txt_land_loc_buffer_zone_area": '//input[@id="defaultFacilityArea2"]',
            "option_land_loc_buffer_zone_percent": '//select[@id="defaultFacilityPercent2"]',
            "btn_land_loc_facilities_add": '//div[@id="dt_facilities_wrapper"]//div[3]//div[2]//button//span//i',
            "txt_land_loc_facilities_add_component": '//input[@id="facilityComponent"]',
            "txt_land_loc_facilities_add_area": '//input[@id="facilityArea"]',
            "option_land_loc_facilities_add_percent": '//select[@id="facilityPercent"]',
            "btn_land_loc_facilities_add_proceed": '//button[@id="btnAddFacilities"]',
            "rbtn_land_loc_status_of_development": '',
            # "rbtn_state_of_development_new_development": '//input[@id="projectDevelopmentStatus1"]',
            # "rbtn_state_of_development_under_development": '//input[@id="projectDevelopmentStatus2"]',
            # "rbtn_state_of_development_existing": '//input[@id="projectDevelopmentStatus3"]',
            "dp_state_of_development_date_commencement": '//div[@id="developmentDateWrapper"]//div//div[2]//input[2]',
            "dp_state_of_development_date_completion": '//div[@id="developmentDateWrapper"]//div//div[3]//input[2]',
            "txt_state_of_development_completion": '//input[@id="landPercentageCompletion"]',
            "btn_labor_requirements_add": '//div[@id="dt_laborRequirements_wrapper"]//div[3]//div[2]//button[@title="Add Labor Requirements"]',
            "txt_labor_requirements_add_year": '//input[@id="laborTargetYear"]',
            "txt_labor_requirements_add_direct": '//input[@id="laborDirectHireCount"]',
            "txt_labor_requirements_add_indirect": '//input[@id="laborIndirectHireCount"]',
            "txt_labor_requirements_add_remarks": '//textarea[@id="laborRemarks"]',
            "btn_labor_requirements_add_proceed": '//button[@id="btnAddLaborRequirements"]',''
            "txt_on_site_facilities_primary_road_width": '//input[@id="primaryRoad"]',
            "txt_on_site_facilities_primary_road_type": '//input[@name="land.primary_road_pavetype"]',
            "txt_on_site_facilities_secondary_road_width": '//input[@id="secondaryRoad"]',
            "txt_on_site_facilities_secondary_road_type": '//input[@name="land.secondary_road_pavetype"]',
            "txt_on_site_facilities_tertiary_road_width": '//input[@id="tertiaryRoad"]',
            "txt_on_site_facilities_tertiary_road_type": '//input[@name="land.tertiary_road_pavetype"]',
            "txt_power_system_source": '//input[@name="project.onsite_power_system_source"]',
            "txt_power_franchisee": '//input[@name="project.onsite_power_franchisee"]',
            "txt_power_transmission_distribution": '//input[@name="project.onsite_power_transmission_distribution"]',
            "txt_back_power_source": '//input[@name="project.onsite_backup_power_source"]',
            "txt_back_power_capacity": '//input[@name="project.onsite_backup_power_capacity"]',
            "txt_telecom_provider": '//input[@name="project.onsite_telecom_provider"]',
            "txt_number_of_lines": '//input[@id="numberOfLines"]',
            "txt_high_speed_voice_data": '//input[@name="project.onsite_hi_speed_voice_data"]',
            "txt_other_communication_service": '//input[@name="project.onsite_other_communication_service"]',
            "txt_water_system_source": '//input[@name="project.onsite_water_system_source"]',
            "txt_distribution_system": '//input[@name="project.onsite_distribution_system"]',
            "txt_sewage_and_drainage_system": '//input[@name="project.sewage_and_drainage_system"]',
            "txt_sewage_treatment_disposal": '//input[@name="project.sewage_treatment_disposal"]',
            "txt_waste_water_treatment": '//input[@name="project.wastewater_treatment"]',
            "txt_waste_water_disposal": '//input[@name="project.wastewater_disposal"]',
            "txt_waste_water_recycling": '//input[@name="project.wastewater_recycling"]',
            "txt_solid_waste_disposal_system": '//input[@name="project.solid_waste_disposal_system"]',
            "txt_firefighting_system": '//input[@name="project.fire_fighting_system"]',
            "txt_other_util_amenities": '//input[@name="project.other_util_amenities"]',
            "txt_propose_community_development_project": '//input[@name="project.proposed_community_development_project"]',
            "txt_propose_improvements": '//input[@name="project.proposed_improvements"]',
            "txt_support_institutions": '//input[@name="project.support_institutions"]',
            "txt_land_aquisition_costs": '//input[@name="project_cost[land_acquisition_cost]"]',
            "txt_escozone_development_cost": '//input[@name="project_cost[ecozone_development_cost]"]',
            "txt_roads_and_open_spaces_cost": '//input[@name="project_cost[roads_and_open_spaces_cost]"]',
            "txt_central_wastewater_treatment_cost": '//input[@name="project_cost[central_wastewater_treatment_cost]"]',
            "txt_utilities_cost": '//input[@name="project_cost[utilities_cost]"]',
            "txt_other_project_cost": '//input[@name="project_cost[other_project_cost]"]',
            "txt_improvement_cost": '//input[@name="project_cost[improvement_cost]"]',
            "btn_source_of_funds_add": '//div[@id="dt_sourceOfFunds_wrapper"]//div[3]//div[2]//button[@title="Add Source of Fund"]',
            "txt_source_of_fund": '//input[@name="funds_source"]',
            "option_source_of_fund": '//select[@id="fundsSource"]',
            "option_funds_percent_share": '//select[@name="funds_percent_share"]',
            "btn_source_of_funds_add_proceed": '//button[@id="btnAddSourceOfFunds"]',
            "txt_land_development_cost": '//input[@name="project.land_development_cost"]',
            "txt_vertical_development_cost": '//input[@name="project.vertical_development_cost"]',
            "txt_preferred_industries": '//input[@name="project.preferred_industries"]',
            "txt_prospective_company_name": '//input[@name="project.prospective_company_name"]',
            "txt_prospective_company_activity": '//input[@name="project.prospective_company_activity"]',
            "txt_projected_employment": '//input[@name="project.projected_employment"]',
            "txt_projected_investment": '//input[@name="project.projected_investment"]',
            "txt_marketing_program": '//input[@name="project.marketing_program"]',
            "txt_environmental_management_program": '//input[@name="project.environmental_management_program"]',
            "txt_liquid_waste_management_program": '//input[@name="project.liquid_waste_management_program"]',
            "txt_solid_waste_management_program": '//input[@name="project.solid_waste_management_program"]',
            "txt_toxic_hazardous_waste_management_plan": '//input[@name="project.toxic_hazardous_waste_management_plan"]',
            "txt_preventation_abatement_of_polution": '//input[@name="project.prevention_abatement_of_pollution"]',
            "btn_the_project_proceed": '//div[@id="the-project"]//div[5]//div//div//button//span[text()="Proceed"]'
        }

        return_element_names = {
            "txt_loc_region_land_loc_industrial_area": 'the project industrial area INPUT',
            "option_land_loc_industrial_percent": 'the project industrial percent SELECT',
            "txt_land_loc_common_utility_area": 'the project common utility area INPUT',
            "option_land_loc_common_utility_percent": 'the project common utility percent SELECT',
            "txt_land_loc_buffer_zone_area": 'the project buffer zone area INPUT',
            "option_land_loc_buffer_zone_percent": 'the project buffer zone percent SELECT',
            "btn_land_loc_facilities_add": 'the project add facilities CLICK',
            "txt_land_loc_facilities_add_component": 'the project add facilities component INPUT',
            "txt_land_loc_facilities_add_area": 'the project add facilities area INPUT',
            "option_land_loc_facilities_add_percent": 'the project add facilities percent INPUT',
            "btn_land_loc_facilities_add_proceed": 'the project add facilities proceed CLICK',
            "rbtn_land_loc_status_of_development": '',
            # "rbtn_state_of_development_new_development": 'the project status of development new CLICK',
            # "rbtn_state_of_development_under_development": 'the project status of development ongoing CLICK',
            # "rbtn_state_of_development_existing": 'the project status of development existing CLICK',
            "dp_state_of_development_date_commencement": 'the project status of development date of commencement INPUT',
            "dp_state_of_development_date_completion": 'the project status of development date of completion INPUT',
            "txt_state_of_development_completion": 'the project status of development percent completion INPUT',
            "btn_labor_requirements_add": 'the project labor requirements add CLICK',
            "txt_labor_requirements_add_year": 'the project labor requirements year INPUT',
            "txt_labor_requirements_add_direct": 'the project labor requirements direct hire INPUT',
            "txt_labor_requirements_add_indirect": 'the project labor requirements indirect hire INPUT',
            "txt_labor_requirements_add_remarks": 'the project labor requirements remarks INPUT',
            "btn_labor_requirements_add_proceed": 'the project labor requirements proceed CLICK',
            "txt_on_site_facilities_primary_road_width": 'the project on-site facilities primary road width INPUT',
            "txt_on_site_facilities_primary_road_type": 'the project on-site facilities primary road type INPUT',
            "txt_on_site_facilities_secondary_road_width": 'the project on-site facilities secondary road width INPUT',
            "txt_on_site_facilities_secondary_road_type": 'the project on-site facilities secondary road type INPUT',
            "txt_on_site_facilities_tertiary_road_width": 'the project on-site facilities tertiary road width INPUT',
            "txt_on_site_facilities_tertiary_road_type": 'the project on-site facilities tertiary road type INPUT',
            "txt_power_system_source": 'the project power source and power system INPUT',
            "txt_power_franchisee": '',
            "txt_power_transmission_distribution": '',
            "txt_back_power_source": '',
            "txt_back_power_capacity": '',
            "txt_telecom_provider": '',
            "txt_number_of_lines": '',
            "txt_high_speed_voice_data": '',
            "txt_other_communication_service": '',
            "txt_water_system_source": '',
            "txt_distribution_system": '',
            "txt_sewage_and_drainage_system": '',
            "txt_sewage_treatment_disposal": '',
            "txt_waste_water_treatment": '',
            "txt_waste_water_disposal": '',
            "txt_waste_water_recycling": '',
            "txt_solid_waste_disposal_system": '',
            "txt_firefighting_system": '',
            "txt_other_util_amenities": '',
            "txt_propose_community_development_project": '',
            "txt_propose_improvements": '',
            "txt_support_institutions": '',
            "txt_land_aquisition_costs": '',
            "txt_escozone_development_cost": '',
            "txt_roads_and_open_spaces_cost": '',
            "txt_central_wastewater_treatment_cost": '',
            "txt_utilities_cost": '',
            "txt_other_project_cost": '',
            "txt_improvement_cost": '',
            "btn_source_of_funds_add": '',
            "txt_source_of_fund": '',
            "option_source_of_fund": '',
            "option_funds_percent_share": '',
            "btn_source_of_funds_add_proceed": '',
            "txt_land_development_cost": '',
            "txt_vertical_development_cost": '',
            "txt_preferred_industries": '',
            "txt_prospective_company_name": '',
            "txt_prospective_company_activity": '',
            "txt_projected_employment": '',
            "txt_projected_investment": '',
            "txt_marketing_program": '',
            "txt_environmental_management_program": '',
            "txt_liquid_waste_management_program": '',
            "txt_solid_waste_management_program": '',
            "txt_toxic_hazardous_waste_management_plan": '',
            "txt_preventation_abatement_of_polution": '',
            "btn_the_project_proceed": ''
        }

        return field_elements_locations[get_element], return_element_names[get_element]

    def get_berms_dev_pages_the_project_others(self, get_element):
        rbtn_land_loc_status_of_development = {
            "NEW DEVELOPMENT": '//input[@id="projectDevelopmentStatus1"]',
            "UNDER DEVELOPMENT": '//input[@id="projectDevelopmentStatus2"]',
            "EXISTING": '//input[@id="projectDevelopmentStatus3"]'
        }

        dp_state_of_development_date_commencement = [
            '//html//body//div[4]//div[1]//div//div//div//input[@class="numInput cur-year"]',
            '//html//body//div[4]//div[1]//div//div//select[@class="flatpickr-monthDropdown-months"]',
            '//html//body//div[4]//div[2]//div//div[2]/div//span[@class="flatpickr-day" and text()="'
        ]

        dp_state_of_development_date_completion = [
            '//html//body//div[5]//div[1]//div//div//div//input[@class="numInput cur-year"]',
            '//html//body//div[5]//div[1]//div//div//select[@class="flatpickr-monthDropdown-months"]',
            '//html//body//div[5]//div[2]//div//div[2]//div//span[@class="flatpickr-day" and text()="'
        ]

        match get_element:
            case 'rbtn_land_loc_status_of_development':
                return rbtn_land_loc_status_of_development
            case 'dp_state_of_development_date_commencement':
                return dp_state_of_development_date_commencement
            case 'dp_state_of_development_date_completion':
                return dp_state_of_development_date_completion

    def get_berms_dev_pages_supporting_documents(self, get_element):
        field_elements_locations = {
            "INITIATE": '//div[@id="berms-application"]//div//div[1]//div[15]//button//span[2]//span[text()="Supporting Documents"]',
            "path_board_resolution_file": '//input[@id="supportingDocFilename0"]',
            "dp_board_resolution_validity": '//input[@id="supportingDocValidityDate0"]',
            "path_projected_financial_statement_file": '//input[@id="supportingDocFilename1"]',
            "dp_projected_financial_statement_validity": '//input[@id="supportingDocValidityDate1"]',
            "path_proof_of_land_ownership_file": '//input[@id="supportingDocFilename2"]',
            "dp_proof_of_land_ownership_validity": '//input[@id="supportingDocValidityDate2"]',
            "path_endorsement_development_ecozone_file": '//input[@id="supportingDocFilename3"]',
            "dp_endorsement_development_ecozone_validity": '//input[@id="supportingDocValidityDate3"]',
            "path_dar_cc_ec_hlurb_file": '//input[@id="supportingDocFilename4"]',
            "dp_dar_cc_ec_hlurb_validity": '//input[@id="supportingDocValidityDate4"]',
            "path_survey_returns_technical_description_file": '//input[@id="supportingDocFilename5"]',
            "dp_survey_returns_technical_description_validity": '//input[@id="supportingDocValidityDate5"]',
            "path_environmental_compliance_certificate_file": '//input[@id="supportingDocFilename6"]',
            "dp_environmental_compliance_certificate_validity":  '//input[@id="supportingDocValidityDate6"]',
            "path_certificate_national_water_resources_file": '//input[@id="supportingDocFilename7"]',
            "dp_certificate_national_water_resources_validity": '//input[@id="supportingDocValidityDate7"]',
            "path_prospective_locator_file": '//input[@id="supportingDocFilename8"]',
            "dp_prospective_locator_validity": '//input[@id="supportingDocValidityDate8"]',
            "path_project_cost_firb_file": '//input[@id="supportingDocFilename9"]',
            "dp_project_cost_firb_validity": '//input[@id="supportingDocValidityDate9"]',
            "path_general_information_sheet_file": '//input[@id="supportingDocFilename10"]',
            "path_site_development_plan_file": '//input[@id="supportingDocFilename11"]',
            "path_vicinity_map_file": '//input[@id="supportingDocFilename12"]',
            "path_notarized_anti_graft": '//input[@id="supportingDocFilename13"]',
            "path_notarized_application_form": '//input[@id="supportingDocFilename14"]',
            "path_applicants_under_taking_file": '//input[@id="supportingDocFilename15"]',
            "path_certificate_registration_sec": '//input[@id="supportingDocFilename16"]',
            "path_articles_incorporation": '//input[@id="supportingDocFilename17"]',
            "path_purpose_and_license_business_philippines": '//input[@id="supportingDocFilename18"]',
            "path_notarized_secretary_certificate": '//input[@id="supportingDocFilename19"]',
            "path_project_description": '//input[@id="supportingDocFilename20"]',
            "path_endorsement_from_government_agency": '//input[@id="supportingDocFilename21"]',
            "button_supporting_documents_proceed": '//div[@id="supporting-documents"]//div[3]//div//div//button//span[text()="Proceed"]',
            "switch_full_responsibility_for_misrepresentation": '//input[@id="suppDocsCheckbox"]'
        }

        return field_elements_locations[get_element], ''

    def get_berms_dev_pages_supporting_documents_others(self, get_element):
        dp_board_resolution_validity = [
            '//html//body//div[7]//div[1]//div//div//div//input[@class="numInput cur-year"]',
            '//html//body//div[7]//div[1]//div//div//select[@class="flatpickr-monthDropdown-months"]',
            '//html//body//div[7]//div[2]//div//div[2]//div//span[@class="flatpickr-day" and text()="'
        ]

        dp_projected_financial_statement_validity = [
            '//html//body//div[8]//div[1]//div//div//div//input[@class="numInput cur-year"]',
            '//html//body//div[8]//div[1]//div//div//select[@class="flatpickr-monthDropdown-months"]',
            '//html//body//div[8]//div[2]//div//div[2]//div//span[@class="flatpickr-day" and text()="'
        ]

        dp_proof_of_land_ownership_validity = [
            '//html//body//div[9]//div[1]//div//div//div//input[@class="numInput cur-year"]',
            '//html//body//div[9]//div[1]//div//div//select[@class="flatpickr-monthDropdown-months"]',
            '//html//body//div[9]//div[2]//div//div[2]//div//span[@class="flatpickr-day" and text()="'
        ]

        dp_endorsement_development_ecozone_validity = [
            '//html//body//div[10]//div[1]//div//div//div//input[@class="numInput cur-year"]',
            '//html//body//div[10]//div[1]//div//div//select[@class="flatpickr-monthDropdown-months"]',
            '//html//body//div[10]//div[2]//div//div[2]//div//span[@class="flatpickr-day" and text()="'
        ]

        dp_dar_cc_ec_hlurb_validity = [
            '//html//body//div[11]//div[1]//div//div//div//input[@class="numInput cur-year"]',
            '//html//body//div[11]//div[1]//div//div//select[@class="flatpickr-monthDropdown-months"]',
            '//html//body//div[11]//div[2]//div//div[2]//div//span[@class="flatpickr-day" and text()="'
        ]

        dp_survey_returns_technical_description_validity = [
            '//html//body//div[12]//div[1]//div//div//div//input[@class="numInput cur-year"]',
            '//html//body//div[12]//div[1]//div//div//select[@class="flatpickr-monthDropdown-months"]',
            '//html//body//div[12]//div[2]//div//div[2]//div//span[@class="flatpickr-day" and text()="'

        ]

        dp_environmental_compliance_certificate_validity = [
            '//html//body//div[13]//div[1]//div//div//div//input[@class="numInput cur-year"]',
            '//html//body//div[13]//div[1]//div//div//select[@class="flatpickr-monthDropdown-months"]',
            '//html//body//div[13]//div[2]//div//div[2]//div//span[@class="flatpickr-day" and text()="'
        ]

        dp_certificate_national_water_resources_validity = [
            '//html//body//div[14]//div[1]//div//div//div//input[@class="numInput cur-year"]',
            '//html//body//div[14]//div[1]//div//div//select[@class="flatpickr-monthDropdown-months"]',
            '//html//body//div[14]//div[2]//div//div[2]//div//span[@class="flatpickr-day" and text()="'
        ]

        dp_prospective_locator_validity = [
            '//html//body//div[15]//div[1]//div//div//div//input[@class="numInput cur-year"]',
            '//html//body//div[15]//div[1]//div//div//select[@class="flatpickr-monthDropdown-months"]',
            '//html//body//div[15]//div[2]//div//div[2]//div//span[@class="flatpickr-day" and text()="'
        ]

        dp_project_cost_firb_validity = [
            '//html//body//div[16]//div[1]//div//div//div//input[@class="numInput cur-year"]',
            '//html//body//div[16]//div[1]//div//div//select[@class="flatpickr-monthDropdown-months"]',
            '//html//body//div[16]//div[2]//div//div[2]//div//span[@class="flatpickr-day" and text()="'
        ]


        match get_element:
            case 'dp_board_resolution_validity':
                return dp_board_resolution_validity
            case 'dp_projected_financial_statement_validity':
                return dp_projected_financial_statement_validity
            case 'dp_proof_of_land_ownership_validity':
                return dp_proof_of_land_ownership_validity
            case 'dp_endorsement_development_ecozone_validity':
                return dp_endorsement_development_ecozone_validity
            case 'dp_dar_cc_ec_hlurb_validity':
                return dp_dar_cc_ec_hlurb_validity
            case 'dp_survey_returns_technical_description_validity':
                return dp_survey_returns_technical_description_validity
            case 'dp_environmental_compliance_certificate_validity':
                return dp_environmental_compliance_certificate_validity
            case 'dp_certificate_national_water_resources_validity':
                return dp_certificate_national_water_resources_validity
            case 'dp_prospective_locator_validity':
                return dp_prospective_locator_validity
            case 'dp_project_cost_firb_validity':
                return dp_project_cost_firb_validity

    def get_berms_dev_pages_confirmation(self, get_element):
        field_elements_locations = {
            "button_confirmation_application_proceed": '//button[@id="btnSubmitApplication"]//span[text()="Submit"]',
            "cbox_modal_acceptance_anti_graft": '//input[@id="acceptAntiGraft"]',
            "button_modal_acceptance_anti_graft_proceed": '//button[@id="antiGraftModalSubmit"]',
            "cbox_modal_acceptance_affidavit": '//input[@id="acceptAffidavit"]',
            "button_modal_acceptance_affidavit_proceed": '//button[@id="affidavitModalSubmit"]',
            "button_swal_acceptance_affidavit_proceed": '//html//body//div[7]//div//div[6]//button[1][text()="Yes"]',
            "button_swal_acceptance_affidavit_proceed_confirmation": '//html//body//div[7]//div//div[6]//button[1][text()="OK"]',
            "txt_berms_application_number": '//span[@id="confirmationReferenceNumber"]'
        }

        return_element_names = {
            "button_confirmation_application_proceed": '',
            "cbox_modal_acceptance_anti_graft": '',
            "button_modal_acceptance_anti_graft_proceed": '',
            "cbox_modal_acceptance_affidavit": '',
            "button_modal_acceptance_affidavit_proceed": '',
            "button_swal_acceptance_affidavit_proceed": '',
            "button_swal_acceptance_affidavit_proceed_confirmation": '',
            "txt_berms_application_number": ''
        }

        return field_elements_locations[get_element], return_element_names[get_element]