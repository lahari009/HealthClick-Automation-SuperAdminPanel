from base.base_test import BaseTest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.admin_settings_page import AdminSettingsPage
from utils.safe_step import run_step


class TestAdminSettingsPositive(BaseTest):

    def test_admin_settings_positive(self):
        self.setup()

        login = LoginPage(self.driver, self.wait)
        dashboard = DashboardPage(self.driver, self.wait)
        admin = AdminSettingsPage(self.driver, self.wait)

        run_step(
            "LOGIN", "Login",
            "Login with valid credentials",
            "User should login successfully",
            lambda: (
                login.open_login_page(),
                login.login("admin@analogueitsolutionz.com", "Admin@123")
            )
        )

        run_step(
            "DASHBOARD", "Dashboard",
            "Verify dashboard loaded",
            "Dashboard should load",
            dashboard.verify_dashboard_loaded
        )

        run_step(
            "ADMIN SETTINGS", "Menu",
            "Open Admin Settings",
            "Admin Settings page should open",
            dashboard.open_admin_settings
        )

        run_step(
            "ADMIN SETTINGS", "Admin Settings",
            "Verify Admin Settings page loaded",
            "Admin Settings page should be visible",
            admin.verify_admin_settings_page_loaded
        )

        run_step(
            "ADMIN SETTINGS", "Admin Settings",
            "Update support phone number",
            "Phone number should be updated",
            lambda: admin.update_support_phone("+919876543210")
        )

        run_step(
            "ADMIN SETTINGS", "Admin Settings",
            "Save Admin Settings",
            "Changes should be saved",
            admin.click_save
        )

        run_step(
            "LOGOUT", "Dashboard",
            "Logout from application",
            "User should logout successfully",
            dashboard.logout
        )

        self.teardown()
