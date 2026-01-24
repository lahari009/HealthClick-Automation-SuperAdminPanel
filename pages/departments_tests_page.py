from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


class DepartmentsTestsPage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # ---------- COMMON ----------
    def wait_for_table(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//table")))
        time.sleep(1)

    # ---------- NAVIGATION ----------
    def open_departments_tests(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[contains(text(),'Departments & Tests')]")
            )
        ).click()
        self.wait_for_table()

    # ---------- SAFE TAB HANDLING ----------
    def open_tab_if_not_active(self, tab_name):
        tab = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, f"//button[contains(text(),'{tab_name}')]")
            )
        )

        # If already active → PASS silently
        if "active" in tab.get_attribute("class"):
            self.wait_for_table()
            return

        tab.click()
        self.wait_for_table()

    # ---------- SEARCH ----------
    def search(self, text):
        search = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//input[contains(@placeholder,'Search')]")
            )
        )
        search.clear()
        search.send_keys(text)
        time.sleep(2)

    # ---------- DOWNLOAD ----------
    def download_csv(self):
        self._download("CSV")

    def download_pdf(self):
        self._download("PDF")

    def _download(self, file_type):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(),'Download')]")
            )
        ).click()

        option = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//a[contains(text(),'{file_type}')]")
            )
        )
        option.click()
        time.sleep(2)

    # ---------- ADD / EDIT ----------
    def open_add_new_test(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(),'Add New Test')]")
            )
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(text(),'Create Test')]")
            )
        )

    def close_create_popup(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(),'Clear All')]")
            )
        ).click()
        time.sleep(1)

    def open_edit_test(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "(//i[contains(@class,'edit')])[1]")
            )
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(text(),'Edit Test')]")
            )
        )
