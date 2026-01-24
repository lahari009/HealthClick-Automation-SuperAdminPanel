from base.base_test import BaseTest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.safe_step import run_step


class TestLoginPositive(BaseTest):

    def test_login_positive(self):
        self.setup()

        login = LoginPage(self.driver, self.wait)
        dashboard = DashboardPage(self.driver, self.wait)

        # ---------- LOGIN ----------
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
            step="Forgot password positive flow",
            expected="Reset email should be sent",
            action=lambda: login.verify_forgot_password_flow(
                "lahari.alla@analogueitsolutionz.com"
            )
        )

        run_step(
            module="LOGIN",
            page="Login",
            step="Back to login page",
            expected="Login page should be visible",
            action=login.back_to_login_page
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

        # ---------- DASHBOARD ----------
        run_step(
            module="DASHBOARD",
            page="Dashboard",
            step="Verify dashboard loaded",
            expected="Dashboard should load",
            action=dashboard.verify_dashboard_loaded
        )

        run_step(
            module="DASHBOARD",
            page="Menu",
            step="Open All Organizations",
            expected="Organizations page should open",
            action=dashboard.open_all_organizations
        )

        run_step(
            module="DASHBOARD",
            page="Menu",
            step="Open All Billings",
            expected="Billings page should open",
            action=dashboard.open_all_billings
        )

        run_step(
            module="DASHBOARD",
            page="Menu",
            step="Open EHR Template",
            expected="EHR template page should open",
            action=dashboard.open_ehr_template
        )

        run_step(
            module="DASHBOARD",
            page="Menu",
            step="Open Departments",
            expected="Departments page should open",
            action=dashboard.open_departments
        )

        run_step(
            module="INFO & POLICIES",
            page="Info",
            step="Open General Info",
            expected="General info should open",
            action=dashboard.open_general_info
        )

        run_step(
            module="INFO & POLICIES",
            page="Info",
            step="Open Terms & Conditions",
            expected="Terms page should open",
            action=dashboard.open_terms_conditions
        )

        run_step(
            module="INFO & POLICIES",
            page="Info",
            step="Open Privacy Policy",
            expected="Privacy page should open",
            action=dashboard.open_privacy_policy
        )

        run_step(
            module="ADMIN SETTINGS",
            page="Settings",
            step="Open Admin Settings",
            expected="Admin settings should open",
            action=dashboard.open_admin_settings
        )

        # ---------- LOGOUT ----------
        run_step(
            module="LOGOUT",
            page="Dashboard",
            step="Logout from application",
            expected="User should logout",
            action=dashboard.logout
        )