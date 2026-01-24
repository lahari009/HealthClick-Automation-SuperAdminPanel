# HealthClick Automation – Super Admin Panel

## Project Overview
This project covers end-to-end automation testing of the HealthClick Super Admin panel. The automation validates the complete positive user flow to ensure that all core functionalities work accurately and smoothly across the application.

The automation framework is structured using standard industry practices, with a strong focus on maintainability, reusability, and scalability.

## Technology Stack
- Programming Language: Python
- Automation Tool: Selenium WebDriver
- Test Framework: Pytest
- Framework Design Pattern: Page Object Model (POM)
- Bug Tracking: Custom Automated Bug Logger
- Test Reporting: HTML-based Test Reports
- Version Control: Git
- Repository Hosting: GitHub

## Project Structure
HealthClick-Automation-SuperAdminPanel
├── base/        Base test setup and common utilities
├── pages/       Page Object classes
├── tests/       Automated test cases
├── utils/       Bug logger and helper utilities
├── HealthClick_Automation_Bug_Report.xlsx
├── .gitignore
├── README.md

## Automated Test Coverage
The automation suite validates the following functionalities:
- Login and Forgot Password
- Dashboard validations
- Menu and sub-menu navigation
- Form validations
- Filter and search operations
- CRUD operations where applicable
- Complete end-to-end user flow
- Logout functionality

## Bug Logging
A custom automated Bug Logger is integrated into the automation framework. Whenever a test failure occurs, the framework captures the failure details and logs them into an Excel-based bug report. The report includes module name, test scenario, expected and actual results, error details, and execution timestamp. This implementation reduces manual effort and improves defect traceability.

## Test Reporting
HTML-based automated test reports are generated after execution. The reports provide clear visibility of test execution results, including pass/fail status and overall execution summary.

## How to Run the Tests
1. Clone the repository  
git clone https://github.com/lahari009/HealthClick-Automation-SuperAdminPanel.git

2. Navigate to the project directory  
cd HealthClick-Automation-SuperAdminPanel

3. Create and activate a virtual environment  
python -m venv .venv  
.venv\Scripts\activate

4. Install dependencies  
pip install -r requirements.txt

5. Execute the test suite  
pytest

## Automation Execution Demo
Automation execution demo video link:  
( https://drive.google.com/file/d/1ZM6tb8Sup1bJfxhFEgo3DlJFJKvrYN-u/view?usp=sharing )

## Author
Alla Lahari
