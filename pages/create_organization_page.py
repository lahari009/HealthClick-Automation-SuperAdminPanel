from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC


class CreateOrganizationPage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # ---------------- LOCATORS ----------------
    ORG_NAME = (By.XPATH, "//input[@placeholder='Enter Organization Name']")
    OWNER_NAME = (By.XPATH, "//input[@placeholder='Enter Owner name']")
    SHORT_NAME = (By.XPATH, "//input[@placeholder='Enter short name']")
    BRANCHES = (By.XPATH, "//input[@type='number']")
    CONTACT = (By.XPATH, "//input[@placeholder='Enter Phone Number']")
    EMAIL = (By.XPATH, "//input[@placeholder='Enter email address']")
    ADDRESS = (By.XPATH, "//input[@placeholder='Enter head office address']")
    PASSWORD = (By.XPATH, "//input[@placeholder='Enter password here']")

    PAYMENT_TYPE = (By.XPATH, "//select")
    TRANSACTION_ID = (By.XPATH, "//input[contains(@placeholder,'Transaction')]")
    PACKAGE_AMOUNT = (By.XPATH, "//input[@type='text' and contains(@value,'0')]")

    START_DATE = (By.XPATH, "(//input[@placeholder='mm/dd/yyyy'])[1]")
    END_DATE = (By.XPATH, "(//input[@placeholder='mm/dd/yyyy'])[2]")

    STATUS_TOGGLE = (By.XPATH, "//input[@type='checkbox']")
    SAVE_BUTTON = (By.XPATH, "//button[normalize-space()='Save']")

    PAGE_HEADER = (By.XPATH, "//h1[contains(text(),'Organization Creation')]")

    # ---------------- ACTIONS ----------------
    def wait_for_page(self):
        self.wait.until(EC.visibility_of_element_located(self.PAGE_HEADER))

    def enter(self, locator, value):
        field = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", field
        )
        field.clear()
        field.send_keys(value)

    def select_payment_type(self, text):
        dropdown = self.wait.until(EC.element_to_be_clickable(self.PAYMENT_TYPE))
        Select(dropdown).select_by_visible_text(text)

    def enable_status(self):
        checkbox = self.wait.until(EC.presence_of_element_located(self.STATUS_TOGGLE))
        if not checkbox.is_selected():
            self.driver.execute_script("arguments[0].click();", checkbox)

    def save(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", btn
        )
        btn.click()
