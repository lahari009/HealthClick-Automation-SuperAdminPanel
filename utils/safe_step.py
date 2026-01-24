from utils.bug_logger import BugLogger

# Single bug logger instance
bug_logger = BugLogger()


def format_actual_result(expected_result: str) -> str:
    """
    UNIVERSAL Actual Result generator.
    Works for ALL pages and ALL tests.
    Never produces ugly generic messages.
    """

    text = expected_result.strip()
    lower = text.lower()

    # -------- PAGE / UI STATE --------
    if "should open" in lower:
        return text.replace("should open", "was not open")

    if "should be visible" in lower:
        return text.replace("should be visible", "was not visible")

    if "should be displayed" in lower:
        return text.replace("should be displayed", "was not displayed")

    # -------- AUTH --------
    if "should login successfully" in lower:
        return "User did not login successfully"

    if "should logout successfully" in lower:
        return "User did not logout successfully"

    # -------- CREATE / SAVE / UPDATE --------
    if "should be created successfully" in lower:
        return text.replace(
            "should be created successfully",
            "was not created successfully"
        )

    if "should be updated successfully" in lower:
        return text.replace(
            "should be updated successfully",
            "was not updated successfully"
        )

    if "should be deleted successfully" in lower:
        return text.replace(
            "should be deleted successfully",
            "was not deleted successfully"
        )

    # -------- FORM VALIDATION --------
    if "all mandatory fields should be filled" in lower:
        return "All mandatory fields were not filled"

    # -------- SHORT ACTION PHRASES --------
    words = lower.split()

    if words[-1] == "saved":
        return text.replace(" saved", " was not saved")

    if words[-1] == "created":
        return text.replace(" created", " was not created")

    if words[-1] == "updated":
        return text.replace(" updated", " was not updated")

    if words[-1] == "deleted":
        return text.replace(" deleted", " was not deleted")

    if words[-1] == "completed":
        return text.replace(" completed", " was not completed")

    # -------- FINAL SAFE FALLBACK --------
    return f"{text} was not successful"


def run_step(module, page, step, expected, action):
    """
    Executes a test step.
    - PASSED → prints success
    - FAILED → logs bug
    - Execution CONTINUES till last step
    """

    try:
        action()
        print(f"✅ [{module}] {step} - PASSED")

    except (AssertionError, Exception) as e:
        print(f"❌ [{module}] {step} - FAILED")
        print(f"   Failure Reason: {str(e)}")

        actual_result = format_actual_result(expected)

        bug_logger.log_bug(
            module=module,
            page=page,
            scenario=step,
            steps=step,
            expected=expected,
            actual=actual_result,
            severity="High",
            status="FAILED"
        )

        # ❗ NO raise here → execution continues
        return
