from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


class AllOrganizationPage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # ---------------- OPEN ALL ORGANIZATIONS ----------------
    def open_all_organizations(self):
        menu = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[normalize-space()='All Organizations']")
            )
        )
        self.driver.execute_script("arguments[0].click();", menu)

        self.wait.until(EC.presence_of_element_located((By.XPATH, "//table")))
        time.sleep(2)

    # ---------------- OPEN FIRST ORGANIZATION ----------------
    def open_first_organization(self):
        first_row = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//table/tbody/tr[1]"))
        )
        self.driver.execute_script("arguments[0].click();", first_row)

        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[normalize-space()='Next']")
            )
        )
        time.sleep(2)

    # ---------------- DETAILS TAB ----------------
    def fill_details_and_next(self):
        next_btn = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[normalize-space()='Next']")
            )
        )
        self.driver.execute_script("arguments[0].click();", next_btn)
        time.sleep(2)

    # ---------------- BRANCH TAB (3rd BRANCH FIXED) ----------------
    def add_branch_and_next(self):

        add_branch_btn = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[normalize-space()='Add Branch']")
            )
        )

        # Ensure 3 branches exist
        self.driver.execute_script("arguments[0].click();", add_branch_btn)
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", add_branch_btn)
        time.sleep(2)

        def fill_branch(index, location, name, short, phone, person):
            card = self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, f"(//div[contains(@class,'card')])[{index}]")
                )
            )

            def fill(ph, val):
                field = card.find_element(By.XPATH, f".//input[@placeholder='{ph}']")
                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});", field
                )
                field.clear()
                field.send_keys(val)
                time.sleep(0.3)

            fill("Branch Location", location)
            fill("Branch Name", name)
            fill("Short Name", short)
            fill("Help Desk Number", phone)
            fill("Contact Person Name", person)

        # Branch 1
        fill_branch(1, "Hyderabad", "HC Main", "HCM", "9876543210", "Admin One")

        # Branch 3 (IMPORTANT)
        fill_branch(3, "Secunderabad", "HC Secondary", "HCS", "9123456789", "Admin Two")

        next_btn = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[normalize-space()='Next']")
            )
        )
        self.driver.execute_script("arguments[0].click();", next_btn)
        time.sleep(3)

    # ---------------- DEPARTMENTS TAB ----------------
    def allocate_departments_and_next(self):

        allocate_btn = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(),'Allocate')]")
            )
        )
        self.driver.execute_script("arguments[0].click();", allocate_btn)

        modal = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(@class,'modal')]")
            )
        )

        checkboxes = modal.find_elements(By.XPATH, ".//input[@type='checkbox']")
        for cb in checkboxes[:3]:
            self.driver.execute_script("arguments[0].click();", cb)

        save_btn = modal.find_element(
            By.XPATH, ".//button[normalize-space()='Save']")
        self.driver.execute_script("arguments[0].click();", save_btn)
        time.sleep(2)

        next_btn = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[normalize-space()='Next']")
            )
        )
        self.driver.execute_script("arguments[0].click();", next_btn)
        time.sleep(2)

    # ---------------- PACKAGE TAB (FIXED ERRORS) ----------------
    def review_package_and_finish(self):

        view_buttons = self.driver.find_elements(
            By.XPATH, "//button[contains(text(),'View')]"
        )

        for btn in view_buttons:
            try:
                self.driver.execute_script("arguments[0].click();", btn)
                time.sleep(1)
                self.driver.find_element(
                    By.XPATH, "//button[normalize-space()='Close']"
                ).click()
                time.sleep(1)
            except Exception:
                continue

        finish_btn = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[normalize-space()='Finish']")
            )
        )
        self.driver.execute_script("arguments[0].click();", finish_btn)
        time.sleep(2)
