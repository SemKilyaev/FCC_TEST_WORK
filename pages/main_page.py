import time
import allure

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from locators import Locators
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import Select


class MainPage(BasePage):
    LOGIN_LINK = (By.ID, Locators.LOGIN_LINK)
    EMAIL_LINK = (By.CLASS_NAME, Locators.EMAIL_LINK)
    PASSWORD_LINK = (By.ID, Locators.PASSWORD_LINK)
    LOGIN_BUTTON_LINK = (By.ID, Locators.LOGIN_BUTTON_LINK)
    CHANGE_BUTTON_LINK = (By.XPATH, Locators.CHANGE_BUTTON_LINK)
    HIDE_BUTTON_LINK = (By.XPATH, Locators.HIDE_BUTTON_LINK)
    BUTTON_AVATAR_LINK = (By.XPATH, Locators.BUTTON_AVATAR_LINK)
    SETTINGS_BUTTON_LINK = (By.XPATH, Locators.SETTINGS_BUTTON_LINK)
    PASSWORD_CHANGE_LINK = (By.XPATH, Locators.PASSWORD_CHANGE_LINK)
    PASSWORD_NOW_LINK = (By.XPATH, Locators.PASSWORD_NOW_LINK)
    PASSWORD_NEW_LINK = (By.XPATH, Locators.PASSWORD_NEW_LINK)
    PASSWORD_CONFIRM_LINK = (
        By.XPATH, Locators.PASSWORD_CONFIRM_LINK)
    BUTTON_CHANGE_PASSWORD_LINK = (
        By.XPATH, Locators.BUTTON_CHANGE_PASSWORD_LINK)
    SELECT_TIMEZONE = (By.XPATH, Locators.SELECT_TIMEZONE)
    BUTTON_SAVE = (By.XPATH, Locators.BUTTON_SAVE)
    NAME_INPUT = (By.XPATH, Locators.NAME_INPUT)
    LAST_NAME_INPUT = (By.XPATH, Locators.LAST_NAME_INPUT)

    def go_to_login_page(self):
        login_link = self.driver.find_element(*self.LOGIN_LINK)
        login_link.click()

    def enter_email(self, email):
        email_link = self.driver.find_element(*self.EMAIL_LINK)
        assert self.is_element_present(*self.EMAIL_LINK), "Email link is not presented"
        email_link.send_keys(email)
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="Screenshot", attachment_type=AttachmentType.PNG)

    def enter_password(self, password):
        password_link = self.driver.find_element(*self.PASSWORD_LINK)
        assert self.is_element_present(*self.PASSWORD_LINK), "Password link is not presented"
        password_link.send_keys(password)
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="Screenshot", attachment_type=AttachmentType.PNG)

    def click_button_authorization(self):
        login_button_link = self.driver.find_element(*self.LOGIN_BUTTON_LINK)
        assert self.is_element_present(*self.LOGIN_BUTTON_LINK), "Login button is not presented"
        login_button_link.click()
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="Screenshot", attachment_type=AttachmentType.PNG)

    def click_change_avatar(self):
        change_button_link = self.driver.find_element(*self.CHANGE_BUTTON_LINK)
        assert self.is_element_present(*self.CHANGE_BUTTON_LINK), "Change avatar button is not presented"
        change_button_link.click()
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="Screenshot", attachment_type=AttachmentType.PNG)

    def choose_file(self, file):
        hide_button_link = self.driver.find_element(*self.HIDE_BUTTON_LINK)
        assert self.is_element_present(*self.HIDE_BUTTON_LINK), "Input avatar button is not presented"
        hide_button_link.send_keys(file)
        time.sleep(5)
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="Screenshot", attachment_type=AttachmentType.PNG)

    def click_button_apply(self):
        button_avatar_link = self.driver.find_element(*self.BUTTON_AVATAR_LINK)
        assert self.is_element_present(*self.BUTTON_AVATAR_LINK), "To apply button is not presented"
        button_avatar_link.click()

    def click_button_settings(self):
        settings_button_link = self.driver.find_element(*self.SETTINGS_BUTTON_LINK)
        assert self.is_element_present(*self.SETTINGS_BUTTON_LINK), "Settings button is not presented"
        settings_button_link.click()
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="Screenshot", attachment_type=AttachmentType.PNG)

    def click_change_password(self):
        password_change_link = self.driver.find_element(*self.PASSWORD_CHANGE_LINK)
        assert self.is_element_present(*self.PASSWORD_CHANGE_LINK), "Change password is not presented"
        password_change_link.click()
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="Screenshot", attachment_type=AttachmentType.PNG)

    def enter_old_password(self, old_password):
        password_now_link = self.driver.find_element(*self.PASSWORD_NOW_LINK)
        assert self.is_element_present(*self.PASSWORD_NOW_LINK), "Now password is not presented"
        password_now_link.send_keys(old_password)
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="Screenshot", attachment_type=AttachmentType.PNG)

    def enter_new_password(self, new_password):
        password_new_link = self.driver.find_element(*self.PASSWORD_NEW_LINK)
        assert self.is_element_present(*self.PASSWORD_NEW_LINK), "New password is not presented"
        password_new_link.send_keys(new_password)
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="Screenshot", attachment_type=AttachmentType.PNG)

    def confirm_new_password(self, new_password):
        password_confirm_link = self.driver.find_element(*self.PASSWORD_CONFIRM_LINK)
        assert self.is_element_present(*self.PASSWORD_CONFIRM_LINK), "Confirm password is not presented"
        password_confirm_link.send_keys(new_password)
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="Screenshot", attachment_type=AttachmentType.PNG)

    def click_button_change_password(self):
        button_change_password_link = self.driver.find_element(*self.BUTTON_CHANGE_PASSWORD_LINK)
        assert self.is_element_present(*self.BUTTON_CHANGE_PASSWORD_LINK), \
            "Change password button is not presented "
        button_change_password_link.click()
        time.sleep(3)
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="Screenshot", attachment_type=AttachmentType.PNG)

    def should_be_login_link(self):
        assert self.is_element_present(*self.LOGIN_LINK), "Login link is not presented"
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="Screenshot", attachment_type=AttachmentType.PNG)

    def choose_Timezone(self, timezone):
        select_timezone = Select(self.driver.find_element(*self.SELECT_TIMEZONE))
        assert self.is_element_present(*self.SELECT_TIMEZONE), \
            "Select Timezone button is not presented "
        select_timezone.select_by_value(timezone)
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="Screenshot", attachment_type=AttachmentType.PNG)

    def click_Save(self):
        button_save = self.driver.find_element(*self.BUTTON_SAVE)
        assert self.is_element_present(*self.BUTTON_SAVE), \
            "Select Timezone button is not presented "
        button_save.click()
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="Screenshot", attachment_type=AttachmentType.PNG)

    def enter_name(self, name):
        name_input = self.driver.find_element(*self.NAME_INPUT)
        assert self.is_element_present(*self.NAME_INPUT), "Input Name is not presented"
        name_input.clear()
        name_input.send_keys(name)
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="Screenshot", attachment_type=AttachmentType.PNG)

    def enter_last_name(self, last_name):
        last_name_input = self.driver.find_element(*self.LAST_NAME_INPUT)
        assert self.is_element_present(*self.LAST_NAME_INPUT), "Input Name is not presented"
        last_name_input.clear()
        last_name_input.send_keys(last_name)
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="Screenshot", attachment_type=AttachmentType.PNG)
