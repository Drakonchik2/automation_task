from tests.page.login_page import LoginPage
from tests.constants import INVALID_LOGIN, INVALID_PASSWORD
from tests.page.authorization_page import AuthorizationPage


def test_negative_login(page_manager):
    pm = page_manager
    pm.reset_app()
    login_page = pm.create_page(LoginPage)
    login_page.open_authorization_page()
    authorization_page = pm.create_page(AuthorizationPage)
    authorization_page.fill_fields(INVALID_LOGIN, INVALID_PASSWORD)
    authorization_page.click_login_button()
    assert authorization_page.show_error_massage()
