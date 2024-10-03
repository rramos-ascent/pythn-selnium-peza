import datetime
import time

class UtilityPackage():
    def get_action_and_location_reference(self, action_element_data):
        action_dictionary_extracted = {
            "input": action_element_data.find('input_'),
            "nwinput": action_element_data.find('nwinput_'),
            "click": action_element_data.find('click_'),
            "picker": action_element_data.find('picker_'),
            "fpicker": action_element_data.find('fpicker_'),
            "vtselect": action_element_data.find('vtselect_'),
            "bvselect": action_element_data.find('bvselect_'),
            "jsdragdrop": action_element_data.find('jsdragdrop_'),
            "tick":  action_element_data.find('tick_'),
            "nwtick": action_element_data.find('nwtick_'),
            "utility": action_element_data.find('utility_'),
            "value": action_element_data.find('value_'),
            "clrinput": action_element_data.find('clrinput_'),
            "click2": action_element_data.find('click2_')
        }

        get_action = [key for key, value in action_dictionary_extracted.items() if value == 0]
        get_element_loc = action_element_data.removeprefix(get_action[0] + '_')

        return get_action[0], get_element_loc

    def date_picker_data_strptime(self, date_input_value):
        date_input_value_to_string = datetime.datetime.strftime(date_input_value, "%m/%d/%Y")
        date_picker_year = datetime.datetime.strptime(date_input_value_to_string,"%m/%d/%Y").strftime("%Y")
        date_picker_month = datetime.datetime.strptime(date_input_value_to_string, "%m/%d/%Y").strftime("%m").lstrip("0")
        date_picker_date = datetime.datetime.strptime(date_input_value_to_string, "%m/%d/%Y").strftime("%d").lstrip("0")
        return date_picker_year, date_picker_month, date_picker_date

    def date_picker_select_month(self, date_month_num):
        match date_month_num:
            case '1':
                return 'January'
            case '2':
                return 'February'
            case '3':
                return 'March'
            case '4':
                return 'April'
            case '5':
                return 'May'
            case '6':
                return 'June'
            case '7':
                return 'July'
            case '8':
                return 'August'
            case '9':
                return 'September'
            case '10':
                return 'October'
            case '11':
                return 'November'
            case '12':
                return 'December'

    def terminate_first_displayed_line(self):
        print(' ')

    def get_if_passed_failed(self, return_status):
        match return_status:
            case 1:
                return "Passed"
            case 0:
                return "Failed"
            case '99':
                return "Blocked"
            case _:
                return return_status

    def process_time_out_provided_time(self, sleep_time):
        time.sleep(sleep_time)
        # print('Process time-out by ' + str(sleep_time) + 'secs')
        return 1
