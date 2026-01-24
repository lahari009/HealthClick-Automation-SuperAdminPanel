from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


class AdminSettingsPage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def verify_admin_settings_page_loaded(self):
        self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//h4[contains(text(),'Admin')] | //span[contains(text(),'Admin')]")
            )
        )

    def update_support_phone(self, new_phone):
        phone_input = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//input[contains(@value,'+91') or contains(@placeholder,'Phone')]")
            )
        )

        phone_input.click()
        phone_input.send_keys(Keys.CONTROL + "a")
        phone_input.send_keys(Keys.DELETE)
        phone_input.send_keys(new_phone)

        # 🔑 IMPORTANT: trigger blur so React updates state
        phone_input.send_keys(Keys.TAB)
        time.sleep(1)

    def click_save(self):
        save_btn = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[contains(text(),'Save')]")
            )
        )

        # 🔑 Wait until Save is actually enabled
        self.wait.until(
            lambda d: save_btn.is_enabled()
        )

        save_btn.click()
        time.sleep(2)
