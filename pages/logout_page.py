from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


class LogoutPage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def open_admin_settings(self):
        """
        Click on Admin Settings from the dashboard menu
        """
        admin_settings = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[contains(text(),'Admin Settings')]")
            )
        )
        self.driver.execute_script("arguments[0].click();", admin_settings)
        time.sleep(1)

    def logout(self):
        """
        Click on Logout option
        """
        logout_btn = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[normalize-space()='Logout']")
            )
        )
        self.driver.execute_script("arguments[0].click();", logout_btn)

        # Optional: wait until redirected to login page
        self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[contains(text(),'Sign In')]")
            )
        )
