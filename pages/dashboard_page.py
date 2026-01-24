from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


class DashboardPage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # ---------------- DASHBOARD ----------------

    def verify_dashboard_loaded(self):
        self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//span[normalize-space()='Dashboard']")
            )
        )

    # ---------------- COMMON SAFE CLICK ----------------

    def _safe_click(self, xpath):
        element = self.wait.until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", element
        )
        self.driver.execute_script("arguments[0].click();", element)

    # ---------------- MAIN MENUS ----------------

    def open_all_organizations(self):
        self._safe_click("//span[normalize-space()='All Organizations']")
        time.sleep(2)

    def open_all_billings(self):
        self._safe_click("//span[normalize-space()='All Billings']")
        time.sleep(2)

    def open_ehr_template(self):
        self._safe_click("//span[normalize-space()='EHR Template']")
        time.sleep(2)

    def open_departments(self):
        self._safe_click("//span[contains(text(),'Departments')]")
        time.sleep(2)

    # ---------------- INFO & POLICIES ----------------

    def expand_info_policies(self):
        self._safe_click("//span[normalize-space()='Info & Policies']")

        # 🔑 wait until submenu really appears
        self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[contains(text(),'General')]")
            )
        )
        time.sleep(1)

    def open_general_info(self):
        self.expand_info_policies()
        self._safe_click("//span[normalize-space()='General Info']")
        time.sleep(3)

    def open_terms_conditions(self):
        self.expand_info_policies()
        self._safe_click("//span[contains(text(),'Terms')]")
        time.sleep(3)

    def open_privacy_policy(self):
        self.expand_info_policies()
        self._safe_click("//span[contains(text(),'Privacy')]")
        time.sleep(3)

    # ---------------- ADMIN & LOGOUT ----------------

    def open_admin_settings(self):
        self._safe_click("//span[contains(text(),'Admin Settings')]")
        time.sleep(2)

    def logout(self):
        self._safe_click("//span[normalize-space()='Logout']")
        time.sleep(2)
