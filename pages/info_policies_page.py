from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


class InfoPoliciesPage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # ---------- MENU ----------
    def open_info_policies_menu(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[contains(text(),'Info & Policies')]")
            )
        ).click()
        time.sleep(1)

    # ---------- OPEN MODULES ----------
    def open_general_info(self):
        self.open_info_policies_menu()
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[contains(text(),'General Info')]")
            )
        ).click()
        time.sleep(1)

    def open_terms_conditions(self):
        self.open_info_policies_menu()
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[contains(text(),'Terms')]")
            )
        ).click()
        time.sleep(1)

    def open_privacy_policy(self):
        self.open_info_policies_menu()
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[contains(text(),'Privacy')]")
            )
        ).click()
        time.sleep(1)

    # ---------- EDITOR ----------
    def _get_editor(self):
        """
        Locate the actual editable node of the rich-text editor
        """
        return self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@contenteditable='true'] | //textarea")
            )
        )

    def append_text(self, text):
        editor = self._get_editor()

        # Focus editor
        editor.click()
        time.sleep(0.3)

        # Move cursor to end
        editor.send_keys(Keys.END)
        time.sleep(0.2)

        # Append text like real user
        editor.send_keys(" " + text)
        time.sleep(0.3)

        # Fire input event so app detects change
        self.driver.execute_script(
            "arguments[0].dispatchEvent(new Event('input', { bubbles: true }));",
            editor
        )

    def save(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(),'Save')]")
            )
        ).click()
        time.sleep(2)

    def clear_all(self):
        """
        Clear editor using keyboard (more reliable than Clear All button)
        """
        editor = self._get_editor()
        editor.click()
        editor.send_keys(Keys.CONTROL + "a")
        editor.send_keys(Keys.DELETE)
        time.sleep(0.5)

        self.driver.execute_script(
            "arguments[0].dispatchEvent(new Event('input', { bubbles: true }));",
            editor
        )
