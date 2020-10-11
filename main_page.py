from .base_page import BasePage
from .locators import MainPageLocators
import os
import time


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def authorization(self):
        email_link = self.browser.find_element(*MainPageLocators.EMAIL_LINK)
        email_link.send_keys('your email')
        password_link = self.browser.find_element(*MainPageLocators.PASSWORD_LINK)
        password_link.send_keys('your password')
        login_button_link = self.browser.find_element(*MainPageLocators.LOGIN_BUTTON_LINK)
        login_button_link.click()

    def change_avatar(self):
        change_button_link = self.browser.find_element(*MainPageLocators.CHANGE_BUTTON_LINK)
        change_button_link.click()
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'file')
        hide_button_link = self.browser.find_element(*MainPageLocators.HIDE_BUTTON_LINK)
        hide_button_link.send_keys(file_path)
        time.sleep(5)
        button_avatar_link = self.browser.find_element(*MainPageLocators.BUTTON_AVATAR_LINK)
        button_avatar_link.click()

    def change_password(self):
        settings_button_link = self.browser.find_element(*MainPageLocators.SETTINGS_BUTTON_LINK)
        settings_button_link.click()
        password_change_link = self.browser.find_element(*MainPageLocators.PASSWORD_CHANGE_LINK)
        password_change_link.click()
        password_now_link = self.browser.find_element(*MainPageLocators.PASSWORD_NOW_LINK)
        password_now_link.send_keys('your password')
        password_new_link = self.browser.find_element(*MainPageLocators.PASSWORD_NEW_LINK)
        password_new_link.send_keys('your new password')
        password_confirm_link = self.browser.find_element(*MainPageLocators.PASSWORD_CONFIRM_LINK)
        password_confirm_link.send_keys('your new password')
        button_change_password_link = self.browser.find_element(*MainPageLocators.BUTTON_CHANGE_PASSWORD_LINK)
        button_change_password_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
