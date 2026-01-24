import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC


class EHRTemplatePage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # ---------------- COMMON ----------------
    def wait_for_table(self):
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//table"))
        )
        time.sleep(1.5)

    # ---------------- DEPARTMENT ----------------
    def select_department(self, dept):
        dropdown = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//select"))
        )
        Select(dropdown).select_by_visible_text(dept)
        self.wait_for_table()

    # ---------------- TAB SWITCH ----------------
    def open_tab_safe(self, tab_name):
        tab = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    f"//button[@role='tab' and contains(normalize-space(), '{tab_name}')]"
                )
            )
        )
        self.driver.execute_script("arguments[0].click();", tab)

        self.wait.until(
            lambda d: tab.get_attribute("aria-selected") == "true"
        )
        self.wait_for_table()

    # ==================================================
    # ================= VITALS (PASS) ==================
    # ==================================================

    def vitals_create_pass(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(),'Create')]")
            )
        ).click()

        modal = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//div[@role='dialog']"))
        )

        modal.find_element(
            By.XPATH, ".//button[normalize-space()='Close All']"
        ).click()

        self.wait.until(EC.invisibility_of_element(modal))
        self.wait_for_table()

    def vitals_search_pass(self, text):
        search = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//input[contains(@placeholder,'Search')]")
            )
        )
        search.clear()
        search.send_keys(text)
        time.sleep(2)

    def vitals_status_pass(self):
        dropdown = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//table/tbody/tr[1]//select")
            )
        )
        Select(dropdown).select_by_index(1)
        time.sleep(1)

    # ==================================================
    # ============ OTHER TEMPLATES (FAIL) ===============
    # ==================================================

    def try_create_and_log_bug(self, template_name):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(),'Create')]")
            )
        ).click()

        modal = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//div[@role='dialog']"))
        )

        modal.find_element(
            By.XPATH, ".//button[normalize-space()='Save']"
        ).click()

        time.sleep(2)

        # ❌ Force failure so run_step logs bug
        raise Exception(f"{template_name} Create did not persist data")

    def try_search_and_log_bug(self, template_name, text):
        search = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//input[contains(@placeholder,'Search')]")
            )
        )
        search.clear()
        search.send_keys(text)
        time.sleep(2)

        rows = self.driver.find_elements(By.XPATH, "//table/tbody/tr")
        if len(rows) == 0:
            raise Exception(f"{template_name} Search returned no results")

    def try_status_and_log_bug(self, template_name):
        dropdown = self.driver.find_element(
            By.XPATH, "//table/tbody/tr[1]//select"
        )
        Select(dropdown).select_by_index(1)
        time.sleep(1)

        raise Exception(f"{template_name} Status change not persisted")

    # ================= MEDICINE TEMPLATE =================

    def open_medicine_tab(self):
        self.open_tab_safe("Medicine")

    def create_medicine_template(self, template_name, medicine_name):
        # Click Create
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(),'Create')]")
            )
        ).click()

        modal = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//div[@role='dialog']"))
        )

        # Enter Template Name
        modal.find_element(
            By.XPATH, ".//input[contains(@placeholder,'Template')]"
        ).send_keys(template_name)

        # Search Medicine
        search = modal.find_element(
            By.XPATH, ".//input[contains(@placeholder,'Search')]"
        )
        search.send_keys(medicine_name)

        # Select medicine
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//li[contains(text(),'{medicine_name}')]")
            )
        ).click()

        # Save
        modal.find_element(
            By.XPATH, ".//button[contains(text(),'Save')]"
        ).click()

        self.wait_for_table()

    # ================= PRESCRIPTION TEMPLATE =================

    def open_prescription_tab(self):
        self.open_tab_safe("Prescription")

    def create_prescription_template(self, template_name, vitals_list):
        # Enter Template Name
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//input[contains(@placeholder,'Template')]")
            )
        ).send_keys(template_name)

        for vital in vitals_list:
            search = self.wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//input[contains(@placeholder,'Search')]")
                )
            )
            search.clear()
            search.send_keys(vital)

            self.wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, f"//li[contains(text(),'{vital}')]")
                )
            ).click()

        # Scroll & Save
        save_btn = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(),'Save')]")
            )
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", save_btn)
        save_btn.click()

        self.wait_for_table()


