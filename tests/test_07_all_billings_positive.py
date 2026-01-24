from base.base_test import BaseTest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.all_billings_page import AllBillingsPage
import time
from utils.safe_step import run_step


class TestAllBillingsPositive(BaseTest):

    def test_all_billings_positive(self):

        # ---------------- SETUP ----------------
        self.setup()
        driver = self.driver
        wait = self.wait

        login = LoginPage(driver, wait)
        dashboard = DashboardPage(driver, wait)
        billings = AllBillingsPage(driver, wait)

        # ---------------- LOGIN ----------------
        run_step(
            "LOGIN", "Login",
            "Open login page",
            "Login page should open",
            login.open_login_page
        )

        run_step(
            "LOGIN", "Login",
            "Login with valid credentials",
            "User should login successfully",
            lambda: login.login(
                "lahari.alla@analogueitsolutionz.com",
                "Admin@123"
            )
        )

        # ---------------- DASHBOARD ----------------
        run_step(
            "DASHBOARD", "Dashboard",
            "Verify dashboard loaded",
            "Dashboard should be visible",
            dashboard.verify_dashboard_loaded
        )

        # ---------------- ALL BILLINGS ----------------
        run_step(
            "ALL_BILLINGS", "Menu",
            "Open All Billings",
            "All Billings page should open",
            dashboard.open_all_billings
        )

        run_step(
            "ALL_BILLINGS", "Page",
            "Verify All Billings page loaded",
            "Billing table should be visible",
            billings.wait_for_all_billings_page
        )

        run_step(
            "ALL_BILLINGS", "Table",
            "Verify billing records",
            "Billing records should be present",
            billings.verify_billings_table_has_data
        )

        run_step(
            "ALL_BILLINGS", "Search",
            "Search billing",
            "Filtered results should appear",
            lambda: billings.search_billing("Health")
        )

        # ---------------- WAIT ----------------
        time.sleep(5)

        # ---------------- LOGOUT ----------------
        run_step(
            "LOGOUT", "Dashboard",
            "Logout from application",
            "User should logout successfully",
            dashboard.logout
        )

        self.teardown()


