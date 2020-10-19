from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.ID, "login-desktop")
    EMAIL_LINK = (By.CLASS_NAME, "login_email")
    PASSWORD_LINK = (By.ID, "password")
    LOGIN_BUTTON_LINK = (By.ID, "loginformsubmit")
    CHANGE_BUTTON_LINK = (By.XPATH, ".//a[text()='Изменить']")
    HIDE_BUTTON_LINK = (By.XPATH, "//input[@type='file']")
    BUTTON_AVATAR_LINK = (By.XPATH, ".//button[text()='Применить']")
    SETTINGS_BUTTON_LINK = (By.XPATH, ".//span[text()='Настройки']")
    PASSWORD_CHANGE_LINK = (By.XPATH, ".//a[text()='Изменить пароль']")
    PASSWORD_NOW_LINK = (By.XPATH, ".//input[@name='password']")
    PASSWORD_NEW_LINK = (By.XPATH, ".//input[@name='new_password']")
    PASSWORD_CONFIRM_LINK = (By.XPATH, ".//input[@name='password_confirmation']")
    BUTTON_CHANGE_PASSWORD_LINK = (By.XPATH, ".//button[text()='Подтвердить']")

