from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    URL = "https://www.demoblaze.com/index.html"

    def __init__(self, driver):
        self.driver = driver
        self.locators = {
            "Home": (By.CSS_SELECTOR, "#navbarExample > ul > li.nav-item.active > a"),
            "Cart": (By.ID, "cartur"),
            "Add to cart": (By.CSS_SELECTOR, "#tbodyid > div.row > div > a"),
            "Log in": (By.ID, "login2"),
            "Log out": (By.ID, "logout2"),
            "Sign up": (By.ID, "signin2"),
            "Place Order": (By.CSS_SELECTOR, "#page-wrapper > div > div.col-lg-1 > button"),
            "Purchase": (By.CSS_SELECTOR, "#orderModal > div > div > div.modal-footer > button.btn.btn-primary"),
            "Delete Nexus Item": (By.XPATH, "//tr[td[text()='Nexus 6']]/td/a[contains(@onclick, 'deleteItem')]"),
        }

    def open(self):
        """Open the Demoblaze homepage."""
        self.driver.get(self.URL)

    def click_button(self, button_name):
        """Generic method to click buttons using the locators map."""
        locator_type, locator_value = self.locators[button_name]
        button = self.driver.find_element(locator_type, locator_value)
        button.click()

    def click_item(self, item_name):
        """Click on a specific product item."""
        item = self.driver.find_element(By.LINK_TEXT, item_name)
        item.click()


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.locators = {
            "Add to cart": (By.CSS_SELECTOR, "#tbodyid > div.row > div > a"),
            "Place Order": (By.CSS_SELECTOR, "#page-wrapper > div > div.col-lg-1 > button"),
            "Purchase": (By.CSS_SELECTOR, "#orderModal > div > div > div.modal-footer > button.btn.btn-primary"),
            "Delete Nexus Item": (By.XPATH, "//tr[td[text()='Nexus 6']]/td/a[contains(@onclick, 'deleteItem')]"),
        }

    def click_button(self, button_name):
        """Generic method to click buttons using the locators map."""
        locator_type, locator_value = self.locators[button_name]
        button = self.driver.find_element(locator_type, locator_value)
        button.click()

    def delete_item(self, item_name):
        """Delete a specific item from the cart."""
        delete_button = self.driver.find_element(By.XPATH, f"//td[contains(text(),'{item_name}')]/following-sibling::td[2]/a")
        delete_button.click()
        WebDriverWait(self.driver, 10).until_not(
            EC.presence_of_element_located((By.XPATH, f"//td[contains(text(),'{item_name}')]"))
        )

    def get_total_price(self):
        """Retrieve the total price in the cart."""
        wait = WebDriverWait(self.driver, 10)
        total_price_element = wait.until(EC.visibility_of_element_located((By.ID, "totalp")))
        return int(total_price_element.text.split()[0])
