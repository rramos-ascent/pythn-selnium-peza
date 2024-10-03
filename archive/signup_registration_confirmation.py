from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from FrameWork.config_files.base_driver import BaseDriver
from selenium.webdriver.remote.webelement import WebElement

class ProceedRegistrationConfirm(BaseDriver):
    def __init__(self, driver):
        self.driver = driver

    field_btn_proceed_application_confirmation = '//button[@id="termsAndConditionBtn"]'
    field_btn_submit_terms_conditions = '//button[@id="btnSubmit"]'
    field_cbox_submit_terms_conditions = '//input[@id="agreeCheckbox"]'
    field_btn_confirm_modal = '//html//body//div[15]//div//div[6]//button[1]'
    field_btn_submit_accept_terms_and_cond = '/html/body/div[2]/div/div/div[3]/button[2]/img'
    modal_proceed_application_confirmation = '//div[@id="termsAndConditionModal"]'

    RETURN_BTN_PROCEED_APPLICATION_CONFIRMATION = 'Proceed sign-up application review Terms and condition BUTTON CLICK'
    RETURN_CBOX_PROCEED_APPLICATION_CONFIRMATION = 'Proceed sign-up application review Terms and condition CHECKBOX CLICK'
    RETURN_BTN_SUBMIT_ACCEPT_TERMS_AND_COND = 'SWAL SUBMISSION YES BUTTON CLICK'
    RETURN_BTN_CONFIRM_MODAL = 'Confirmation modal BUTTON CLICK'

    def btn_proceed_application_confirmation(self):
        try:
            click_btn_proceed_application_confirmation = self.wait_element_to_be_clickable(By.XPATH, self.field_btn_proceed_application_confirmation)
            self.execute_script_click(click_btn_proceed_application_confirmation)
            return 1, self.RETURN_BTN_PROCEED_APPLICATION_CONFIRMATION
        except NoSuchElementException:
            return 0, self.RETURN_BTN_PROCEED_APPLICATION_CONFIRMATION

    def cbox_accept_terms_and_cond(self):
        try:
            terms_condition_modal: WebElement = self.locate_element_by(By.XPATH, self.modal_proceed_application_confirmation)
            try:
                btn_submit_terms_condition = terms_condition_modal.find_element(By.XPATH, self.field_btn_submit_terms_conditions)
                btn_submit_terms_condition_status = btn_submit_terms_condition.get_attribute("disabled")
                if btn_submit_terms_condition_status == "true":
                    try:
                        cbox_terms_condition_accept = terms_condition_modal.find_element(By.XPATH, self.field_cbox_submit_terms_conditions)
                        self.execute_script_click(cbox_terms_condition_accept)
                        return 1, self.RETURN_CBOX_PROCEED_APPLICATION_CONFIRMATION
                    except NoSuchElementException:
                        return 0, self.RETURN_CBOX_PROCEED_APPLICATION_CONFIRMATION
                else:
                    return 0, self.RETURN_CBOX_PROCEED_APPLICATION_CONFIRMATION
            except NoSuchElementException:
                return 0, self.RETURN_CBOX_PROCEED_APPLICATION_CONFIRMATION
        except NoSuchElementException:
            return 0, self.RETURN_CBOX_PROCEED_APPLICATION_CONFIRMATION

    def btn_submit_accept_terms_and_cond(self):
        try:
            click_btn_submit_tac = self.wait_element_to_be_clickable(By.XPATH, self.field_btn_submit_accept_terms_and_cond)
            self.execute_script_click(click_btn_submit_tac)
            return 1, self.RETURN_BTN_SUBMIT_ACCEPT_TERMS_AND_COND
        except NoSuchElementException:
            return 0, self.RETURN_BTN_SUBMIT_ACCEPT_TERMS_AND_COND

    def btn_modal_acceptance_confirmation(self):
        try:
            self.locate_element_by(By.XPATH, self.field_btn_confirm_modal)
            click_btn_confirmation_modal = self.wait_element_to_be_clickable(By.XPATH, self.field_btn_confirm_modal)
            self.execute_script_click(click_btn_confirmation_modal)
            return 1, self.RETURN_BTN_CONFIRM_MODAL
        except NoSuchElementException:
            return 0, self.RETURN_BTN_CONFIRM_MODAL