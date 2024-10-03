from FrameWork.config_files.frame_work_base_driver import FrameWorkBaseDriver
from FrameWork.pkg_utilities.utility_script_general import UtilityPackage
from FrameWork.peza.home.home_main_page.home_main_page_login import HomePageLogin
from FrameWork.peza.menu_pages.menu_main_side_bar.menu_main_side_bar_berms import MainMenuNavigationBerms
from FrameWork.peza.administration.manage_users_recent_applications import AdminManageUsersRecentApps
from FrameWork.peza.home.home_main_page.sign_up_all_pages import SignUpAllElementLocations


class ExecuteSignUpTestCases(FrameWorkBaseDriver):
    def __init__(self, driver):
        self.driver = driver

    def get_utility_function(self):
        return UtilityPackage()

    def peza_sign_up_all_pages(self):
        return SignUpAllElementLocations(self.driver)

    def peza_main_menu_side_bar_admin(self):
        return MainMenuNavigationBerms(self.driver)

    def peza_home_main_page_login(self):
        return HomePageLogin(self.driver)

    def peza_admin_manage_users_recent_apps(self):
        return AdminManageUsersRecentApps(self.driver)
    def peza_function_element_action_click(self, element_location):
        return self.function_element_action_click(element_location)

    def peza_function_element_action_no_wait_click(self, element_location):
        return self.function_element_action_no_wait_click(element_location)

    def peza_function_element_action_input(self, element_location, test_data):
        return self.function_element_action_input(element_location, test_data)

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
            case 'click':
                return self.peza_function_element_action_click(element_location)
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
            case 'utility':
                return self.utility_function_1(element_location, test_data)
            case _:
                return 0

    def utility_function_1(self, module_inc, test_data):
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
            "peza_main_menu_side_bar_admin": 'self.peza_main_menu_side_bar_admin()',
            "peza_main_menu_top_profile": 'self.peza_main_menu_side_bar_admin()',
            "peza_registration_select": 'self.peza_sign_up_all_pages()',
            "peza_company_information": 'self.peza_sign_up_all_pages()',
            "peza_company_information_sup_docs": 'self.peza_sign_up_all_pages()',
            "peza_company_information_contact_information": 'self.peza_sign_up_all_pages()',
            "peza_registration_finalization": 'self.peza_sign_up_all_pages()',
            "peza_type_service_provider": 'self.peza_sign_up_all_pages()',
            "peza_sp_representative_information": 'self.peza_sign_up_all_pages()',
            "peza_sp_principal_officer": 'self.peza_sign_up_all_pages()',
            "peza_admin_manage_users_recent_apps": 'self.peza_admin_manage_users_recent_apps()'
        }

        get_peza_main_function = {
            "utility_function": 'self.get_utility_function()',
            "peza_home_main_page_login": 'get_home_main_page_login',
            "peza_main_menu_side_bar_admin": 'get_main_menu_side_bar_admin',
            "peza_main_menu_top_profile": 'get_top_profile_menu',
            "peza_registration_select": 'get_registration_select',
            "peza_company_information": 'get_company_information',
            "peza_company_information_sup_docs": 'get_company_information_sup_docs',
            "peza_company_information_contact_information": 'get_company_information_contact_information',
            "peza_registration_finalization": 'get_registration_finalization',
            "peza_type_service_provider": 'get_type_service_provider',
            "peza_sp_representative_information": 'get_sp_representative_information',
            "peza_sp_principal_officer": 'get_sp_principal_officer',
            "peza_admin_manage_users_recent_apps": 'get_admin_manage_users_recent_apps'
        }

        get_peza_main_function_other = {
            "self.get_utility_function()": '',
            "get_home_main_page_login": '',
            "get_main_menu_side_bar_admin": '',
            "get_top_profile_menu": '',
            "get_registration_select": 'get_registration_select_others',
            "get_company_information": 'get_company_information_others',
            "get_company_information_sup_docs": 'get_company_information_sup_docs_others',
            "get_company_information_contact_information": '',
            "get_registration_finalization": '',
            "get_type_service_provider": 'get_type_service_provider_others',
            "get_sp_representative_information": '',
            "get_sp_principal_officer": '',
            "get_admin_manage_users_recent_apps": ''
        }

        peza_main_function = get_peza_main_function[get_element]

        return get_peza_main_module[get_element], peza_main_function, get_peza_main_function_other[peza_main_function]