from base.base_test import BaseTest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.logout_page import LogoutPage
from utils.safe_step import run_step


class TestLogoutPositive(BaseTest):

    def test_logout_positive(self):
        self.setup()

        login = LoginPage(self.driver, self.wait)
        dashboard = DashboardPage(self.driver, self.wait)
        logout_page = LogoutPage(self.driver, self.wait)

        # ---------- LOGIN ----------
        run_step(
            module="LOGIN",
            page="Login",
            step="Login with valid credentials",
            expected="User should login successfully",
            action=lambda: (
                login.open_login_page(),
                login.login("lahari.alla@analogueitsolutionz.com", "Admin@123")
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

        # ---------- ADMIN SETTINGS ----------
        run_step(
            module="ADMIN SETTINGS",
            page="Dashboard",
            step="Open Admin Settings",
            expected="Admin Settings should open",
            action=logout_page.open_admin_settings
        )

        # ---------- LOGOUT ----------
        run_step(
            module="LOGOUT",
            page="Dashboard",
            step="Logout from application",
            expected="User should be logged out successfully",
            action=logout_page.logout
        )

        self.teardown()
