from selenium.webdriver.common.by import By
from pages.sauce_demo_login_page import SauceDemoLoginPage

class MenuPage(SauceDemoLoginPage):
    MENU_ICON = (By.ID, "react-burger-menu-btn")
    LOGOUT_BUTTON = (By.ID, "logout_sidebar_link")

    def __init__(self, context):
        super().__init__(context)

    def open_menu(self):
        self.click(self.MENU_ICON)

    def logout(self):
        self.click(self.LOGOUT_BUTTON)
