from tests.constants import VALID_LOGIN, VALID_PASSWORD


def test_login(create_main_page, create_login_page, create_authorization_page):
    main_page = create_main_page
    login_page = create_login_page
    authorization_page = create_authorization_page

    login_page.open_authorization_page()
    authorization_page.fill_fields(VALID_LOGIN, VALID_PASSWORD)
    authorization_page.click_login_button()
    assert main_page.is_main_page_opened()
    main_page.click_cancel_button()
    assert main_page.add_hub_button_displayed()
    assert main_page.add_first_hub_text_displayed()
    assert main_page.menu_button_displayed()