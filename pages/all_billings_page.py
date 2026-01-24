from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


class AllBillingsPage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # ---------------- VERIFY ALL BILLINGS PAGE ----------------
    def wait_for_all_billings_page(self):
        self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//h1 | //span[contains(text(),'All Billings')]")
            )
        )
        self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//table")
            )
        )
        time.sleep(2)

    # ---------------- VERIFY BILLINGS TABLE ----------------
    def verify_billings_table_has_data(self):
        rows = self.wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//table/tbody/tr")
            )
        )

        if len(rows) == 0:
            raise AssertionError("No billing records found")

    # ---------------- SEARCH BILLINGS ----------------
    def search_billing(self, keyword):
        search_input = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//input[contains(@placeholder,'Search')]")
            )
        )
        search_input.clear()
        search_input.send_keys(keyword)
        time.sleep(2)

    # ---------------- PAGINATION ----------------
    def verify_pagination_present(self):
        self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//ul[contains(@class,'pagination')]")
            )
        )
