from selenium.webdriver.common.by import By

class SauceDemoCartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
        self.cart_container = (By.ID, "shopping_cart_container")
        self.checkout_button = (By.ID, "checkout")

    def get_cart_item_count(self):
        """
        Gets the number of items in the cart using the cart badge.
        If the badge is not present, returns 0 (no items in the cart).
        """
        try:
            cart_badge_element = self.driver.find_element(*self.cart_badge)
            return int(cart_badge_element.text)
        except Exception:

            print("Cart badge not found. Assuming no items in the cart.")
            return 0

    def open_cart(self):
        """
        Clicks on the shopping cart container to open the cart page.
        """
        self.driver.find_element(*self.cart_container).click()

    def click_checkout(self):
        """
        Clicks the checkout button on the cart page.
        """
        self.driver.find_element(*self.checkout_button).click()
