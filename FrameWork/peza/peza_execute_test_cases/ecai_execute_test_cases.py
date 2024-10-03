from FrameWork.config_files.frame_work_base_driver import FrameWorkBaseDriver
from FrameWork.pkg_utilities.utility_script_general import UtilityPackage
from FrameWork.peza.home.home_main_page.home_main_page_login import HomePageLogin
from FrameWork.peza.menu_pages.menu_main_side_bar.menu_main_side_bar import MainMenuNavigation
from FrameWork.peza.menu_pages.menu_main_pages.menu_main_pages import MainMenuPages
from FrameWork.peza.ecai_pages.ecia_ent_pages import EcaiEnterpriseElementLocations

class ECAIExecuteTestCases(FrameWorkBaseDriver):
    def __init__(self, driver):
        self.driver = driver

    def peza_home_main_page_login(self):
        return HomePageLogin(self.driver)

    def peza_main_menu_side_bar(self):
        return MainMenuNavigation(self.driver)

    def peza_main_menu_pages(self):
        return MainMenuPages(self.driver)

    def peza_ecai_ent_pages(self):
        return EcaiEnterpriseElementLocations(self.driver)

    def get_utility_function(self):
        return UtilityPackage()

    def peza_function_element_action_no_wait_click(self, element_location):
        return self.function_element_action_no_wait_click(element_location)

    def peza_save_value_text_field(self, element_location):
        return self.save_value_text_field(element_location)

    def peza_function_element_action_click(self, element_location):
        return self.function_element_action_click(element_location)

    def peza_function_element_action_click_02(self, element_location):
        return self.function_element_action_click_02(element_location)

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
            case 'picker':
                get_field_element_location = self.locate_element_by_x_path(element_location)
                return self.peza_function_date_picker_select_date_v2(other_element_location, test_data, get_field_element_location)
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
            "peza_main_menu_side_bar": 'self.peza_main_menu_side_bar()',
            "peza_main_menu_pages": 'self.peza_main_menu_pages()',
            "peza_main_menu_top_profile": 'self.peza_main_menu_side_bar_berms()',
            "peza_ecai_ent_pages": 'self.peza_ecai_ent_pages()'
        }

        get_peza_main_function = {
            "utility_function": 'self.get_utility_function()',
            "peza_home_main_page_login": 'get_home_main_page_login',
            "peza_main_menu_side_bar": 'get_main_menu_side_bar',
            "peza_main_menu_pages": 'get_main_menu_pages',
            "peza_main_menu_top_profile": 'get_top_profile_menu',
            "peza_ecai_ent_pages": 'get_ecai_ent_pages'
        }

        get_peza_main_function_other = {
            "self.get_utility_function()": '',
            "get_home_main_page_login": '',
            "get_main_menu_side_bar": '',
            "get_main_menu_pages": '',
            "get_top_profile_menu": '',
            "get_ecai_ent_pages": 'get_ecai_ent_pages_others'
        }

        peza_main_function = get_peza_main_function[get_element]

        return get_peza_main_module[get_element], peza_main_function, get_peza_main_function_other[peza_main_function]

