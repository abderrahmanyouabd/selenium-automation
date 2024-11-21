import undetected_chromedriver as uc
from selenium_stealth import stealth

def before_all(context):
    """
    Initialize the Selenium driver with undetected-chromedriver and stealth settings
    to bypass Cloudflare and other bot detection mechanisms.
    """
    try:
        # Configure undetected ChromeDriver options
        options = uc.ChromeOptions()
        options.add_argument("start-maximized")
        # options.add_argument("--headless")  # Uncomment for headless mode
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-popup-blocking")  # Disable popups
        options.add_argument("--disable-notifications")  # Disable notifications

        # Add preferences to disable password and enhanced protection prompts
        prefs = {
            "credentials_enable_service": False,  # Disable password manager
            "profile.password_manager_enabled": False,  # Disable save password prompt
            "safebrowsing.enabled": False,  # Enable safe browsing but without enhanced protection
        }
        options.add_experimental_option("prefs", prefs)

        # Initialize the undetected ChromeDriver
        context.driver = uc.Chrome(options=options)

        context.driver.implicitly_wait(5)

        # Apply stealth settings to the driver
        stealth(
            context.driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
        )
    except Exception as e:
        print(f"Error initializing driver: {e}")
        raise

def after_all(context):
    """
    Clean up after all tests are run by quitting the driver.
    """
    if hasattr(context, 'driver'):
        context.driver.quit()
