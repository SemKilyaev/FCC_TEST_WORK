from pages.main_page import MainPage
import pytest
import allure
from allure_commons.types import AttachmentType


email = 'darkvanted@gmail.com'
password = 'cehr032197'
password_change = '032197cehr'
link = "https://www.freeconferencecall.com/ru"
file = '1234.jpg'



@allure.testcase(link, 'FCC')
@pytest.mark.parametrize('email, password, link', [(email, password, link)])
@pytest.mark.aut
def test_authorization(browser, email, password, link):
    with allure.step("Launch site"):
        page = MainPage(browser, link)
        page.open()
        allure.attach(browser.get_screenshot_as_png(), name="ScreenshotAut1", attachment_type=AttachmentType.PNG)
    with allure.step("Authorization"):
        page.should_be_login_link()
        page.go_to_login_page()
        allure.attach(browser.get_screenshot_as_png(), name="ScreenshotAut2", attachment_type=AttachmentType.PNG)
        page.enter_email(email)
        page.enter_password(password)
        allure.attach(browser.get_screenshot_as_png(), name="ScreenshotAut3", attachment_type=AttachmentType.PNG)
        page.click_button_authorization()
        allure.attach(browser.get_screenshot_as_png(), name="ScreenshotAut4", attachment_type=AttachmentType.PNG)

@allure.testcase(link, 'FCC_avatar')
@pytest.mark.avatar
@pytest.mark.parametrize('email, password, link, file', [(email, password, link, file)])
def test_change_avatar(browser, email, password, link, file):
    with allure.step("Launch site"):
        page = MainPage(browser, link)
        page.open()
        allure.attach(browser.get_screenshot_as_png(), name="ScreenshotAvatar1", attachment_type=AttachmentType.PNG)
    with allure.step("Authorization"):
        page.go_to_login_page()
        allure.attach(browser.get_screenshot_as_png(), name="ScreenshotAvatar2", attachment_type=AttachmentType.PNG)
        page.enter_email(email)
        page.enter_password(password)
        allure.attach(browser.get_screenshot_as_png(), name="ScreenshotAvatar3", attachment_type=AttachmentType.PNG)
        page.click_button_authorization()
        allure.attach(browser.get_screenshot_as_png(), name="ScreenshotAvatar4", attachment_type=AttachmentType.PNG)
    with allure.step("Change avatar"):
        page.click_change_avatar()
        allure.attach(browser.get_screenshot_as_png(), name="ScreenshotAvatar5", attachment_type=AttachmentType.PNG)
        page.choose_file(file)
        allure.attach(browser.get_screenshot_as_png(), name="ScreenshotAvatar6", attachment_type=AttachmentType.PNG)
        page.click_button_apply()
        allure.attach(browser.get_screenshot_as_png(), name="ScreenshotAvatar7", attachment_type=AttachmentType.PNG)

@allure.testcase(link, 'FCC_password')
@pytest.mark.pasw
@pytest.mark.parametrize('old_password, new_password, email, link', [(password, password_change, email, link),
                                                                     (password_change, password, email, link)])
def test_change_password(browser, old_password, new_password, email, link):
    with allure.step("Launch site"):
        page = MainPage(browser, link)
        page.open()
        allure.attach(browser.get_screenshot_as_png(), name="ScreenshotPassw1", attachment_type=AttachmentType.PNG)
    with allure.step("Authorization"):
        page.go_to_login_page()
        allure.attach(browser.get_screenshot_as_png(), name="ScreenshotPassw2", attachment_type=AttachmentType.PNG)
        page.enter_email(email)
        page.enter_password(old_password)
        allure.attach(browser.get_screenshot_as_png(), name="ScreenshotPassw3", attachment_type=AttachmentType.PNG)
        page.click_button_authorization()
        allure.attach(browser.get_screenshot_as_png(), name="ScreenshotPassw4", attachment_type=AttachmentType.PNG)
    with allure.step("Change password"):
        page.click_button_settings()
        allure.attach(browser.get_screenshot_as_png(), name="ScreenshotPassw5", attachment_type=AttachmentType.PNG)
        page.click_change_password()
        allure.attach(browser.get_screenshot_as_png(), name="ScreenshotPassw6", attachment_type=AttachmentType.PNG)
        page.enter_old_password(old_password)
        page.enter_new_password(new_password)
        page.confirm_new_password(new_password)
        allure.attach(browser.get_screenshot_as_png(), name="ScreenshotPassw7", attachment_type=AttachmentType.PNG)
        page.click_button_change_password()
        allure.attach(browser.get_screenshot_as_png(), name="ScreenshotPassw8", attachment_type=AttachmentType.PNG)
