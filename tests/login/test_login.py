from tests.page.login_page import LoginPage
from tests.page.main_page import MainPage
from tests.page.authorization_page import AuthorizationPage
from tests.constants import VALID_LOGIN, VALID_PASSWORD


def test_login(page_manager):
    pm = page_manager
    login_page = pm.create_page(LoginPage)
    login_page.open_authorization_page()
    authorization_page = pm.create_page(AuthorizationPage)
    authorization_page.fill_fields(VALID_LOGIN, VALID_PASSWORD)
    authorization_page.click_login_button()
    main_page = pm.create_page(MainPage)
    assert main_page.is_main_page_opened()
    main_page.click_cancel_button()
    assert main_page.add_hub_button_displayed()
    assert main_page.add_first_hub_text_displayed()
    assert main_page.menu_button_displayed()