from tests.constants import INVALID_LOGIN, INVALID_PASSWORD
import pytest


@pytest.mark.parametrize("invalid_log, invalid_pass", [(INVALID_LOGIN, INVALID_PASSWORD), (INVALID_LOGIN, ''),
                                                       ('', INVALID_PASSWORD), ('', '')])
def test_negative_login(create_login_page, create_authorization_page, invalid_log, invalid_pass):
    login_page = create_login_page
    authorization_page = create_authorization_page

    login_page.open_authorization_page()
    authorization_page.fill_fields(invalid_log, invalid_pass)
    authorization_page.click_login_button()
    assert authorization_page.show_error_massage()
