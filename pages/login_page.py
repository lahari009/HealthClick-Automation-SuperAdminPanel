from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


class LoginPage:

    LOGIN_URL = "https://staging.mediclickz.com/auth/login"

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def open_login_page(self):
        self.driver.get(self.LOGIN_URL)
        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//form"))
        )

    def verify_login_page_ui(self):
        self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[contains(@placeholder,'Email')]")
        ))
        self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[contains(@placeholder,'Password')]")
        ))
        self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//button[contains(text(),'Sign In')]")
        ))

    def verify_password_toggle_logic(self, password_text):
        password_input = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//input[contains(@placeholder,'Password')]")
            )
        )

        password_input.clear()
        password_input.send_keys(password_text)

        initial_type = password_input.get_attribute("type")

        eye_icons = self.driver.find_elements(
            By.XPATH, "//button//*[name()='svg'] | //span//*[name()='svg']"
        )

        if not eye_icons:
            raise AssertionError("Password eye toggle icon missing")

        eye_icons[0].click()
        time.sleep(1)
        after_show = password_input.get_attribute("type")

        eye_icons[0].click()
        time.sleep(1)
        after_hide = password_input.get_attribute("type")

        if initial_type != "password":
            raise AssertionError("Password not masked by default")

        if after_show != "text":
            raise AssertionError("Eye toggle show logic incorrect")

        if after_hide != "password":
            raise AssertionError("Eye toggle hide logic incorrect")

    def verify_forgot_password_flow(self, email):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[contains(text(),'Forgot')]")
            )
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//input[contains(@placeholder,'Email')]")
            )
        ).clear()

        self.driver.find_element(
            By.XPATH, "//input[contains(@placeholder,'Email')]"
        ).send_keys(email)

        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button"))
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//*[contains(text(),'email') or contains(text(),'sent')]")
            )
        )

    # ✅ FINAL FIX – RELIABLE RETURN TO LOGIN
    def back_to_login_page(self):
        self.driver.get(self.LOGIN_URL)
        self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[contains(text(),'Sign In')]")
            )
        )

    def login(self, email, password):
        email_field = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//input[contains(@placeholder,'Email')]")
            )
        )
        email_field.clear()
        email_field.send_keys(email)

        password_field = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//input[contains(@placeholder,'Password')]")
            )
        )
        password_field.clear()
        password_field.send_keys(password)

        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(),'Sign In')]")
            )
        ).click()
