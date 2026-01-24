from base.base_test import BaseTest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.info_policies_page import InfoPoliciesPage
from utils.safe_step import run_step


class TestInfoPoliciesPositive(BaseTest):

    def test_info_policies_positive(self):
        self.setup()

        login = LoginPage(self.driver, self.wait)
        dashboard = DashboardPage(self.driver, self.wait)
        info = InfoPoliciesPage(self.driver, self.wait)

        # ---------- LOGIN ----------
        run_step(
            "LOGIN", "Login",
            "Login with valid credentials",
            "User should login successfully",
            lambda: (
                login.open_login_page(),
                login.login("lahari.alla@analogueitsolutionz.com", "Admin@123")
            )
        )

        # ---------- DASHBOARD ----------
        run_step(
            "DASHBOARD", "Dashboard",
            "Verify dashboard loaded",
            "Dashboard should load",
            dashboard.verify_dashboard_loaded
        )

        # ========= GENERAL INFO =========
        run_step(
            "INFO & POLICIES", "General Info",
            "Open General Info",
            "General Info page should open",
            info.open_general_info
        )

        run_step(
            "INFO & POLICIES", "General Info",
            "Append General Info data",
            "Data should be appended",
            lambda: info.append_text("HealthClick")
        )

        run_step(
            "INFO & POLICIES", "General Info",
            "Save General Info",
            "Data should be saved",
            info.save
        )

        run_step(
            "INFO & POLICIES", "General Info",
            "Clear General Info",
            "Content should be cleared",
            info.clear_all
        )

        # ========= TERMS =========
        run_step(
            "INFO & POLICIES", "Terms & Conditions",
            "Open Terms & Conditions",
            "Terms page should open",
            info.open_terms_conditions
        )

        run_step(
            "INFO & POLICIES", "Terms & Conditions",
            "Append Terms data",
            "Data should be appended",
            lambda: info.append_text("HealthClick")
        )

        run_step(
            "INFO & POLICIES", "Terms & Conditions",
            "Save Terms data",
            "Data should be saved",
            info.save
        )

        run_step(
            "INFO & POLICIES", "Terms & Conditions",
            "Clear Terms data",
            "Content should be cleared",
            info.clear_all
        )

        # ========= PRIVACY =========
        run_step(
            "INFO & POLICIES", "Privacy Policy",
            "Open Privacy Policy",
            "Privacy page should open",
            info.open_privacy_policy
        )

        run_step(
            "INFO & POLICIES", "Privacy Policy",
            "Append Privacy Policy data",
            "Data should be appended",
            lambda: info.append_text("HealthClick")
        )

        run_step(
            "INFO & POLICIES", "Privacy Policy",
            "Save Privacy Policy",
            "Data should be saved",
            info.save
        )

        run_step(
            "INFO & POLICIES", "Privacy Policy",
            "Clear Privacy Policy",
            "Content should be cleared",
            info.clear_all
        )

        # ---------- LOGOUT ----------
        run_step(
            "LOGOUT", "Dashboard",
            "Logout from application",
            "User should logout successfully",
            dashboard.logout
        )

        self.teardown()
