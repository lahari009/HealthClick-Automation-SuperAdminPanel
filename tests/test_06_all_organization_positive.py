from base.base_test import BaseTest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.all_organization_page import AllOrganizationPage
from utils.safe_step import run_step
import time


class TestAllOrganizationPositive(BaseTest):

    def test_all_organization_positive(self):

        self.setup()
        driver = self.driver
        wait = self.wait

        login = LoginPage(driver, wait)
        dashboard = DashboardPage(driver, wait)
        org_page = AllOrganizationPage(driver, wait)

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

        run_step(
            "DASHBOARD", "Dashboard",
            "Verify dashboard loaded",
            "Dashboard should be visible",
            dashboard.verify_dashboard_loaded
        )

        run_step(
            "ALL_ORG", "Menu",
            "Open All Organizations",
            "All Organizations page should open",
            org_page.open_all_organizations
        )

        run_step(
            "ALL_ORG", "List",
            "Open first organization record",
            "Organization details page should open",
            org_page.open_first_organization
        )

        run_step(
            "ALL_ORG", "Details",
            "Fill Details tab and proceed",
            "Details saved",
            org_page.fill_details_and_next
        )

        run_step(
            "ALL_ORG", "Branch",
            "Add 3rd branch and proceed",
            "Branch saved",
            org_page.add_branch_and_next
        )

        run_step(
            "ALL_ORG", "Departments",
            "Allocate departments and proceed",
            "Departments saved",
            org_page.allocate_departments_and_next
        )

        run_step(
            "ALL_ORG", "Package",
            "Review package and finish",
            "Package completed",
            org_page.review_package_and_finish
        )

        run_step(
            "LOGOUT", "Dashboard",
            "Logout from application",
            "User logged out",
            dashboard.logout
        )

        time.sleep(2)
        self.teardown()

