import datetime
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.wait import TimeoutException as TimeExce
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from FrameWork.pkg_utilities.utility_script_general import UtilityPackage


class FrameWorkBaseDriver:
    def __init__(self, driver):
        self.driver = driver

    action_click = "arguments[0].click();"
    action_clear = "arguments[0].value='';"
    action_scroll_view = "arguments[0].scrollIntoView(true);"
    scripting_utility_tools = UtilityPackage()

    JS_DROP_FILE = """
        var target = arguments[0],
            offsetX = arguments[1],
            offsetY = arguments[2],
            document = target.ownerDocument || document,
            window = document.defaultView || window;

        var input = document.createElement('INPUT');
        input.type = 'file';
        input.onchange = function () {
          var rect = target.getBoundingClientRect(),
              x = rect.left + (offsetX || (rect.width >> 1)),
              y = rect.top + (offsetY || (rect.height >> 1)),
              dataTransfer = { files: this.files };

          ['dragenter', 'dragover', 'drop'].forEach(function (name) {
            var evt = document.createEvent('MouseEvent');
            evt.initMouseEvent(name, !0, !0, window, 0, 0, 0, x, y, !1, !1, !1, !1, 0, null);
            evt.dataTransfer = dataTransfer;
            target.dispatchEvent(evt);
          });

          setTimeout(function () { document.body.removeChild(input); }, 25);
        };
        document.body.appendChild(input);
        return input;
    """

    def action_chain_move_to_element(self, element_location):
        move_element_location = self.locate_element_by(By.XPATH, element_location)
        actions_element_location = ActionChains(self.driver)
        actions_element_location.move_to_element(move_element_location).perform()

    def execute_test_case(self, result):
        if result[0] == 1:
            print("Test Passed -", result[1])
        elif result[0] == '99':
            print("Test Blocked -", result[1])
        else:
            print("Test Failed -", result[1])

    def print_next_line(self):
        print(' ')

    def wait_for_presence_of_all_elements_xpath(self, locator_path):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.presence_of_all_elements_located((By.XPATH, locator_path)))

    def wait_element_to_be_clickable(self, locator_type, locator_path):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.element_to_be_clickable((locator_type, locator_path)))

    def wait_precense_of_element_located(self, locator_type, locator_path):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.presence_of_element_located((locator_type, locator_path)))

    def wait_precense_of_element_located_try_xpath(self, locator_path):
        wait = WebDriverWait(self.driver, 10)
        try:
            return wait.until(EC.presence_of_element_located((By.XPATH, locator_path)))
        # except NoSuchElementException or TimeoutException or ElementNotInteractableException:
        except:
            return 0
        # finally:
        #     return '99'

    def save_value_text_field(self, locator_path):
        wait_for_element_precense = self.wait_precense_of_element_located_try_xpath(locator_path)
        match wait_for_element_precense:
            case 0:
                return 0
            case _:
                return wait_for_element_precense.get_attribute("innerHTML")

    def locate_element_by(self, locator_type, locator_path):
        try:
            element_position = self.driver.find_element(locator_type, locator_path)
            return element_position
        except NoSuchElementException:
            return 0

    def locate_element_by_x_path(self, locator_path):
        try:
            element_position = self.driver.find_element(By.XPATH, locator_path)
            return element_position
        except:
            return 0

    def locate_all_element_by_x_path(self, locator_path):
        try:
            return self.driver.find_elements(By.XPATH, locator_path)
        except NoSuchElementException:
            return 0

    def select_dropdown_by_visible_text(self, select_field, select_option):
        wait = WebDriverWait(self.driver, 10)
        select_option_element = '//option[text()="' + select_option + '"]'
        wait.until(EC.presence_of_element_located((By.XPATH, select_option_element)))
        select_dropdown = Select(select_field)
        select_dropdown.select_by_visible_text(select_option)

    def select_dropdown_by_value(self, select_field, select_option):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, '//option[@value="' + str(select_option) + '"]')))
        select_dropdown = Select(select_field)
        select_dropdown.select_by_value(str(select_option))

    def input_data_in_date_field(self, date_element, date_input):
        self.execute_script_click(date_element)
        date_element.clear()
        date_element.send_keys(date_input)
        date_element.send_keys(Keys.TAB)

    def execute_script_scroll_into_view(self, element_location):
        if element_location.is_displayed() is False:
            self.driver.execute_script(self.action_scroll_view, element_location)

    def execute_script_scroll_into_view_02(self, element_position):
        element_location = self.locate_element_by_x_path(element_position)
        if element_location == 0:
            return 0
        else:
            if element_location.is_displayed() is False:
                try:
                    self.driver.execute_script(self.action_scroll_view, element_location)
                    element_location_find = self.wait_precense_of_element_located_try_xpath(element_position)
                    element_location_find.click()
                    return 1
                except NoSuchElementException or TimeoutException or ElementNotInteractableException:
                    return 0
            else:
                try:
                    self.action_chain_move_to_element(element_position)
                    element_location.click()
                    return 1
                except NoSuchElementException or TimeoutException or ElementNotInteractableException:
                    return 0

    def execute_script_js_drop(self, element_position):
        element_location = self.locate_element_by_x_path(element_position)
        return self.driver.execute_script(self.JS_DROP_FILE, element_location, 0, 0)

    def execute_script_click(self, element_position):
        self.driver.execute_script(self.action_click, element_position)

    def execute_script_clear(self, element_position):
        self.driver.execute_script(self.action_clear, element_position)

    def execute_script_date_value(self, date_value, date_field):
        self.driver.execute_script("arguments[0].value =" + '"' + date_value + '"' + ";",date_field)

    def convert_date_format(self, date_value):
        return datetime.datetime.strptime(date_value,"%m/%d/%Y").strftime("%Y-%m-%d")

    def function_string_start_with_this(self, get_action):
        function_action = get_action.startswith("input_path")
        return function_action

    def function_element_action_js_drop(self, element_location, file_location):
        try:
            drop_element_location = self.execute_script_js_drop(element_location)
            drop_element_location.send_keys(file_location)
            return 1
        except NoSuchElementException and TimeoutException and ElementNotInteractableException:
            return 0

    def function_element_action_no_wait_click(self, element_location):
        initiate_element_action_click = self.locate_element_by_x_path(element_location)
        if initiate_element_action_click == 0:
            return 0
        else:
            try:
                self.execute_script_click(initiate_element_action_click)
                return 1
            except NoSuchElementException and TimeoutException and ElementNotInteractableException:
                return 0

    def function_element_action_click(self, element_location):
        element_location_find = self.locate_element_by_x_path(element_location)
        if element_location_find == 0:
            return 0
        else:
            self.execute_script_scroll_into_view(element_location_find)
            try:
                element_location_action = self.wait_element_to_be_clickable(By.XPATH, element_location)
                self.execute_script_click(element_location_action)
                return 1
            except:
                return 0

    def function_element_action_click_02(self, element_location):
        return self.execute_script_scroll_into_view_02(element_location)

    def function_element_action_2_modal_confirm(self, confirm_modal, confirm_button):
        confirm_modal_status = self.wait_precense_of_element_located_try_xpath(confirm_modal)
        if confirm_modal_status == 0:
            return 0
        else:
            return self.function_element_action_click(confirm_button)

    def function_element_action_input(self, element_location, data_input):
        try:
            initiate_element_action_input = self.wait_precense_of_element_located_try_xpath(element_location)
            if initiate_element_action_input == 0:
                return initiate_element_action_input
            elif initiate_element_action_input == '99':
                return initiate_element_action_input
            else:
                initiate_element_action_input.send_keys(data_input)
                return 1
        except:
            return 0

    def function_element_action_no_wait_input(self, element_location, data_input):
        try:
            initiate_element_action_input = self.locate_element_by_x_path(element_location)
            initiate_element_action_input.send_keys(data_input)
            return 1
        except:
            return 0

    def function_element_action_clear_input(self, element_location, data_input):
        try:
            initiate_element_action_input = self.wait_precense_of_element_located(By.XPATH, element_location)
            initiate_element_action_input.clear()
            initiate_element_action_input.send_keys(data_input)
            return 1
        except NoSuchElementException and TimeoutException and ElementNotInteractableException:
            return 0

    def function_element_action_select_vt(self, element_location, data_input):
        try:
            initiate_element_action_select = self.wait_element_to_be_clickable(By.XPATH, element_location)
            self.select_dropdown_by_visible_text(initiate_element_action_select, data_input)
            return 1
        except:
            return 0

    def function_element_action_select_bv(self, element_location, data_input):
        try:
            initiate_element_action_select = self.wait_precense_of_element_located(By.XPATH, element_location)
            self.select_dropdown_by_value(initiate_element_action_select, data_input)
            return 1
        except NoSuchElementException and TimeoutException and ElementNotInteractableException:
            return 0

    def function_force_date_picker_date(self, date_input_position, date_input_value, date_input_element):
        try:
            self.execute_script_click(date_input_element)
        except:
            return 0
            exit()

        get_data_position_date_data = self.scripting_utility_tools.date_picker_data_strptime(date_input_value)

        intial_date_picker_date = date_input_position[3]

        date_picker_year = get_data_position_date_data[0]
        date_picker_month = get_data_position_date_data[1]
        date_picker_date = get_data_position_date_data[2]

        input_date_picker_month_txt = self.scripting_utility_tools.date_picker_select_month(date_picker_month)

        select_date_picker_date = intial_date_picker_date + input_date_picker_month_txt + ' ' + str(date_picker_date) + ', ' + date_picker_year + '"]'

        try:
            locate_select_date_picker_date = self.locate_element_by_x_path(select_date_picker_date)
            # self.driver.execute_script("arguments[0].setAttribute('class', 'flatpickr-day selected')", locate_select_date_picker_date)
            locate_select_date_picker_date.click()
            return 1
        except:
            return 0


    def function_date_picker_select_date(self, date_input_position, date_input_value, date_input_element):
        self.execute_script_click(date_input_element)
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
            print('year element found')
            try:
                input_date_picker_month = self.wait_precense_of_element_located(By.XPATH, select_date_picker_month)
                print('month element found ', select_date_picker_month)
                try:
                    input_date_picker_year.click()
                    input_date_picker_year.clear()
                    input_date_picker_year.send_keys(date_picker_year)
                    time.sleep(5)
                    try:
                        self.select_dropdown_by_visible_text(input_date_picker_month, input_date_picker_month_txt)
                        # print('month select success')
                        try:
                            select_date_picker_date = self.wait_precense_of_element_located(By.XPATH, select_date_picker_date)
                            # print('day element found')
                            select_date_picker_date.click()
                            return 1
                        except NoSuchElementException and ElementNotInteractableException:
                            # print('day element not found')
                            return 0
                    except NoSuchElementException and ElementNotInteractableException:
                        # print('month select not success')
                        return 0
                except NoSuchElementException and ElementNotInteractableException:
                    return 0
            except NoSuchElementException and ElementNotInteractableException:
                return 0
        except NoSuchElementException and ElementNotInteractableException:
            return 0

    def function_date_picker_select_date_v2(self, date_input_position, date_input_value, date_input_element):
        try:
            self.execute_script_click(date_input_element)
        except:
            return 0
            exit()

        get_data_position_date_data = self.scripting_utility_tools.date_picker_data_strptime(date_input_value)

        select_date_picker_year = date_input_position[0]
        select_date_picker_month = date_input_position[1]
        intial_date_picker_date = date_input_position[2]

        date_picker_year = get_data_position_date_data[0]
        date_picker_month = get_data_position_date_data[1]
        date_picker_date = get_data_position_date_data[2]

        select_date_picker_date = intial_date_picker_date + date_picker_date + '"]'

        input_date_picker_month_txt = self.scripting_utility_tools.date_picker_select_month(date_picker_month)

        try:
            input_date_picker_year = self.wait_precense_of_element_located(By.XPATH, select_date_picker_year)
            # print('year element found')
            try:
                input_date_picker_month = self.wait_precense_of_element_located(By.XPATH, select_date_picker_month)
                # print('month element found ', select_date_picker_month)
                try:
                    # self.execute_script_click(input_date_picker_year)
                    # print('click year')
                    # input_date_picker_year.click()
                    self.execute_script_click(input_date_picker_year)
                    input_date_picker_year.clear()
                    # print('clear year')
                    input_date_picker_year.send_keys(date_picker_year)
                    # print('input year')
                    try:
                        self.select_dropdown_by_visible_text(input_date_picker_month, input_date_picker_month_txt)
                        # print('month select success')
                        try:
                            select_date_picker_date = self.wait_precense_of_element_located(By.XPATH, select_date_picker_date)
                            # print('day element found')
                            # select_date_picker_date.click()
                            self.execute_script_click(select_date_picker_date)
                            return 1
                        # except NoSuchElementException and ElementNotInteractableException:
                        except:
                            # print('day element not found')
                            return 0
                    # except NoSuchElementException and ElementNotInteractableException:
                    except:
                        # print('month select not success')
                        return 0
                # except NoSuchElementException and ElementNotInteractableException:
                except:
                    return 0
            # except NoSuchElementException and ElementNotInteractableException:
            except:
                return 0
        # except NoSuchElementException and ElementNotInteractableException:
        except:
            return 0