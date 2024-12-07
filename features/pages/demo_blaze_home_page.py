from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
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
            "Send Message": (By.CSS_SELECTOR, "#exampleModal > div > div > div.modal-footer > button.btn.btn-primary"),
            "Delete Nexus Item": (By.XPATH, "//tr[td[text()='Nexus 6']]/td/a[contains(@onclick, 'deleteItem')]"),
            "Close Video": (By.CSS_SELECTOR, "#videoModal > div > div > div.modal-footer > button"),
            "Pop up Login": (By.CSS_SELECTOR, "#logInModal > div > div > div.modal-footer > button.btn.btn-primary"),
        }

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

    def fill_order_details(self, name, country, city, credit_card, month, year):
        """Fill the order details in the modal form."""
        self.driver.find_element(By.ID, "name").send_keys(name)
        self.driver.find_element(By.ID, "country").send_keys(country)
        self.driver.find_element(By.ID, "city").send_keys(city)
        self.driver.find_element(By.ID, "card").send_keys(credit_card)
        self.driver.find_element(By.ID, "month").send_keys(month)
        self.driver.find_element(By.ID, "year").send_keys(year)