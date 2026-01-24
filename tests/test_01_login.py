import time

from base.base_test import BaseTest
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage


class TestDashboard(BaseTest):

    def test_login(self):
        try:
            # Browser setup
            self.setup()

            # Login
            login = LoginPage(self.driver, self.wait)
            login.open_login_page()
            login.login("admin@analogueitsolutionz.com", "Admin@123")

            self.wait.until(lambda d: "/dashboard" in d.current_url)
            print("Login successful, dashboard URL loaded")

            dashboard = DashboardPage(self.driver, self.wait)
            dashboard.verify_dashboard_loaded()
            print("Dashboard verified")

            dashboard.open_all_organizations()
            dashboard.open_all_billings()
            dashboard.open_ehr_template()
            dashboard.open_departments()

            # Info & Policies (menu collapses each time – handled correctly)
            dashboard.expand_info_policies()
            dashboard.open_general_info()

            dashboard.expand_info_policies()
            dashboard.open_terms_conditions()

            dashboard.expand_info_policies()
            dashboard.open_privacy_policy()

            dashboard.open_admin_settings()
            dashboard.logout()

        except Exception as e:
            print("❌ Test failed:", type(e).__name__, e)
            time.sleep(10)
            raise