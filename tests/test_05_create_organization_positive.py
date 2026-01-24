from base.base_test import BaseTest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.create_organization_page import CreateOrganizationPage
from utils.safe_step import run_step

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestCreateOrganizationPositive(BaseTest):

    def test_create_organization_positive(self):

        self.setup()
        driver = self.driver
        wait = self.wait

        login = LoginPage(driver, wait)
        dashboard = DashboardPage(driver, wait)
        create_org = CreateOrganizationPage(driver, wait)

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

        # ---------------- OPEN CREATE ORGANIZATION ----------------
        def open_create_org_page():
            driver.get(
                "https://staging.mediclickz.com/admin/v1/dashboard/organisations/create"
            )
            create_org.wait_for_page()

        run_step(
            "CREATE_ORG", "Dashboard",
            "Open Create Organization page",
            "Create Organization page should open",
            open_create_org_page
        )

        # ---------------- ENTER DATA ----------------
        def enter_valid_data():
            create_org.enter(create_org.ORG_NAME, "HC Automation Org")
            create_org.enter(create_org.OWNER_NAME, "Admin User")
            create_org.enter(create_org.SHORT_NAME, "HCAUTO")
            create_org.enter(create_org.BRANCHES, "2")
            create_org.enter(create_org.CONTACT, "9876543210")
            create_org.enter(create_org.EMAIL, "hcautomation@gmail.com")
            create_org.enter(create_org.ADDRESS, "Hyderabad, Telangana")
            create_org.enter(create_org.PASSWORD, "Admin@123")

            create_org.select_payment_type("Online")
            create_org.enter(create_org.TRANSACTION_ID, "TXN123456")
            create_org.enter(create_org.PACKAGE_AMOUNT, "50000")

            create_org.enter(create_org.START_DATE, "01/01/2025")
            create_org.enter(create_org.END_DATE, "31/01/2025")

            create_org.enable_status()

        run_step(
            "CREATE_ORG", "Create Organization",
            "Enter valid organization data",
            "All mandatory fields should be filled",
            enter_valid_data
        )

        # ---------------- SAVE ----------------
        run_step(
            "CREATE_ORG", "Create Organization",
            "Save organization",
            "Organization should be created successfully",
            create_org.save
        )

        # ---------------- LOGOUT ----------------
        run_step(
            "LOGOUT", "Dashboard",
            "Logout from application",
            "User should logout successfully",
            dashboard.logout
        )

        self.teardown()
