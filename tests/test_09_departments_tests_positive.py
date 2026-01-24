from base.base_test import BaseTest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.departments_tests_page import DepartmentsTestsPage
from utils.safe_step import run_step


class TestDepartmentsTestsPositive(BaseTest):

    def test_departments_tests_positive(self):
        self.setup()

        login = LoginPage(self.driver, self.wait)
        dashboard = DashboardPage(self.driver, self.wait)
        dept = DepartmentsTestsPage(self.driver, self.wait)

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

        # ---------- DEPARTMENTS & TESTS ----------
        run_step(
            "DEPARTMENTS & TESTS", "Menu",
            "Open Departments & Tests",
            "Page should open",
            dept.open_departments_tests
        )

        # ---------- ALL DEPARTMENTS ----------
        run_step(
            "ALL DEPARTMENTS", "Tab",
            "Open All Departments tab",
            "All Departments should be visible",
            lambda: dept.open_tab_if_not_active("All Departments")
        )

        run_step(
            "ALL DEPARTMENTS", "Search",
            "Search department",
            "Search should filter records",
            lambda: dept.search("doctor")
        )

        run_step(
            "ALL DEPARTMENTS", "Download",
            "Download CSV",
            "CSV should download",
            dept.download_csv
        )

        run_step(
            "ALL DEPARTMENTS", "Download",
            "Download PDF",
            "PDF should download",
            dept.download_pdf
        )

        # ---------- ALL TESTS ----------
        run_step(
            "ALL TESTS", "Tab",
            "Open All Tests tab",
            "All Tests should be visible",
            lambda: dept.open_tab_if_not_active("All Tests")
        )

        run_step(
            "ALL TESTS", "Search",
            "Search test",
            "Search should filter tests",
            lambda: dept.search("Blood")
        )

        run_step(
            "ALL TESTS", "Download",
            "Download CSV",
            "CSV should download",
            dept.download_csv
        )

        run_step(
            "ALL TESTS", "Download",
            "Download PDF",
            "PDF should download",
            dept.download_pdf
        )

        run_step(
            "ALL TESTS", "Create",
            "Open Add New Test popup",
            "Create Test popup should open",
            dept.open_add_new_test
        )

        run_step(
            "ALL TESTS", "Popup",
            "Close Create Test popup",
            "Popup should close",
            dept.close_create_popup
        )

        run_step(
            "ALL TESTS", "Edit",
            "Open Edit Test",
            "Edit popup should open",
            dept.open_edit_test
        )

        # ---------- LOGOUT ----------
        run_step(
            "LOGOUT", "Dashboard",
            "Logout",
            "User should logout",
            dashboard.logout
        )

        self.teardown()
