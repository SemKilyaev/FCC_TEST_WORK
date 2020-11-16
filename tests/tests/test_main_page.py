import pytest
import allure
from links import Links
from pages.main_page import MainPage
from data import Data


@pytest.mark.usefixtures("driver")
@allure.parent_suite("FCC")
@allure.suite("FCC test")
class Test_FCC:

    def setup(self):
        self.links = Links()
        self.main_page = MainPage(self.driver)
        self.data = Data()
        self.driver.get(self.links.landing)

    @allure.testcase('FCC login')
    @pytest.mark.smoke
    def test_authorization(self):
        with allure.step("Open login page"):
            self.main_page.should_be_login_link()
            self.main_page.go_to_login_page()
        with allure.step("Enter email"):
            self.main_page.enter_email(self.data.EMAIL)
        with allure.step("Enter password"):
            self.main_page.enter_password(self.data.PASSWORD)
        with allure.step("Click on submit button"):
            self.main_page.click_button_authorization()
            self.main_page.save_cookies("fcc")

    @allure.testcase('FCC_avatar')
    @pytest.mark.smoke
    def test_change_avatar(self):
        with allure.step("Login in account"):
            self.main_page.load_cookies(self.links.login, "fcc")

        with allure.step("Change avatar"):
            self.main_page.click_change_avatar()
            self.main_page.choose_file(self.data.FILE)
            self.main_page.click_button_apply()

    @allure.testcase('FCC_password')
    @pytest.mark.pasw
    @pytest.mark.parametrize("current_password, new_password", [
        (Data.PASSWORD, Data.NEW_PASSWORD),
        (Data.NEW_PASSWORD, Data.PASSWORD)
    ])
    def test_change_password(self, current_password, new_password):
        with allure.step("Login in account"):
            self.main_page.load_cookies(self.links.login, "fcc")

        with allure.step("Open settings page"):
            self.main_page.click_button_settings()

        with allure.step("Click on change password button"):
            self.main_page.click_change_password()

        with allure.step("Enter new password"):
            self.main_page.enter_old_password(current_password)

        with allure.step("Enter new password again"):
            self.main_page.enter_new_password(new_password)

        with allure.step("Save new password"):
            self.main_page.confirm_new_password(new_password)
            self.main_page.click_button_change_password()

    @allure.testcase('FCC_Timezone')
    @pytest.mark.timezone
    @pytest.mark.parametrize("timezone", [
        Data.TIMEZONE,
        Data.NEW_TIMEZONE
    ])
    def test_change_timezone(self, timezone):
        with allure.step("Login in account"):
            self.main_page.load_cookies(self.links.login, "fcc")

        with allure.step("Open settings page"):
            self.main_page.click_button_settings()

        with allure.step("Choose timezone"):
            self.main_page.choose_Timezone(timezone)

        with allure.step("Click Save"):
            self.main_page.click_Save()

    @allure.testcase('FCC_Change_Name')
    @pytest.mark.name
    @pytest.mark.parametrize("name, last_name", [
        (Data.NEW_NAME, Data.NEW_LAST_NAME),
        (Data.NAME, Data.LAST_NAME)
    ])
    def test_change_name(self, name, last_name):
        with allure.step("Login in account"):
            self.main_page.load_cookies(self.links.login, "fcc")

        with allure.step("Open settings page"):
            self.main_page.click_button_settings()

        with allure.step("Input name"):
            self.main_page.enter_name(name)

        with allure.step("Input last name"):
            self.main_page.enter_last_name(last_name)

        with allure.step("Click Save"):
            self.main_page.click_Save()
