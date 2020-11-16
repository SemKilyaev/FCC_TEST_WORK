from .base_page import BasePage
from locators import MainPageLocators
import time
import pickle
from source.file_path_to_jpg import MyPath


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def enter_email(self, email):
        email_link = self.browser.find_element(*MainPageLocators.EMAIL_LINK)
        assert self.is_element_present(*MainPageLocators.EMAIL_LINK), "Email link is not presented"
        email_link.send_keys(email)

    def enter_password(self, password):
        password_link = self.browser.find_element(*MainPageLocators.PASSWORD_LINK)
        assert self.is_element_present(*MainPageLocators.PASSWORD_LINK), "Password link is not presented"
        password_link.send_keys(password)

    def click_button_authorization(self):
        login_button_link = self.browser.find_element(*MainPageLocators.LOGIN_BUTTON_LINK)
        assert self.is_element_present(*MainPageLocators.LOGIN_BUTTON_LINK), "Login button is not presented"
        login_button_link.click()

    def click_change_avatar(self):
        change_button_link = self.browser.find_element(*MainPageLocators.CHANGE_BUTTON_LINK)
        assert self.is_element_present(*MainPageLocators.CHANGE_BUTTON_LINK), "Change avatar button is not presented"
        change_button_link.click()

    def choose_file(self, file):
        hide_button_link = self.browser.find_element(*MainPageLocators.HIDE_BUTTON_LINK)
        assert self.is_element_present(*MainPageLocators.HIDE_BUTTON_LINK), "Input avatar button is not presented"
        hide_button_link.send_keys(file)
        time.sleep(5)

    def click_button_apply(self):
        button_avatar_link = self.browser.find_element(*MainPageLocators.BUTTON_AVATAR_LINK)
        assert self.is_element_present(*MainPageLocators.BUTTON_AVATAR_LINK), "To apply button is not presented"
        button_avatar_link.click()

    def click_button_settings(self):
        settings_button_link = self.browser.find_element(*MainPageLocators.SETTINGS_BUTTON_LINK)
        assert self.is_element_present(*MainPageLocators.SETTINGS_BUTTON_LINK), "Settings button is not presented"
        settings_button_link.click()

    def click_change_password(self):
        password_change_link = self.browser.find_element(*MainPageLocators.PASSWORD_CHANGE_LINK)
        assert self.is_element_present(*MainPageLocators.PASSWORD_CHANGE_LINK), "Change password is not presented"
        password_change_link.click()

    def enter_old_password(self, old_password):
        password_now_link = self.browser.find_element(*MainPageLocators.PASSWORD_NOW_LINK)
        assert self.is_element_present(*MainPageLocators.PASSWORD_NOW_LINK), "Now password is not presented"
        password_now_link.send_keys(old_password)

    def enter_new_password(self, new_password):
        password_new_link = self.browser.find_element(*MainPageLocators.PASSWORD_NEW_LINK)
        assert self.is_element_present(*MainPageLocators.PASSWORD_NEW_LINK), "New password is not presented"
        password_new_link.send_keys(new_password)

    def confirm_new_password(self, new_password):
        password_confirm_link = self.browser.find_element(*MainPageLocators.PASSWORD_CONFIRM_LINK)
        assert self.is_element_present(*MainPageLocators.PASSWORD_CONFIRM_LINK), "Confirm password is not presented"
        password_confirm_link.send_keys(new_password)

    def click_button_change_password(self):
        button_change_password_link = self.browser.find_element(*MainPageLocators.BUTTON_CHANGE_PASSWORD_LINK)
        assert self.is_element_present(*MainPageLocators.BUTTON_CHANGE_PASSWORD_LINK), \
            "Change password button is not presented "
        button_change_password_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def make_cookie(self):
        print(self.browser.get_cookies())
        pickle.dump(self.browser.get_cookies(), open("D:\\FCC_TEST_WORK\\source\\cookies.pkl", "wb"))

    def in_for_cookie(self, file):
        # self.browser.get("https://www.freeconferencecall.com/ru/ru/login")
        # cookies = pickle.load(open(file, "rb"))
        # for cookie in cookies:
        #     self.browser.add_cookie(cookie)
        # time.sleep(10)
        cookies = pickle.load(open(file, "rb"))
        self.browser.get("https://www.freeconferencecall.com/ru/ru/login")
        for cookie in cookies:
            self.browser.add_cookie(cookie)
        time.sleep(5)
        self.browser.refresh()
        time.sleep(5)
