from FrameWork.config_files.frame_work_base_driver import FrameWorkBaseDriver


class ImportPermitElementLocations(FrameWorkBaseDriver):
    def __init__(self, driver):
        self.driver = driver

    def get_create_new_import_permit(self, get_element):
        field_elements_locations = {
            "option_eco_zone": '//select[@id="zoneId"]',
            "option_enterpirse_type": '//select[@id="enterpriseTypeId"]',
            "option_puporse_importation": '//select[@id="purposeOfImportationId"]',
            "text_shipper_name": '//input[@id="shipperName"]',
            "textarea_shipper_address": '//textarea[@id="shipperAddress"]',
            "option_country_of_origin": '//select[@id="portOfOrigin"]',
            "option_port_of_discharge": '//select[@id="portOfDischarge"]',
            "text_delivery_address_instruction": '//input[@id="deliveryAddress"]',
            "dp_departure_date": '//form[@id="form_importPermit"]//div[1]//div[1]//div[8]//div[1]//input[2]',
            "dp_estimated_date_arrival": '//form[@id="form_importPermit"]//div[1]//div[1]//div[8]//div[2]//input[2]',
            "text_registry_number": '//input[@id="registryNo"]',
            "text_way_bill_number": '//input[@id="wayBillNo"]',
            "text_invoice_number": '//input[@id="invoiceNo"]',
            "textarea_import_permit_remarks": '//textarea[@id="remarks"]',
            "option_payment_method": '//select[@id="paymentMethodId"]',
            "option_currency": '//select[@id="currencyId"]',
            "search_data_table_importable": '//div[@id="importablestbl_filter"]//label//input',
            "link_first_item_data_table_importable": '//table[@id="importablestbl"]//tbody//tr//td[2]//a',
            "text_item_purchase_number": '//input[@id="add_purchase_order_no"]',
            "text_item_item_use": '//input[@id="add_item_use"]',
            "text_item_quantity": '//input[@id="add_quantity"]',
            "option_unit_of_measure": '//select[@id="add_package"]',
            "text_item_gross_weight": '//input[@id="add_gross_weight"]',
            "text_item_invoice_value": '//input[@id="add_invoice_value"]',
            "button_add_ip_item": '//form[@id="form_addItemImportables"]//div[2]//button[@id="btnSave"]',
            "button_submit_import_permit": '//button[@id="btnSubmitApplication"]',
            "button_submit_import_permit_confirm": '//button[text()="Yes"]',
            "button_submit_import_permit_confirm_ok": '//button[text()="OK"]',
        }

        return_element_names = {
        }

        return field_elements_locations[get_element], ''

    def get_create_new_import_permit_others(self, get_element):
        field_dp_departure_date = [
            '//html//body//div[3]//div[1]//div//div//div//input[@class="numInput cur-year"]',
            '//html//body//div[3]//div[1]//div//div//select[@class="flatpickr-monthDropdown-months"]',
            '//html//body//div[3]//div[2]//div//div[2]//div//span[@class="flatpickr-day" and text()="'
        ]

        field_dp_estimated_date_arrival = [
            '//html//body//div[4]//div[1]//div//div//div//input[@class="numInput cur-year"]',
            '//html//body//div[4]//div[1]//div//div//select[@class="flatpickr-monthDropdown-months"]',
            '//html//body//div[4]//div[2]//div//div[2]//div//span[@class="flatpickr-day" and text()="'
        ]

        match get_element:
            case 'dp_departure_date':
                return field_dp_departure_date
            case 'dp_estimated_date_arrival':
                return field_dp_estimated_date_arrival