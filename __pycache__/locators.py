from selenium.webdriver.common.by import By


class Locators:

    LOGIN_LINK = "login-desktop"
    EMAIL_LINK = "login_email"
    PASSWORD_LINK = "password"
    LOGIN_BUTTON_LINK = "loginformsubmit"
    CHANGE_BUTTON_LINK = ".//a[text()='Изменить']"
    HIDE_BUTTON_LINK = "//input[@type='file']"
    BUTTON_AVATAR_LINK = ".//button[text()='Применить']"
    SETTINGS_BUTTON_LINK = ".//span[text()='Настройки']"
    PASSWORD_CHANGE_LINK = ".//a[text()='Изменить пароль']"
    PASSWORD_NOW_LINK = ".//input[@name='password']"
    PASSWORD_NEW_LINK = ".//input[@name='new_password']"
    PASSWORD_CONFIRM_LINK = ".//input[@name='password_confirmation']"
    BUTTON_CHANGE_PASSWORD_LINK = ".//button[text()='Подтвердить']"
    SELECT_TIMEZONE = './/select[@aria-label="Часовой пояс"]'
    BUTTON_SAVE = './/button[@title="Сохранить изменения"]'
    NAME_INPUT = './/input[@name="first_name"]'
    LAST_NAME_INPUT = './/input[@name="last_name"]'
