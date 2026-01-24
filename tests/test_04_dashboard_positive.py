from base.base_test import BaseTest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.safe_step import run_step

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


class TestDashboardPositive(BaseTest):

    def test_dashboard_positive(self):

        # ---------------- SETUP ----------------
        self.setup()

        login = LoginPage(self.driver, self.wait)
        dashboard = DashboardPage(self.driver, self.wait)

        # ---------------- LOGIN ----------------
        run_step(
            module="LOGIN",
            page="Login",
            step="Open login page",
            expected="Login page should open",
            action=login.open_login_page
        )

        run_step(
            module="LOGIN",
            page="Login",
            step="Login with valid credentials",
            expected="User should login successfully",
            action=lambda: login.login(
                "lahari.alla@analogueitsolutionz.com",
                "Admin@123"
            )
        )

        # ---------------- DASHBOARD LOAD ----------------
        run_step(
            module="DASHBOARD",
            page="Dashboard",
            step="Verify dashboard page loads",
            expected="Dashboard page should be displayed",
            action=dashboard.verify_dashboard_loaded
        )

        # ---------------- MAIN SECTIONS VISIBILITY ----------------
        def verify_main_sections_visibility():
            # Summary cards
            self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[contains(@class,'card')]")
                )
            )

            # Sales Details section
            self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//*[contains(text(),'Sales')]")
                )
            )

            # Customers section
            self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//*[contains(text(),'Customers')]")
                )
            )

        run_step(
            module="DASHBOARD",
            page="Dashboard",
            step="Verify main dashboard sections visibility",
            expected="Summary, Sales, and Customers sections should be visible",
            action=verify_main_sections_visibility
        )

        # ---------------- SALES DATE PICKER INPUT PRESENCE ----------------
        def verify_sales_date_inputs_presence():
            inputs = self.driver.find_elements(By.XPATH, "//input")
            if len(inputs) < 2:
                raise AssertionError("Sales date picker inputs not present")

        run_step(
            module="DASHBOARD",
            page="Dashboard",
            step="Verify Sales date picker inputs are present",
            expected="From and To date inputs should be present",
            action=verify_sales_date_inputs_presence
        )

        # ---------------- SALES DATE INPUT MANUAL ENTRY ----------------
        def verify_sales_date_input_manual_entry():
            inputs = self.driver.find_elements(By.XPATH, "//input")

            inputs[0].clear()
            inputs[0].send_keys("01/01/2025")

            inputs[1].clear()
            inputs[1].send_keys("31/01/2025")

            # ⏳ Wait to visually verify date entry (as requested)
            time.sleep(10)

        run_step(
            module="DASHBOARD",
            page="Dashboard",
            step="Verify Sales date input manual entry",
            expected="Sales date fields should accept manual input",
            action=verify_sales_date_input_manual_entry
        )

        # ---------------- CREATE ORGANIZATION NAVIGATION ----------------
        def verify_create_organization_navigation():
            create_btn = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button"))
            )

            create_btn.click()

            # Verify Create Organization page loads
            self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//form | //h1"))
            )

            # ⏳ Wait to visually verify page load
            time.sleep(3)

        run_step(
            module="DASHBOARD",
            page="Dashboard",
            step="Verify Create Organization button click and page load",
            expected="Create Organization page should open",
            action=verify_create_organization_navigation
        )

        # ---------------- LOGOUT ----------------
        run_step(
            module="LOGOUT",
            page="Dashboard",
            step="Logout from application",
            expected="User should logout successfully",
            action=dashboard.logout
        )

        # ---------------- TEARDOWN ----------------
        self.teardown()
