from pages.main_page import MainPage
import pytest

email = 'your email'
password = 'your password'
password_change = 'your password for test'
link = "https://www.freeconferencecall.com/ru"
file = 'your file'


@pytest.mark.parametrize('email, password, link', [(email, password, link)])
@pytest.mark.aut
def test_authorization(browser, email, password, link):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    page.enter_email(email)
    page.enter_password(password)
    page.click_button_authorization()


@pytest.mark.avatar
@pytest.mark.parametrize('email, password, link, file', [(email, password, link, file)])
def test_change_avatar(browser, email, password, link, file):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.enter_email(email)
    page.enter_password(password)
    page.click_button_authorization()
    page.click_change_avatar()
    page.choose_file(file)
    page.click_button_apply()


@pytest.mark.pasw
@pytest.mark.parametrize('old_password, new_password, email, link', [(password, password_change, email, link),
                                                                     (password_change, password, email, link)])
def test_change_password(browser, old_password, new_password, email, link):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.enter_email(email)
    page.enter_password(old_password)
    page.click_button_authorization()
    page.click_button_settings()
    page.click_change_password()
    page.enter_old_password(old_password)
    page.enter_new_password(new_password)
    page.confirm_new_password(new_password)
    page.click_button_change_password()
