from .pages.main_page import MainPage
import pytest


@pytest.mark.authorization
def test_authorization(browser):
    link = "https://www.freeconferencecall.com/ru"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    page.authorization()


@pytest.mark.avatar
def test_change_avatar(browser):
    link = "https://www.freeconferencecall.com/ru"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.authorization()
    page.change_avatar()


@pytest.mark.password
def test_change_password(browser):
    link = "https://www.freeconferencecall.com/ru"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.authorization()
    page.change_password()
