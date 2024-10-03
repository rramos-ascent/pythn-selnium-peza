from FrameWork.config_files.frame_work_base_driver import FrameWorkBaseDriver
from FrameWork.pkg_utilities.utility_script_general import UtilityPackage
from FrameWork.peza.home.home_main_page.home_main_page_login import HomePageLogin
from FrameWork.peza.menu_pages.menu_main_side_bar.menu_main_side_bar_berms import MainMenuNavigationBerms
from FrameWork.peza.menu_pages.menu_main_pages.menu_main_pages_berms import MainMenuPagesBerms
from FrameWork.peza.berms_pages.berms_dev_pages import BermsDeveloperElementLocations
from FrameWork.peza.berms_pages.berms_ent_pages import BermsEntpriseElementLocations
from FrameWork.peza.berms_pages.berms_sp_pages import BermsSProviderElementLocations


class BermsExecuteTestCases(FrameWorkBaseDriver):
    def __init__(self, driver):
        self.driver = driver

    def peza_home_main_page_login(self):
        return HomePageLogin(self.driver)

    def peza_berms_ent(self):
        return BermsEntpriseElementLocations(self.driver)

    def peza_berms_dev(self):
        return BermsDeveloperElementLocations(self.driver)

    def peza_berms_sp(self):
        return BermsSProviderElementLocations(self.driver)

    def peza_main_menu_side_bar_berms(self):
        return MainMenuNavigationBerms(self.driver)

    def peza_menu_main_pages_berms(self):
        return MainMenuPagesBerms(self.driver)

    def get_utility_function(self):
        return UtilityPackage()

    def peza_function_element_action_no_wait_click(self, element_location):
        return self.function_element_action_no_wait_click(element_location)

    def peza_save_value_text_field(self, element_location):
        return self.save_value_text_field(element_location)

    def peza_function_element_action_click(self, element_location):
        return self.function_element_action_click(element_location)

    def peza_function_element_action_input(self, element_location, test_data):
        return self.function_element_action_input(element_location, test_data)

    def peza_function_element_action_click_02(self, element_location):
        return self.function_element_action_click_02(element_location)

    def peza_function_element_action_no_wait_input(self, element_location, test_data):
        return self.function_element_action_no_wait_input(element_location, test_data)

    def peza_function_element_action_clear_input(self, element_location, test_data):
        return self.function_element_action_clear_input(element_location, test_data)

    def peza_function_element_action_select_vt(self, element_location, test_data):
        locate_select_field = self.locate_element_by_x_path(element_location)
        if locate_select_field == 0:
            return 0
        else:
            return self.function_element_action_select_vt(element_location, test_data)

    def peza_function_element_action_select_value(self, element_location, test_data):
        locate_select_field = self.locate_element_by_x_path(element_location)
        if locate_select_field == 0:
            return 0
        else:
            return self.function_element_action_select_bv(element_location, test_data)

    def peza_function_element_action_js_drop(self, element_location, test_data):
        return self.function_element_action_js_drop(element_location, test_data)

    def peza_function_date_picker_select_date_v2(self, date_input_position, date_input_value, date_input_element):
        return self.function_date_picker_select_date_v2(date_input_position, date_input_value, date_input_element)

    def peza_function_force_date_picker_date(self, date_input_position, date_input_value, date_input_element):
        return self.function_force_date_picker_date(date_input_position, date_input_value, date_input_element)

    def function_call_test_cases(self, execute_test_case):
        get_utility_function = UtilityPackage()

        get_modules = self.peza_main_dictionary(execute_test_case[0])
        formatted_action = get_utility_function.get_action_and_location_reference(execute_test_case[1])

        field_element_location = self.function_import_modules(get_modules[0], get_modules[1], formatted_action[1])
        other_element_location = self.function_import_modules(get_modules[0], get_modules[2], formatted_action[1])

        execution_result = self.function_execute_element_actions(formatted_action[0], field_element_location[0], execute_test_case[2], other_element_location)
        return execution_result, ''

    def function_execute_element_actions(self, test_action, element_location, test_data, other_element_location):
        match test_action:
            case 'nwinput':
                return self.peza_function_element_action_no_wait_input(element_location, test_data)
            case 'input':
                return self.peza_function_element_action_input(element_location, test_data)
            case 'clrinput':
                return self.peza_function_element_action_clear_input(element_location, test_data)
            case 'picker':
                get_field_element_location = self.locate_element_by_x_path(element_location)
                return self.peza_function_date_picker_select_date_v2(other_element_location, test_data, get_field_element_location)
            case 'fpicker':
                get_field_element_location = self.locate_element_by_x_path(element_location)
                return self.peza_function_force_date_picker_date(other_element_location, test_data, get_field_element_location)
            case 'click':
                return self.peza_function_element_action_click(element_location)
            case 'click2':
                return self.peza_function_element_action_click_02(element_location)
            case 'tick':
                get_field_element_location = other_element_location[test_data]
                return self.peza_function_element_action_click(get_field_element_location)
            case 'nwtick':
                get_field_element_location = other_element_location[test_data]
                return self.peza_function_element_action_no_wait_click(get_field_element_location)
            case 'vtselect':
                return self.peza_function_element_action_select_vt(element_location, test_data)
            case 'bvselect':
                return self.peza_function_element_action_select_value(element_location, test_data)
            case 'jsdragdrop':
                return self.peza_function_element_action_js_drop(element_location, test_data)
            case 'value':
                return self.peza_save_value_text_field(element_location)
            case 'utility':
                return self.utility_function(element_location, test_data)
            case _:
                return 0

    def utility_function(self, module_inc, test_data):
        match test_data:
            case '':
                module_complete = module_inc + '(' + ')'
                execution_result = eval(module_complete)
                return execution_result
            case _:
                module_complete = module_inc + '(' + str(test_data) + ')'
                execution_result = eval(module_complete)
                return execution_result

    def function_import_modules(self, class_entry, function_entry, location_entry):
        match function_entry:
            case '':
                return ''
            case 'self.get_utility_function()':
                module = function_entry + '.' + location_entry
                return module, ''
            case _:
                module = class_entry + '.' + function_entry + '("' + location_entry + '")'
                execution_result = eval(module)
                return execution_result

    def peza_main_dictionary(self, get_element):
        get_peza_main_module = {
            "utility_function": 'self.get_utility_function()',
            "peza_home_main_page_login": 'self.peza_home_main_page_login()',
            "peza_main_menu_side_bar_berms": 'self.peza_main_menu_side_bar_berms()',
            "peza_main_menu_top_profile": 'self.peza_main_menu_side_bar_berms()',
            "peza_menu_main_pages_berms": 'self.peza_menu_main_pages_berms()',
            "peza_berms_ent_supporting_documents": 'self.peza_berms_ent()',
            "peza_berms_ent_project_cost_financing": 'self.peza_berms_ent()',
            "peza_berms_ent_pages_market_aspect": 'self.peza_berms_ent()',
            "peza_berms_ent_pages_area_utilities_waste_disposal": 'self.peza_berms_ent()',
            "peza_berms_ent_pages_machinery_production_schedule": 'self.peza_berms_ent()',
            "peza_berms_ent_pages_manufacturing_process_service_flow": 'self.peza_berms_ent()',
            "peza_berms_ent_pages_manpower_requirement": 'self.peza_berms_ent()',
            "peza_berms_ent_pages_stockholders_principal_officers": 'self.peza_berms_ent()',
            "peza_berms_ent_pages_application_existing_bus_reg": 'self.peza_berms_ent()',
            "peza_berms_ent_pages_application": 'self.peza_berms_ent()',
            "peza_berms_ent_pages_confirmation": 'self.peza_berms_ent()',
            "peza_berms_dev_pages_application": 'self.peza_berms_dev()',
            "peza_berms_dev_pages_off_rep": 'self.peza_berms_dev()',
            "peza_berms_dev_pages_capital_structure": 'self.peza_berms_dev()',
            "peza_berms_dev_pages_principal_officer": 'self.peza_berms_dev()',
            "peza_berms_dev_pages_the_land": 'self.peza_berms_dev()',
            "peza_berms_dev_pages_the_project": 'self.peza_berms_dev()',
            "peza_berms_dev_pages_supporting_documents": 'self.peza_berms_dev()',
            "peza_berms_dev_pages_confirmation": 'self.peza_berms_dev()',
            "peza_berms_sp_applications": 'self.peza_berms_sp()',
            "peza_berms_sp_rep_principal_officers": 'self.peza_berms_sp()',
            "peza_berms_sp_supporting_documents": 'self.peza_berms_sp()',
            "peza_processing_views": 'self.peza_berms_ent()',
            "peza_processing_views_staff": 'self.peza_berms_ent()',
            "peza_processing_views_chief": 'self.peza_berms_ent()',
            "peza_processing_views_approver": 'self.peza_berms_ent()',
            "peza_processing_views_verifier": 'self.peza_berms_ent()'
        }

        get_peza_main_function = {
            "utility_function": 'self.get_utility_function()',
            "peza_home_main_page_login": 'get_home_main_page_login',
            "peza_main_menu_side_bar_berms": 'get_main_menu_side_bar_berms',
            "peza_menu_main_pages_berms": 'get_menu_main_pages_berms',
            "peza_main_menu_top_profile": 'get_top_profile_menu',
            "peza_berms_ent_supporting_documents": 'get_application_supporting_documents',
            "peza_berms_ent_project_cost_financing": 'get_application_project_cost_financing',
            "peza_berms_ent_pages_market_aspect": 'get_application_market_aspect',
            "peza_berms_ent_pages_area_utilities_waste_disposal": 'get_application_area_utilities_waste_disposal',
            "peza_berms_ent_pages_machinery_production_schedule": 'get_application_machinery_production_schedule',
            "peza_berms_ent_pages_manufacturing_process_service_flow": 'get_application_manufacturing_process_service_flow',
            "peza_berms_ent_pages_manpower_requirement": 'get_application_manpower_timetable',
            "peza_berms_ent_pages_stockholders_principal_officers": 'get_stockholders_principal_officers',
            "peza_berms_ent_pages_application_existing_bus_reg": 'get_application_exi_bus_reg',
            "peza_berms_ent_pages_application": 'get_berms_ent_pages_application',
            "peza_berms_ent_pages_confirmation": 'get_berms_ent_pages_confirmation',
            "peza_berms_dev_pages_application": 'get_berms_dev_pages_application',
            "peza_berms_dev_pages_off_rep": 'get_berms_dev_pages_off_rep',
            "peza_berms_dev_pages_capital_structure": 'get_berms_dev_pages_capital_structure',
            "peza_berms_dev_pages_principal_officer": 'get_berms_dev_pages_principal_officer',
            "peza_berms_dev_pages_the_land": 'get_berms_dev_pages_the_land',
            "peza_berms_dev_pages_the_project": 'get_berms_dev_pages_the_project',
            "peza_berms_dev_pages_supporting_documents": 'get_berms_dev_pages_supporting_documents',
            "peza_berms_dev_pages_confirmation": 'get_berms_dev_pages_confirmation',
            "peza_berms_sp_applications": 'get_berms_sp_applications',
            "peza_berms_sp_rep_principal_officers": 'get_berms_sp_rep_principal_officers',
            "peza_berms_sp_supporting_documents": 'get_berms_sp_supporting_documents',
            "peza_processing_views": 'get_processing_views',
            "peza_processing_views_staff": 'get_processing_views_staff',
            "peza_processing_views_chief": 'get_processing_views_chief',
            "peza_processing_views_approver": 'get_processing_views_approver',
            "peza_processing_views_verifier": 'get_processing_views_verifier'
        }

        get_peza_main_function_other = {
            "self.get_utility_function()": '',
            "get_home_main_page_login": '',
            "get_main_menu_side_bar_berms": '',
            "get_menu_main_pages_berms": '',
            "get_top_profile_menu": '',
            "get_application_supporting_documents": 'get_application_supporting_documents_locations',
            "get_application_project_cost_financing": '',
            "get_application_market_aspect": '',
            "get_application_area_utilities_waste_disposal": '',
            "get_application_machinery_production_schedule": '',
            "get_application_manufacturing_process_service_flow": '',
            "get_application_manpower_timetable": 'get_application_other_locations',
            "get_stockholders_principal_officers": 'get_application_other_locations',
            "get_application_exi_bus_reg": 'get_application_other_locations',
            "get_berms_ent_pages_application": 'get_application_other_locations',
            "get_berms_ent_pages_confirmation": '',
            "get_berms_dev_pages_application": 'get_berms_dev_pages_application_others',
            "get_berms_dev_pages_off_rep": '',
            "get_berms_dev_pages_capital_structure": '',
            "get_berms_dev_pages_principal_officer": '',
            "get_berms_dev_pages_the_land": 'get_berms_dev_pages_the_land_others',
            "get_berms_dev_pages_the_project": 'get_berms_dev_pages_the_project_others',
            "get_berms_dev_pages_supporting_documents": 'get_berms_dev_pages_supporting_documents_others',
            "get_berms_dev_pages_confirmation": '',
            "get_berms_sp_applications": 'get_berms_sp_applications_others',
            "get_berms_sp_rep_principal_officers": '',
            "get_berms_sp_supporting_documents": '',
            "get_processing_views": '',
            "get_processing_views_staff": '',
            "get_processing_views_chief": '',
            "get_processing_views_approver": '',
            "get_processing_views_verifier": 'get_processing_views_verifier_others'
        }

        peza_main_function = get_peza_main_function[get_element]

        return get_peza_main_module[get_element], peza_main_function, get_peza_main_function_other[peza_main_function]

