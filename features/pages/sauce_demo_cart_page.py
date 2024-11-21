from selenium.webdriver.common.by import By

class SauceDemoCartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")  # Badge showing cart item count
        self.cart_container = (By.ID, "shopping_cart_container")  # Container for cart
        self.checkout_button = (By.ID, "checkout")  # Checkout button

    def get_cart_item_count(self):
        """
        Gets the number of items in the cart using the cart badge.
        If the badge is not present, returns 0 (no items in the cart).
        """
        try:
            cart_badge_element = self.driver.find_element(*self.cart_badge)
            return int(cart_badge_element.text)  # Return the count as an integer
        except Exception:
            # If the cart badge is not found, assume the cart is empty
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
