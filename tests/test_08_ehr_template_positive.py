from base.base_test import BaseTest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.ehr_template_page import EHRTemplatePage
from utils.safe_step import run_step


class TestEHRTemplatePositive(BaseTest):

    def test_ehr_template_positive(self):
        self.setup()

        login = LoginPage(self.driver, self.wait)
        dashboard = DashboardPage(self.driver, self.wait)
        ehr = EHRTemplatePage(self.driver, self.wait)

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

        # ---------- OPEN EHR ----------
        run_step(
            module="EHR",
            page="Menu",
            step="Open EHR Template",
            expected="EHR Template page should open",
            action=dashboard.open_ehr_template
        )

        # ---------- SELECT DEPARTMENT ----------
        run_step(
            module="EHR",
            page="Department",
            step="Select Pediatrician department",
            expected="Pediatrician department should be selected",
            action=lambda: ehr.select_department("Pediatrician")
        )

        # ================== VITALS (PASS FLOW) ==================
        run_step(
            module="EHR",
            page="Vitals",
            step="Open Vitals tab",
            expected="Vitals tab should open",
            action=lambda: ehr.open_tab_safe("Vitals")
        )

        run_step(
            module="EHR",
            page="Vitals",
            step="Vitals Create popup",
            expected="Create popup should open",
            action=ehr.vitals_create_pass
        )

        run_step(
            module="EHR",
            page="Vitals",
            step="Vitals Search",
            expected="Search should work",
            action=lambda: ehr.vitals_search_pass("Blood")
        )

        run_step(
            module="EHR",
            page="Vitals",
            step="Vitals Status change",
            expected="Status should change",
            action=ehr.vitals_status_pass
        )

        # ================== OTHER TEMPLATES (BUG EXPECTED) ==================
        templates = [
            "Complaint",
            "History",
            "Diagnosis",
            "Advice",
            "Treatment",
            "ProgressNote"
        ]

        for template in templates:

            run_step(
                module="EHR",
                page=template,
                step=f"Open {template} tab",
                expected=f"{template} tab should open",
                action=lambda t=template: ehr.open_tab_safe(t)
            )

            run_step(
                module="EHR",
                page=template,
                step=f"{template} Create",
                expected="Create popup should open and save data",
                action=lambda t=template: ehr.try_create_and_log_bug(t)
            )

            run_step(
                module="EHR",
                page=template,
                step=f"{template} Search",
                expected="Search should filter records",
                action=lambda t=template: ehr.try_search_and_log_bug(t, "Test")
            )

            run_step(
                module="EHR",
                page=template,
                step=f"{template} Status change",
                expected="Status should change successfully",
                action=lambda t=template: ehr.try_status_and_log_bug(t)
            )

        # ================= MEDICINE TEMPLATE =================
        run_step(
            module="EHR",
            page="Medicine",
            step="Open Medicine Template",
            expected="Medicine template page should open",
            action=ehr.open_medicine_tab
        )

        run_step(
            module="EHR",
            page="Medicine",
            step="Create Medicine Template",
            expected="Medicine template should be created",
            action=lambda: ehr.create_medicine_template("Cough", "Dolo")
        )

        run_step(
            module="EHR",
            page="Medicine",
            step="Verify Medicine Search",
            expected="Search should work",
            action=lambda: ehr.search_record_safe("Cough")
        )

        run_step(
            module="EHR",
            page="Medicine",
            step="Verify Medicine Status Change",
            expected="Status should change",
            action=lambda: ehr.try_status_and_log_bug("Medicine")
        )

        # ================= PRESCRIPTION TEMPLATE =================
        run_step(
            module="EHR",
            page="Prescription",
            step="Open Prescription Template",
            expected="Prescription template page should open",
            action=ehr.open_prescription_tab
        )

        run_step(
            module="EHR",
            page="Prescription",
            step="Create Prescription Template",
            expected="Prescription template should be created",
            action=lambda: ehr.create_prescription_template(
                "Cold",
                ["vvvvvv", "lllllllllllll"]
            )
        )

        # ---------- LOGOUT ----------
        run_step(
            module="LOGOUT",
            page="Dashboard",
            step="Logout from application",
            expected="User should logout successfully",
            action=dashboard.logout
        )

        self.teardown()
