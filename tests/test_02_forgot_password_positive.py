from base.base_test import BaseTest
from pages.login_page import LoginPage
from utils.safe_step import run_step


class TestForgotPasswordPositive(BaseTest):

    def test_forgot_password_positive(self):
        self.setup()

        login = LoginPage(self.driver, self.wait)

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

        self.teardown()
